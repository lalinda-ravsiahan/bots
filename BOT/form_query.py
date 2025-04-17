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

def get_form_responses(form_id):
    
    creds_read_responses = get_credentials(READ_RESPONSES_SCOPES, TOKEN_READ_RESPONSES)
    service_read_responses = build('forms', 'v1', credentials=creds_read_responses)

    responses = service_read_responses.forms().responses().list(formId=form_id).execute()

    return responses



def main():
    response=get_form_responses("1loG11rbHJlGUvlYBgKZAs-GgwtRP_kGH5SpVnfNjbpQ")

    print(len(response["responses"]))

    for i in response["responses"]:
        print(i["answers"]["5bd21089"]["textAnswers"]["answers"][0]["value"])
        print(i["answers"]["5ccd54f1"]["textAnswers"]["answers"][0]["value"])
        print(i["answers"]["18cc91e4"]["fileUploadAnswers"]["answers"][0]["fileId"])
        print()
    

    print(response["responses"][1]["answers"])

    """
    print(response["responses"][0]["answers"]['32cb09a9']['textAnswers']["answers"])#birthdays
    print(response["responses"][0]["answers"]['6409e234']['fileUploadAnswers'])#photoes
    print(response["responses"][0]["answers"]["110c0a85"]["textAnswers"])#name
    """


"""

def main():

    form_id=""

    creds_read_responses = get_credentials(READ_RESPONSES_SCOPES, TOKEN_READ_RESPONSES)
    service_read_responses = build('forms', 'v1', credentials=creds_read_responses)
    responses = get_form_responses(service_read_responses, form_id)
    print(f"Responses: {responses}")


if __name__=="__main__":
    main()

    """

if __name__=="__main__":
    main()