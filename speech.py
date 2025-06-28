import speech_recognition as sr
from config import WAKE_WORD  # Optional wake word ("hey linux")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source, timeout=3, phrase_time_limit=5)
    try:
        text = r.recognize_google(audio).lower()  # Fastest online
        # OR for offline: r.recognize_vosk(audio)
        return text if WAKE_WORD in text else None
    except Exception as e:
        print(f"Error: {e}")
        return None