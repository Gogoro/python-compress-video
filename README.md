# Python Compress Video

## Gaol
I have 5TB+ worth of videos stored on my NAS that are from livestreams I've done and YouTube videos.

Compressing all of these videos using Media Encoder is going to take a while and be cluncy. Also, I want this to just happen automatically whenever I save a recording.

Therefore I'm going to make the following functionality:
- [x] Distinguish between compressed and not compressed files
- [x] Set root folder, and automatically compress ALL videos in sub folders of this
- [x] Have good naming, so I can visually see what's been compressed. // Dropped this. Program detects if it needs to be compressed, that's enough.

## Usage

### Warning
This script runs through all the sub folders to the base folder you define and finds `.mp4` files and compresses them. After it's done running, it deletes the original and replaces that with the new file. 
So, if the process failes. It should not delete the original. 
But if the process is successful, you will loose your original file.

### Running the command
1. Install `ffmpeg`
2. Instal dependencies `python3 pip install -r requirements.txt`
2. Run compression with `python3 compress-video.py test/` // Change `test/` to your base path.