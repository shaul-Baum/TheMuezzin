import os
from dal.Logger import Logger
logger = Logger.get_logger()

class ExtractingMetadata:
    def __init__(self):
        pass
    @staticmethod
    def extracting_file_metadata(wav_file_path) -> dict[str:str] :
        file_path = wav_file_path
        if os.path.exists(file_path):
            last_modified_datetime = str(os.path.getmtime(file_path))
            file_size = os.path.getsize(file_path)
            creation_datetime = str(os.path.getctime(file_path))
            logger.info("Metadata extraction was successful.")
            return {"file_path":file_path,"Last modified":last_modified_datetime,"file size":file_size,"Created":creation_datetime}
        else:
            logger.error(f"File not found :{file_path}")
            return {"File not found":file_path}



