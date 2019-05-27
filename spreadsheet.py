from __future__ import print_function
import pickle
import os.path
import csv
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class Spreadsheet():

    def __init__(self, csv, sheet, range, credentials):
        self.csv = csv
        self.sheet = sheet
        self.range = range
        self.credentials = credentials
        # Scopes to read the spreadsheet'data'
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

        # The ID and range of spreadsheet.
        self.spreadsheet_id = self.sheet
        self.range_name = self.range

    def spreadsheet_call(self):
        # Creedentials of the project
        creds = self.credentials

        # The file token.pickle stores the user's access and refresh tokens,
        # and is created automatically when the authorization flow completes
        # for the first time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.scopes)
                creds = flow.run_local_server()

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=self.spreadsheet_id,
                                    range=self.range_name).execute()

        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
            with open(self.csv, 'w') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerows(values)
            print('Writing Data')
