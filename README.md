# checksumthing
The ultimate checksum script! Checksumthing helps you create different kinds of checksum sidecar files.

## What is checksumthing?
checksumthing helps you transform your checksum files in the format that you want. Different pieces of software used to produce checksums create sidecar files (typically files ending in .md5 or .sha1) with very different formatting, which creates headaches for archivists—we love standards and loathe disorder. Checksumthing is a python script that can solve this problem by allowing users to transform the data inside sidecar files into a standardized format most convenient for them. For example, you can:
* Append text before or after the checksum value (like the path to the file or the filename)
* Change the checksum text to all caps or all lowercase
* Search for checksum files and transform files through a nested directory structure

Checksumthing currently supports MD5, SHA1, and SHA256 checksums. Right now the script only supports plaintext sidecar files. In the future, we hope to support CSV and other types of files.

## Software Requirements and Compatibility
* Mac OS X with Python 2.7 or 3.0
* Windows 10 and Linux with Python 2.7

## How to Run or Install
You can run checksumthing straight out of the box by [cloning the repostory](https://help.github.com/articles/cloning-a-repository/), opening up the command line (Terminal in Mac OS X), navigating to the "checksumthing" directory, and running `$ python checksumthing.py` along with any arguments that you need. 

There is also an install process that allows you run checksumthing as a regular command. To install, clone the repository and then navigate to your checksumthing directory. Run `$ python setup.py install`. To test your install run `$ checksumthing -h`. You should see the help menu.

For more information on running checksumthing please see the [online documentation][1]. 

[1]: https://amiaopensource.github.io/checksumthing/
