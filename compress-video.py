import ffmpeg

ffmpeg.input('test/original.mp4').output('test/compressed.mp4', **{'c:v': 'h264_videotoolbox', 'c:a': 'aac', 'b:v': '6800k'}).run()