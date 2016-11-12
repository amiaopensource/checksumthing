Running the Command Line Script
-------------------------------

Running checksumthing with Sample Data

Our repository includes some sample image files and checksum files to work with located in the (suprise, surprise)
Sample_Files folder. These sample commands are designed to be run after you install checksumthing::

    checksumthing -i Sample_Files/ -ie .md5 -t md5 -c upper -r -pre '#######' -post '*{relativepath}'

The above command will attempt to overwrite the data in the existing .md5 files with with "#######" appearing before
the checksum and then the relative path to the associated file appearing after the checksum. It will also make the
checksum all upper case. The command will work recursively through all the sample folders. It will prompt the user
before overwriting any files.::

    checksumthing -i Sample_Files/ -ie .md5 -t md5 -c upper -r -pre '#######' -post '*{relativepath}' -o Sample_Files/checksum_manifest.txt

The above command will create a manifest file called "checksum_manifest.txt" with a list of checksums for all the
sample files. For each file, it will print "#######" before the checksum (the checksum will be in upper case) and then
print the relative path to the file. If a manifest already exists, it will prompt the user to make sure they would
like to overwrite the existing manifest.

Currently, the script cannot make csv files through a dedicated method. However, we can make csv files by hacking the
current manifest creation method. Let's say you want a csv file where the first column is the filename, the second
column is the relative path to the file, and the third column is the hash with lowercase letters. The follow string
would create this for you::

    checksumthing -i Sample_Files/ -ie .md5 -t md5 -c lower -r -pre '{filename},{relativepath},' -ns -o Sample_Files/checksum_manifest.csv

Notice, the use of the -ns flag, which removes spaces between the pre, hash, and post portions of the text. Without
this flag, there would be a space added to the hash, which could cause problems.

This script can also be used to mimick the output of other checksum creation tools. The following string mimicks the
output of the md5deep tool in recursive mode::

    checksumthing -i Sample_Files/ -ie .md5 -t md5 -c lower -r -post ' {fullpath}' -o Sample_Files/md5deepstyle.txt

If for some reason you are not able to run any of the commands here, you can still run the script by navigating to
the "checksumthing" directory, and run python checksumthing.py along with any arguments that you need.


The usage of each flag is described in the help. There are however, three strings that mean something special to
checksumthing. They can be entered using the -pre or -post flags, but they must have the curly brackets in order to be
properly substituted.

{filename} will be replaced by the filename of the file associated with the sidecar checksum file.

{fullpath} will be replaced by the full path of the file associated with the sidecar checksum file.

{relativepath} can only be used when creating a text manifest (using the -o flag). This string will be replaced by
the relative path of the file associated with the sidecar checksum file in relation to the manifest file.

It's that simple!

.. NOTE:: While this documentation should be up to date, if there is any question about how to use the current version
          \ installed, you can always type "checksumthing -h" into a command prompt. This will provide the usage and all
          \ the options for the currently install version of the script. ::


            $ checksumthing -h

            usage: checksumthing.py [-h] [-i I] [-o OUTPUTPATH] [-m MANIFESTTYPE] [-t T]
                                    [-ie IE] [-c C] [-b B] [-a A] [-ns] [-r]

            The Ultimate Checksum Script!

            optional arguments:
              -h, --help            show this help message and exit
              -i I, --inputDirectory I
                                    The Directory To Process
              -o OUTPUTPATH, --outputPath OUTPUTPATH
                                    The path to the output manifest file
              -m MANIFESTTYPE, --manifestType MANIFESTTYPE
                                    The the type of manifest file you want to create
              -t T, --typeOfHash T  Select the checksum type to process
              -ie IE, --inputExtension IE
                                    Select the extension of the input files
              -c C, --caseOutput C  Define the case of the output hash letters. use lower
                                    or upper, defaults to lower
              -b B, --before B      Any text entered here will appear before the hash in
                                    the sidecar file
              -a A, --after A       Any text entered here will appear after the hash in
                                    the sidecar file
              -ns, --noSpace        if included, the script will not add padding spaces to
                                    the before and after strings
              -r, --recursive       if true, the script will process all checksum files
                                    recursively through the input directory

