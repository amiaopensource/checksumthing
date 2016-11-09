#!/usr/bin/env python

# Checksumthing.py


import glob
import os

from Checksumthing import hashing
from scripts.args import get_args


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
