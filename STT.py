import speech_recognition as sr

def stt(files_paths):
    # Initialize the recognizer
    r = sr.Recognizer()
    audio_file_path = files_paths

    try:
        # Load the audio file
        with sr.AudioFile(audio_file_path) as source:
            audio_data = r.record(source)  # Read the entire audio file

        # Transcribe the audio using Google Speech Recognition
        text = r.recognize_google(audio_data)
        print("Transcribed Text:", text)

    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except FileNotFoundError:
        print(f"Error: The audio file '{audio_file_path}' was not found.")