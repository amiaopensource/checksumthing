#!/usr/bin/env python

# Checksumthing.py


import argparse
import glob
import os

from Checksumthing import hashing

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

    parser.add_argument('-ns', '--noSpace', dest='ns', default=False,
                        help='if true, the script will not add padding spaces to the before and after strings')

    return parser.parse_args()


def main():

    # Read in the user arguments
    args = get_args()

    print("Starting analysis on " + args.t + " type checksums in " + os.path.basename(args.i))

    # Calculate the length of the hash value for the given type.
    try:
        hash_length = hashing.get_hash_length(args.t)
    except KeyError as e:
        # If an invalid key is given, exit.
        print("Invalid hash type.")
        exit()

    # Cycle through the given files of the inputExtension at the inputDirectory
    os.chdir(args.i)
    files = glob.glob('*' + args.ie)

    for filename in files:

        # Read the existing hash
        old_hash = hashing.read_hash(filename, hash_length=hash_length)

        # Create a new hash to replace the exiting
        new_hash = hashing.modify_hash(old_hash, args=args)

        # Overwrite the original file with the new has
        hashing.write_hash(new_hash, filename)

if __name__ == '__main__':
    main()
