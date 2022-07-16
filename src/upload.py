from __future__ import print_function
from email.mime import base
from mimetypes import MimeTypes
import os
from pathlib import Path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

class Upload:
    
    def upload_file(creds, file_path, folder_id = None):
        """Insert new file on drive.
        Returns : Id's of the file uploaded.
        """
        
        try:
            service = build('drive', 'v3', credentials=creds)

            basename = os.path.basename(file_path)
            file_name = os.path.splitext(basename)[0]
            
            mime_type = MimeTypes().guess_type(basename)[0]

            if(folder_id == None):
                file_metadata = {'name': file_name}
            else:
                file_metadata = {'name': file_name, 'parents': [folder_id]}
     
            media = MediaFileUpload(file_path, mimetype=mime_type)
            
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

            with open("folder_register.txt", "a",) as registro:
                registro.write("File path: " + file_path + " - File ID:" + file.get("id") + "\n")
            print(F'File ID: {file.get("id")}')
            
        except HttpError as error:
            print(F'An error occurred: {error}')
            file = None

        return file.get('id')

    def create_folder(creds, path, folder_id = None):
        """ Create a folder on drive.
        Returns : Folder Id.
        """

        try:
            service = build('drive', 'v3', credentials=creds)
            
            folder_name = os.path.basename(path)

            if(folder_id == None):
                file_metadata = {
                    'title': folder_name,
                    'name': folder_name,
                    'mimeType': 'application/vnd.google-apps.folder'
                }
            else:
                file_metadata = {
                    'title': folder_name,
                    'name': folder_name,
                    'parents': [folder_id],
                    'mimeType': 'application/vnd.google-apps.folder'
                }

            file = service.files().create(body=file_metadata, fields='id').execute()

            with open("folder_register.txt", "a",) as registro:
                registro.write("Folder path: " + path + " - Folder ID:" + file.get("id") + "\n")
            print(F'Folder has created with ID: "{file.get("id")}".')

        except HttpError as error:
            print(F'An error occurred: {error}')
            file = None

        return file.get('id')