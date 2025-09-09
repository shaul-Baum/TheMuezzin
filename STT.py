import speech_recognition as sr
from Logger import Logger

logger = Logger.get_logger()
def stt(files_paths):

    # Initialize the recognizer
    r = sr.Recognizer()
    audio_file_path = files_paths

    try:
        with sr.AudioFile(audio_file_path) as source:
            audio_data = r.record(source)

        text = r.recognize_google(audio_data)
        print("Transcribed Text:", text)
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