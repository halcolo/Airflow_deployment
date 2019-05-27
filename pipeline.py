from spreadsheet import Spreadsheet
from clean_data import Clean_data
from variables import (CSV, BQ, CRED_BQ,
                       SHEET, RANGE, CRED_SHEET)


if __name__ == '__main__':

    # Creating the variables from csv and objects
    etl = Clean_data(CSV, BQ, CRED_BQ)
    sheet = Spreadsheet(CSV, SHEET, RANGE, CRED_SHEET)

    # Call methods
    sheet.spreadsheet_call()
    etl.getData()
