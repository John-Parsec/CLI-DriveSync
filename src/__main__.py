from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import sys
from icecream import ic
from src.sync import Sync
from src.authentication import Authentication
from src.upload import Upload

def main():
    ic('CLI-Driver started')

    creds = Authentication.auth()

    args = sys.argv[1:]
    ic('The args called: ', args)
    
    if args[0] == 'list':
        try:
            service = build('drive', 'v3', credentials=creds)

            results = service.files().list(
                pageSize=10, fields="nextPageToken, files(id, name)").execute()
            items = results.get('files', [])

            if not items:
                print('No files found.')
                return
            
            ic('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
        except HttpError as error:
            ic(f'An error occurred: {error}')

    elif args[0] == 'upfile':
        Upload.upload_file(creds, args[1])
    
    elif args[0] == 'sync':
        Sync.sync(creds, args[1])

    elif args[0] == 'teste':
        ic('teste')

    else:
        ic("Comando não reconhecido!")


if __name__ == '__main__':
    main()
