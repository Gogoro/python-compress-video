# Python Compress Video

## Usage

### ⚠️ Warning
This script operates by traversing all subfolders from the defined base folder, identifying `.mp4` files, and compressing them. Once the compression process is complete, the original files are deleted and replaced with the compressed versions. However, if the process encounters any errors, it will not delete the original files.

### Running the Command
Follow the steps below to utilize this video compression automation tool:

1. Install `ffmpeg`.
2. Install the required dependencies by running the following command: `python3 -m pip install -r requirements.txt`
3. Execute the compression process by running the following command: `python3 compress-video.py /path/to/your/videos/`
Replace `/path/to/your/videos/` with the absolute path to the directory containing the videos you want to compress.

## Contribution
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
