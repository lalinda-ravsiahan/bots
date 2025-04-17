import os
import json
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Define the scope
SCOPES = ['https://www.googleapis.com/auth/forms.body']

# Token file to store the user's access and refresh tokens
TOKEN_PATH = 'token.pickle'
# Credentials file obtained from Google Cloud Console
CREDENTIALS_PATH = 'client_secret_427892765744-5im5shv7rea450qahbao7dm0nk3fnglv.apps.googleusercontent.com.json'

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first time.
TOKEN_FILE = 'token.json'
CREDENTIALS_FILE = 'client_secret_427892765744-5im5shv7rea450qahbao7dm0nk3fnglv.apps.googleusercontent.com.json'
SCOPES = ['https://www.googleapis.com/auth/forms.responses.readonly']

def get_credentials():
    creds = None

    # Check if token file exists
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'rb') as token_file:
            creds = pickle.load(token_file)

    # If there are no valid credentials, request authorization
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(TOKEN_PATH, 'wb') as token_file:
            pickle.dump(creds, token_file)

    return creds


def responses():
    creds = get_credentials()
    service = build('forms', 'v1', credentials=creds)

    # Replace with your form ID
    form_id = '1or3QGLyvZmATDuriaKa2deGpX7jsrQCp19FBTdoa9cw'
    create_google_form(service)


'''
    # Fetch responses
    response = service.forms().responses().list(formId=form_id).execute()
    print(response["responses"][0]["answers"]['32cb09a9']['textAnswers']["answers"])#birthdays
    print(response["responses"][0]["answers"]['6409e234']['fileUploadAnswers'])#photoes
    print(response["responses"][0]["answers"]["110c0a85"]["textAnswers"])#name
    #print(json.dumps(response, indent=2))

    '''

    
def create_google_form(service):
    # Define the form content
    form = {
        "info": {
            "title": "Test Form",
            "documentTitle": "Test Form Document",
            "description": "This is a test form created using Google Forms API."
        },
        "items": [
            {
                "title": "Sample Question",
                "questionItem": {
                    "question": {
                        "required": True,
                        "textQuestion": {
                            "paragraph": False
                        }
                    }
                }
            }
        ]
    }

    # Create the form
    created_form = service.forms().create(body=form).execute()
    print(f"Form created: {created_form['responderUri']}")

if __name__ == '__main__':
    responses()
