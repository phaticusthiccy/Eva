from gtts import gTTS
from pygame import mixer

import mutagen.mp3


while True:
    query = input("query: ")
    tts = gTTS(text=query, lang='ko')
    tts.save("./out.mp3")

    mp3 = mutagen.mp3.MP3("./out.mp3")

    mixer.init(frequency=mp3.info.sample_rate)
    mixer.music.load("./out.mp3")
    mixer.music.play()
