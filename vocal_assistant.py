from pyttsx3 import init
from speech_recognition import Recognizer, Microphone
from datetime import datetime
import webbrowser
from random import choice

engine = init()
voices = engine.getProperty("voices")
for voice in voices:
    print(voice)
engine.setProperty('voice', voices[0].id)
engine.say("Simone, dimmi, cosa posso fare per te?")
engine.runAndWait()
r = Recognizer()

with Microphone() as source:
    print('pronto ad ascoltare...')
    audio = r.listen(source)
    # Ricordare di convertire il testo in minuscolo in modo che le condizioni non siano influzenzate da lettere maiuscole
    text = r.recognize_google(audio, language="it-IT").lower()
    response = "mmmmmmmm..non sò proprio come aiutarti"
    print(text)
    if "article" in text:
        with open("article.txt", "w") as f:
            f.write("This is the .txt file")
        response = "Ho creato per te un testo con la descrizione dell'articolo che cercavi"
    elif any(word in text for word in ["ore", "ora", "orario"]):
        webbrowser.open("https://www.google.com/search?q=time&rlz=1C1ONGR_itIT930IT930&oq=time&aqs=chrome..69i57j0i131i433i512j69i59j69i65l2j69i60j69i61l2.1287j0j9&sourceid=chrome&ie=UTF-8")
        response = f"sono le ore {datetime.now().strftime('%H e %M')}"
        print(response)
    elif text.startswith(("cosa", "come", "quanto")):
        response = choice(["vediamo..fammi pensare", "fai prima a cercare su google"])
    engine.say(response)
    engine.runAndWait()
