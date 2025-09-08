from Loader import Loader
from ExtractingMetadata import ExtractingMetadata
import json
from Producer import Produce

if __name__ == "__main__":
    topic = "File_details"
    Produce = Produce()
    loader = Loader("data/")
    files_paths = loader.file_path()
    for path in files_paths:
        metadata = ExtractingMetadata.extracting_file_metadata(path)
        json_string = json.dumps(metadata)
        Produce.publish_message(topic,metadata)


