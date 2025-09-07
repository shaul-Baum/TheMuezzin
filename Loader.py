
import os

class Loader:
    def __init__(self,folder_path:str):
        self.folder_path = folder_path
        self.entries = os.listdir(self.folder_path)

    def file_path(self) -> list[str] :
        for i,path in enumerate(self.entries):
            path = str(path)
            wav_file_path = self.folder_path + path
            self.entries[i] = wav_file_path
        return self.entries
