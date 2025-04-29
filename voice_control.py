import speech_recognition as sr
import pyttsx3

class VoiceController:
    def __init__(self, callback_fn):
        self.callback = callback_fn

        # Initialize recognizer and text‑to‑speech engine
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()

        # (Optional) adjust for ambient noise
        with sr.Microphone() as mic:
            self.recognizer.adjust_for_ambient_noise(mic, duration=1)

    def speak(self, text):
        """Give verbal feedback via speakers."""
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def listen_forever(self):
        """Continuously listen for voice commands."""
        with sr.Microphone() as mic:
            while True:
                try:
                    print("Listening...")
                    audio = self.recognizer.listen(mic, phrase_time_limit=4)
                    command = self.recognizer.recognize_google(audio)
                    print(f"Recognized: {command}")

                    # Invoke the callback in main.py
                    self.callback(command)

                    # (Optional) confirm with TTS
                    self.speak(f"You said: {command}")

                except sr.UnknownValueError:
                    # Speech was unintelligible
                    pass
                except sr.RequestError as e:
                    # API was unreachable or unresponsive
                    print(f"Speech API error: {e}")
