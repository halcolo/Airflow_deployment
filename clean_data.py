from __future__ import print_function
import pandas as pd
from google.oauth2 import service_account
from tqdm import tqdm


class Clean_data():
    def __init__(self, csvFile, bqDatabase, credentials):
        # Variables recived
        self.csvFile = csvFile
        self.bqDatabase = bqDatabase
        self.credentials = credentials
        self.query = '''SELECT *
                        FROM <CHANGE FOR YOUR BQ.DB>'''

    def getData(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials
            )
        data = pd.read_csv(self.csvFile)

        # Count the total files
        print(data.count())
        print('-' * 50)
        print('Before Data split.')
        print('-' * 50)

        # Describe all the fields before the treatment
        print(data.describe(include='all'))
        print('\n' + 'Transforming Data')
        for i in tqdm(range(int(1e3))):
            pass

        # # Dictionary for the moths
        # month = {'November': '11',
        #          'December': '12'}
        #
        # Split the NaN values
        data['quarter_hour'] = (data['quarter_hour'].fillna('00:00'))
        #
        # # datetime.timedelta(hours=0000)))
        # data['category'] = data['category'].fillna('N/A')
        #
        # # Replace data
        # data['month'] = data.month.map(month)
        #
        # data['date'] = pd.to_datetime(dict(year=data['year'],
        #                                    month=data['month'],
        #                                    day=data['day_of_month']),
        #                               utc=True)

        print('-' * 50)
        print('After Data split.')
        print('-' * 50)

        # try:
        #     data_verify = pd.read_gbq(self.query,
        #                               credentials=credentials,
        #                               project_id='test-jalfonso'
        #                               # ,
        #                               # dialect="legacy"
        #                               )
        #     print(data_verify.head)
        #     new_data = pd.contact([data, data_verify])
        #     new_data = new_data.drop_duplicates(Keep=False)
        #     print('ńewdata')
        #     print(new_data.head)
        # except Exception as e1:
        #     print("General exception: ", e1)
        # Describe all the fileds after the treatment
        # print(data.describe(include='all'))

        # To print the table in command line
        # print(data.head)
        try:
            # data.to_csv(self.csvFile, index=False)
            data.to_gbq(self.bqDatabase,
                        if_exists='replace',
                        credentials=credentials
                        )

        except Exception as e2:
            print("General exception: ", e2)
