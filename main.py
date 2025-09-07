# import time
from Loader import Loader
from ExtractingMetadata import ExtractingMetadata
import json
from Producer import Produce
from consumer import Consumer
Produce = Produce()
loader = Loader("data/")
files_paths = loader.file_path()
for path in files_paths:
    metadata = ExtractingMetadata.extracting_file_metadata(path)
    json_string = json.dumps(metadata)
    Produce.publish_message("File_details",metadata)
consumer = Consumer("File_details")
print(consumer.reading_message())
