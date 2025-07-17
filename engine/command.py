import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 150)
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print('Recognizing...')
        eel.DisplayMessage("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        eel.DisplayMessage(query)
        speak(query)
        eel.ShowHood()
        return query.lower()
    except Exception as e:
        print("Error:", e)
        speak("Sorry, I did not catch that.")
        eel.ShowHood()  # ✅ Switch UI back
        return ""
