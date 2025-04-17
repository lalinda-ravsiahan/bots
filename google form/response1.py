import os
import json
import google.auth.transport.requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first time.
TOKEN_FILE = 'token.json'
CREDENTIALS_FILE = 'client_secret_427892765744-5im5shv7rea450qahbao7dm0nk3fnglv.apps.googleusercontent.com.json'
SCOPES = ['https://www.googleapis.com/auth/forms.responses.readonly']

def get_credentials():
    creds = None
    # Check if the token file exists
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    # If there are no valid credentials, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(google.auth.transport.requests.Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    return creds

def main():
    creds = get_credentials()
    service = build('forms', 'v1', credentials=creds)

    # Replace with your form ID
    form_id = '1or3QGLyvZmATDuriaKa2deGpX7jsrQCp19FBTdoa9cw'

    # Fetch responses
    response = service.forms().responses().list(formId=form_id).execute()
    print(response["responses"][0]["answers"]['32cb09a9']['textAnswers']["answers"])#birthdays
    print(response["responses"][0]["answers"]['6409e234']['fileUploadAnswers'])#photoes
    print(response["responses"][0]["answers"]["110c0a85"]["textAnswers"])#name
    #print(json.dumps(response, indent=2))

if __name__ == '__main__':
    main()
