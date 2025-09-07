# from pathlib import Path
import os
import time
import datetime

class ExtractingMetadata:
    def __init__(self):
        pass
    @staticmethod
    def extracting_file_metadata(wav_file_path):
        file_path = wav_file_path
        if os.path.exists(file_path):
            mod_timestamp = os.path.getmtime(file_path)
            last_modified_datetime = datetime.datetime.fromtimestamp(mod_timestamp)
            last_modified_datetime = str(last_modified_datetime)
            file_size = os.path.getsize(file_path)
            creation_timestamp = os.path.getctime(file_path)
            creation_datetime = datetime.datetime.fromtimestamp(creation_timestamp)
            creation_datetime = str(creation_datetime)
            return {"file_path":file_path,"Last modified":last_modified_datetime,"file size":file_size,"Created":creation_datetime}
        else:
            return {"File not found":file_path}



