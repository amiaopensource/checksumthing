About
-----

Created as a part of the 2016 AMIA Hack day hackathon.

The ultimate checksum script! Checksumthing helps you create different kinds of checksum sidecar files.



What is checksumthing?
----------------------

checksumthing helps you transform your checksum files in the format that you want. Different pieces of software used to
produce checksums create sidecar files (typically files ending in .md5 or .sha1) with very different formatting, which
creates headaches for archivists—we love standards and loathe disorder. checksumthing is a Python script that can solve
this problem by allowing users to transform the data inside sidecar files into a standardized format most convenient
for them. For example, you can:

Append text before or after the checksum value (like the path to the file or the filename)
Change the checksum text to all caps or all lowercase
Search for checksum files and transform files through a nested directory structure
checksumthing currently supports MD5, SHA1, and SHA256 checksums. Right now the script only supports plaintext sidecar
files. In the future, we hope to support CSV and other types of files.