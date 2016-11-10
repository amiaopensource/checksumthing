Running the Command Line Script
-------------------------------

To move all the files in a directory into a Medusa package follow these steps.

1) Open a command prompt/terminal.
2) Type "checksumthing" followed by the path to the directory and a path to save the new packaged content.

You are done.

For example... ::

        checksumthing

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

