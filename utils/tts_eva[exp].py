# The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
# The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
# Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
# All such material is used with the permission of the owner.
# All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
# All Rights Reserved.

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
