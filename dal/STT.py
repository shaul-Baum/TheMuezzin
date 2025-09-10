import speech_recognition as sr
from dal.Logger import Logger
import base64

logger = Logger.get_logger()
class STT:

    @staticmethod
    def stt(files_paths):
        r = sr.Recognizer()
        audio_file_path = files_paths
        try:
            with sr.AudioFile(audio_file_path) as source:
                audio_data = r.record(source)

            text = r.recognize_google(audio_data)
            logger.info("Text output was successful.")
            return text
        except sr.UnknownValueError:
            logger.error("Speech Recognition could not understand audio.")
            print("Speech Recognition could not understand audio.")
        except sr.RequestError as e:
            logger.error(f"Could not request results from Google Speech Recognition service; {e}")
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except FileNotFoundError:
            print(f"Error: The audio file '{audio_file_path}' was not found.")
            logger.error(f"Error: The audio file '{audio_file_path}' was not found.")

    @staticmethod
    def bas64_to_str(base64_string:str)->str:
        decoded_bytes = base64.b64decode(base64_string)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string