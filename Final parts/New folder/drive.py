import os
import pickle
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pyrogram import Client, filters

async def drive_handle(app):
    # Google Drive API scopes
    SCOPES = ['https://www.googleapis.com/auth/drive.file']

    def authenticate_google_drive():
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('client_secret_427892765744-5im5shv7rea450qahbao7dm0nk3fnglv.apps.googleusercontent.com.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('drive', 'v3', credentials=creds)
        return service

    def upload_to_google_drive(service, file_path, file_name, folder_id):
        file_metadata = {
            'name': file_name,
            'parents': [folder_id]
        }
        media = MediaFileUpload(file_path, mimetype='image/jpeg')
        file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    # Authenticate Google Drive
    drive_service = authenticate_google_drive()

    @app.on_message(filters.photo)
    async def handle_photo(client, message):
        # Download the photo
        file_path = await message.download()
        print(f"Photo downloaded to: {file_path}")

        # Prepare the file for Google Drive
        file_name = f"{message.photo.file_unique_id}.jpg"
        folder_id ="1Sozo47GnwbzBgG0nUJdpLtuizgkjSQNZ"


        # Upload the photo to Google Drive
        file_id = upload_to_google_drive(drive_service, file_path, file_name,folder_id)
        print(f"Photo uploaded to Google Drive with file ID: {file_id}")

        # Respond to the user
        await message.reply_text("Photo received and uploaded to Google Drive!")
        print(message.text)
        # Optionally, clean up the downloaded file
        os.remove(file_path)