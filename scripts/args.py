import argparse


def get_args():
    """
    Get the arguments for the script.
    :return: Parsed arguments
    """
    parser = argparse.ArgumentParser(description="The Ultimate Checksum Script!")

    parser.add_argument('-i', '--inputDirectory', dest='i', help='The Directory To Process')

    parser.add_argument('-t', '--typeOfHash', dest='t', default='md5', help='Select the checksum type to process')

    parser.add_argument('-ie', '--inputExtension', dest='ie', default='.md5',
                        help='Select the extension of the input files')

    parser.add_argument('-c', '--caseOutput', dest='c', default='lower',
                        help='Define the case of the output hash letters. use lower or upper, defaults to lower')

    parser.add_argument('-b', '--before', dest='b', default='',
                        help='Any text entered here will appear before the hash in the sidecar file')

    parser.add_argument('-a', '--after', dest='a', default='',
                        help='Any text entered here will appear after the hash in the sidecar file')

    parser.add_argument('-ns', '--noSpace', action='store_true',
                        help='if true, the script will not add padding spaces to the before and after strings')

    return parser.parse_args()