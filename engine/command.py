import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 1 = female, 0 = male
    engine.setProperty('rate', 150) 
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, timeout=10, phrase_time_limit=6)
        
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print("Error:", e)
        return ""
    
    return query.lower()

text = takecommand()
if text:
    speak(text)
else:
    speak("I did not catch that. Please try again.")
