# ffmpeg -y -i /dev/video0 cam.mkv
dims=$(xdpyinfo | grep dimensions | awk '{print $2;}')
ffmpeg -y -f x11grab -s $dims -i :0.0 screen.mkv & # screen recording
# mpv --no-keepaspect-window /dev/video0 get cam footage ; this kinda works but fucks up cpu
# Joining and editing audio:
ffmpeg -i screen.mkv -vf "movie=cam.webm, scale=400: -1 [inner]; [in][inner] overlay=main_w-(overlay_w+10):10 [out]" sync.mp4
ffmpeg -i cam.webm -vn audio.wav
ffmpeg -i sync.mp4 -i audio.wav -map 0:v -map 1:a -c:v copy -shortest final-output.mp4
ffmpeg -i {INT} {FILTER} ? -vf | -af | -filter_complex {COMPLEX} {FORMAT} {RATE} {OUT}
