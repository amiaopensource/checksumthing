# checksumthing
The ultimate checksum script! Checksumthing helps you create different kinds of checksum sidecar files.

## What is checksumthing?
checksumthing helps you transform your checksum files in the format that you want. Different pieces of software used to produce checksums create sidecar files (typically files ending in .md5 or .sha1) with very different formatting, which creates headaches for archivists—we love standards and loathe disorder. Checksumthing is a python script that can solve this problem by allowing users to transform the data inside sidecar files into a standardized format most convenient for them. For example, you can:
* Append text before or after the checksum value (like the path to the file or the filename)
* Change the checksum text to all caps or all lowercase
* Search for checksum files and transform files through a nested directory structure

Checksumthing currently supports MD5, SHA1, and SHA256 checksums. Right now the script only supports plaintext sidecar files. In the future, we hope to support CSV and other types of files.

## Software Requirements and Compatibility
* Mac OS X with Python 2.7 or 3.x
* Windows 10 and Linux with Python 2.7

## How to Run or Install
You can run checksumthing straight out of the box by [cloning the repostory](https://help.github.com/articles/cloning-a-repository/), opening up the command line (Terminal in Mac OS X), navigating to the "checksumthing" directory, and running `$ python checksumthing.py` along with any arguments that you need. 

There is also an install process that allows you run checksumthing as a regular command. To install, clone the repository and then navigate to your checksumthing directory. Run `$ python setup.py install`. To test your install run `$ checksumthing -h`. If you see the checksumthing help menu the install was successful. Time to put down your cocktail!

For more information on running checksumthing please see the [online documentation][1]. 

[1]: https://amiaopensource.github.io/checksumthing/

## Running checksumthing with Sample Data
Our repository includes some sample image files and checksum files to work with located in the (suprise, surprise) `Sample_Files` folder. These sample commands are designed to be run from the checksumthing directory:

```
python checksumthing.py -i Sample_Files/ -ie .md5 -t md5 -c upper -r -pre '#######' -post '*{relativepath}'
```
The above command will attempt to overwrite the data in the existing .md5 files with with "#######" appearing before the checksum and then the relative path to the associated file appearing after the checksum. It will also make the checksum all upper case. The command will work recursively through all the sample folders. It will prompt the user before overwriting any files.

```
python checksumthing.py -i Sample_Files/ -ie .md5 -t md5 -c upper -r -pre '#######' -post '*{relativepath}' -o Sample_Files/checksum_manifest.txt
```
The above command will create a manifest file called "checksum_manifest.txt" with a list of checksums for all the sample files. For each file, it will print "#######" before the checksum (the checksum will be in upper case) and then print the relative path to the file. If a manifest already exists, it will prompt the user to make sure they would like to overwrite the existing manifest.

Currently, the script cannot make csv files through a dedicated method. However, we can make csv files by hacking the current manifest creation method. Let's say you want a csv file where the first column is the filename, the second column is the relative path to the file, and the third column is the hash with lowercase letters. The follow string would create this for you:
```
python checksumthing.py -i Sample_Files/ -ie .md5 -t md5 -c lower -r -pre '{filename},{relativepath},' -ns -o Sample_Files/checksum_manifest.csv
```
Notice, the use of the -ns flag, which removes spaces between the pre, hash, and post portions of the text. Without this flag, there would be a space added to the hash, which could cause problems. 

This script can also be used to mimick the output of other checksum creation tools. The following string mimicks the output of the md5deep tool in recursive mode:
```
python checksumthing.py -i Sample_Files/ -ie .md5 -t md5 -c lower -r -post ' {fullpath}' -o Sample_Files/md5deepstyle.txt
```
