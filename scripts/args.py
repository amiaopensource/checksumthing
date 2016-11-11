import argparse


def get_args():
    """
    Get the arguments for the script.
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser(description="The Ultimate Checksum Script!")

    parser.add_argument('-i', '--inputDirectory', dest='i', help='The directory to process')
    
    parser.add_argument('-o', '--outputPath', help='The path to the output manifest file')
    
    parser.add_argument('-m', '--manifestType', help='The the type of manifest file you want to create')

    parser.add_argument('-t', '--typeOfHash', dest='t', default='md5', help='Select the checksum type to process')
    
    parser.add_argument('-ie', '--inputExtension', dest='ie', default=".md5",
                        help='Select the extension of the input files')

    parser.add_argument('-c', '--caseOutput', dest='c', default='lower',
                        help='Define the case of the output hash letters. Use lower or upper, default is lower')

    parser.add_argument('-pre', '--preHashText', dest='pre', default='',
                        help='Any text entered here will appear before the hash in the sidecar file')

    parser.add_argument('-post', '--postHashText', dest='post', default='',
                        help='Any text entered here will appear after the hash in the sidecar file')

    parser.add_argument('-ns', '--noSpace', action='store_true',
                        help='If included, the script will not add padding spaces to the before and after strings')
                        
    parser.add_argument('-r', '--recursive', action='store_true',
                        help='If included, the script will process all checksum files recursively through the input directory')
    
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='If included, the script will not output every step to the command line')
                        
    parser.add_argument('-f', '--force', action='store_true',
                        help='If included, the script will not ask before overwriting any files')

    
    return parser.parse_args()
