from __future__ import print_function
import pandas as pd
# from google.oauth2 import service_account
from tqdm import tqdm


def clean_load(ds, **kwargs):
    url = 'https://docs.google.com/spreadsheet/ccc?key='
    sheet = url + '1oYPhZbGVOJPrmmvoJ23ZjKubmV4KpBgle3uQaP7_Dyw&output=csv'
    # Download the spreadsheet as CSV
    data = pd.read_csv(
        sheet
        )
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

    # Dictionary for the moths
    month = {'November': '11',
             'December': '12'}

    # Split the NaN values
    data['quarter_hour'] = (data['quarter_hour'].fillna('00:00'))

    # datetime.timedelta(hours=0000)))
    data['category'] = data['category'].fillna('N/A')

    # Replace data
    data['month'] = data.month.map(month)

    data['date'] = pd.to_datetime(dict(year=data['year'],
                                       month=data['month'],
                                       day=data['day_of_month']),
                                  utc=True)

    print('-' * 50)
    print('After Data split.')
    print('-' * 50)

    # Describe all the fileds after the treatment
    print(data.describe(include='all'))

    # To print the table in command line
    # print(data.head)
    try:

        # data.to_csv('dataset/data_changed.csv', index=False)
        data.to_gbq('PRUEBAS_GCP.testJalfonsoBQ',
                    if_exists='replace',
                    project_id='test-jalfonso'
                    # credentials=credentials
                    )

    except Exception as e:
        print("General exception: ", e)
