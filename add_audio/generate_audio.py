import pyttsx3
import hashlib

engine = pyttsx3.init("sapi5")
def print_available_voices():
   print(engine.getProperty("voices"))

def text_to_mp3(text):
    engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0")

    sha1 = hashlib.sha1()
    sha1.update(text.encode('utf-8'))
    hash_hex = sha1.hexdigest()

    engine.save_to_file(text, f'{hash_hex}.mp3')
    engine.runAndWait()
