import os
import ffmpeg
import subprocess
import sys

# Get input from the user with the path to the directory with the videos
if len(sys.argv) == 1:
    print('Please provide a path to the directory with the videos')
    sys.exit()

print('Compressing videos in: ', sys.argv[1])
basepath = sys.argv[1]

# List all files in a directory using os.listdir
files_in_basepath = os.listdir(basepath)

# Filter out all files that are not video files
# Filter out all files that are already compressed
# Filter out all files that has a compressed version
files_in_basepath = [file for file in files_in_basepath if file.endswith('.mp4') and not file.startswith('compressed-') and not 'compressed-' + file in files_in_basepath]

# Fill this variable with files that we are going to compress 
files_to_compress = []

# Check if file is not compressed and is a video file
for file_in_basepath in files_in_basepath:
    cmd = ['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=bit_rate', '-of', 'default=noprint_wrappers=1:nokey=1', basepath + file_in_basepath]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = process.communicate()[0]
    print(output)
    if int(output) < 6850000:
        print('File is already compressed', file_in_basepath)
    elif file_in_basepath.endswith('.mp4'):
        files_to_compress.append(file_in_basepath)

# Compress all files in the list
print('Files to compress: ', files_to_compress)
for file_to_compress in files_to_compress:
    print('Compressing: ', file_to_compress)
    # Compression command
    ffmpeg.input(basepath + file_to_compress).output(basepath + 'compressed-' + file_to_compress, **{'c:v': 'h264_videotoolbox', 'c:a': 'aac', 'b:v': '6800k'}).run()
    # Delete the original file
    os.remove(basepath + file_to_compress)
    # Rename the compressed file to the original name
    os.rename(basepath + 'compressed-' + file_to_compress, basepath + file_to_compress)
    print('Done compressing: ', file_to_compress)
