# Python Compress Video

This small script takes `.mp4` videos located in the target folder and sub folders, and compresses them into ~6800kb/s videos. 

Warning: This scripts replaces your original files with the compressed version. So do some tests before you run it on your important files. 

## Requirements
- [Install ffmpeg](https://www.ffmpeg.org/)
- Install python dependencies `pip install -r requirements.txt`

## Running the Command

``` bash
$ python3 compress-video.py /path/to/your/videos/
```

Change the path to be the root folder of where you want to compress videos.

## Potential future improvements
Currently, the script is just doing a spesific task for me. If there is need or interest, I can add more features. 

Some potential features:
- [ ] Set target bitrate from cmd
- [ ] Relative basepath
- [ ] Support more file types

## Contribution
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
