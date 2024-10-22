from gtts import gTTS
import os

def convert_text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    audio_file = "output.mp3"
    audio_path = os.path.join('./static/uploads/', audio_file)
    tts.save(audio_path)
    return audio_file
