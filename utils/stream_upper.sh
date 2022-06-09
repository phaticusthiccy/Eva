# The entire Eva Application is Copyright ©2021 by Phaticusthiccy.
# The Eva site may not be copied or duplicated in whole or part by any means without express prior agreement in writing or unless specifically noted on the site.
# Some photographs or documents contained on the application may be the copyrighted property of others; acknowledgement of those copyrights is hereby given.
# All such material is used with the permission of the owner.
# All Copyright Belong to Phaticusthiccy - (2017-2021) Eva 
# All Rights Reserved.


# ffmpeg -y -i /dev/video0 cam.mkv
dims=$(xdpyinfo | grep dimensions | awk '{print $2;}')
ffmpeg -y -f x11grab -s $dims -i :0.0 screen.mkv & # screen recording
# mpv --no-keepaspect-window /dev/video0 get cam footage ; this kinda works but fucks up cpu
# Joining and editing audio:
ffmpeg -i screen.mkv -vf "movie=cam.webm, scale=400: -1 [inner]; [in][inner] overlay=main_w-(overlay_w+10):10 [out]" sync.mp4
ffmpeg -i cam.webm -vn audio.wav
ffmpeg -i sync.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -shortest final-output.mp4
ffmpeg -i {INT} {FILTER} ? -vf | -af | -filter_complex {COMPLEX} {FORMAT} {RATE} {OUT}
