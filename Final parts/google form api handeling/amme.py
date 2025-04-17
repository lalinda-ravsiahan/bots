import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CREATE_FORM_SCOPES = ['https://www.googleapis.com/auth/forms.body']
READ_RESPONSES_SCOPES = ['https://www.googleapis.com/auth/forms.responses.readonly']

TOKEN_CREATE_FORM = 'token_create_form.pickle'
TOKEN_READ_RESPONSES = 'token_read_responses.pickle'
CREDENTIALS_PATH = 'client_secret_427892765744-5im5shv7rea450qahbao7dm0nk3fnglv.apps.googleusercontent.com.json'

def get_credentials(scopes, token_path):
    creds = None
    if os.path.exists(token_path):
        with open(token_path, 'rb') as token_file:
            creds = pickle.load(token_file)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, scopes)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'wb') as token_file:
            pickle.dump(creds, token_file)
    return creds

def create_form(service):
    form_metadata = {
        "info": {
            "title": "Automated Birthday Card Generator ",
        }
    }
    form = service.forms().create(body=form_metadata).execute()
    return form

def add_questions(service, form_id):
    requests = {
        "requests": [
            {
                "updateFormInfo": {
                    "info": {
                        "description": "This Form Is Collecting Your Information For Generate Your Birthday Card At Your Birthday\nPlz Provide Correct Information!!\n<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>"
                    },
                    "updateMask": "description"
                }
            },
            {
                "createItem": {
                    "item": {
                        "title": "Enter a short answer",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "textQuestion": {}
                            }
                        }
                    },
                    "location": {
                        "index": 0
                    }
                }
            },
            {
                "createItem": {
                    "item": {
                        "title": "Enter your birth date",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "dateQuestion": {}
                            }
                        }
                    },
                    "location": {
                        "index": 1
                    }
                }
            },
            {
                "createItem": {
                    "item": {
                        "title": "To upload your photo please visit this link",
                        "description": "Please visit https://script.google.com/macros/s/AKfycbxUiYfJ7mbUB-hCZvlqUUCdn7bp7ioV7oZu8PvVxEgpscUWowc3r6YL62eXmLdWQC_XNg/exec for more information.",
                        "questionItem": {
                            "question": {
                                "required": False,
                                "textQuestion": {}
                            }
                        }
                    },
                    "location": {
                        "index": 2
                    }
                }
            }
            
        ]
    }
    service.forms().batchUpdate(formId=form_id, body=requests).execute()

def get_form_responses(service, form_id):
    responses = service.forms().responses().list(formId=form_id).execute()
    return responses

def main():
    # Step 1: Create Form
    creds_create_form = get_credentials(CREATE_FORM_SCOPES, TOKEN_CREATE_FORM)
    service_create_form = build('forms', 'v1', credentials=creds_create_form)
    form = create_form(service_create_form)
    form_id = form['formId']
    print(f"Form created: {form['responderUri']}")
    print(f"Form ID: {form_id}")

    # Step 2: Add Questions
    add_questions(service_create_form, form_id)
    print("Questions added.")

    # Step 3: Retrieve Responses
    creds_read_responses = get_credentials(READ_RESPONSES_SCOPES, TOKEN_READ_RESPONSES)
    service_read_responses = build('forms', 'v1', credentials=creds_read_responses)
    responses = get_form_responses(service_read_responses, form_id)
    print(f"Responses: {responses}")

if __name__ == '__main__':
    main()
