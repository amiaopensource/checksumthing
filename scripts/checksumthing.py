#!/usr/bin/env python

# Checksumthing.py


import os
from Checksumthing import manifest_formats
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

    for root, dirs, files in os.walk(args.i):
        if not args.recursive:
            #only use files at the root directory
            if root != args.i:
                continue
        for file_ in files:
            if os.path.splitext(file_)[1] != args.ie:
                continue
            
            filepath = os.path.join(root, file_)
            
            # Read the existing hash
            old_hash = hashing.read_hash(filepath, hash_length=hash_length)

            # Create a new hash to replace the exiting
            new_hash = hashing.modify_hash(old_hash, args=args)

            # Overwrite the original file with the new hash
            if args.outputPath:
                manifest_file = manifest_formats.Manifest(manifest_formats.TextManifest())
                manifest_file.add_line(args.outputPath, filepath, new_hash)
            else:
                decorated_hash = hashing.decorate_hash(args.pre, new_hash, args.post)
                hashing.write_hash(decorated_hash, filepath)
if __name__ == '__main__':
    main()
