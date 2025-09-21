from gtts import gTTS

def speak_text(text, filename="response.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    return filename