from Loader import Loader
from ExtractingMetadata import ExtractingMetadata
import json
from dal.Producer import Produce
import Variables

if __name__ == "__main__":
    topic = Variables.TOPIC
    Produce = Produce()
    loader = Loader(Variables.FILES)
    files_paths = loader.file_path()
    for path in files_paths:
        metadata = ExtractingMetadata.extracting_file_metadata(path)
        json_string = json.dumps(metadata)
        Produce.publish_message(topic,metadata)



