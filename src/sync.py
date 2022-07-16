import os

from src.upload import Upload

class Sync:
    def sync(creds, folder_path, folder_id = None):        
        if(folder_id == None):
            folder_id = Upload.create_folder(creds, folder_path)
        
        if(os.path.exists(folder_path)):
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    if dirpath == folder_path:
                        path = os.path.join(dirpath, filename)
                        Upload.upload_file(creds, path, folder_id)

                for dirname in dirnames:
                    path = os.path.join(dirpath, dirname)
                    if dirpath == folder_path and os.listdir(path):
                        id = Upload.create_folder(creds, dirname, folder_id)
                        Sync.sync(creds, path, id)
