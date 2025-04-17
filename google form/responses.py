from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage("token.json")
creds = None
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets("client_secret_427892765744-5im5shv7rea450qahbao7dm0nk3fnglv.apps.googleusercontent.com.json", SCOPES)
  creds = tools.run_flow(flow, store)
service = discovery.build(
    "forms",
    "v1",
    http=creds.authorize(Http()),
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False,
)

# Prints the responses of your specified form:
form_id = "1Ht_Qc-qKKTEoImsavlz5zNy1fm7yZ_dLSNq0QKwCME"
result = service.forms().responses().list(formId=form_id).execute()
print(result)