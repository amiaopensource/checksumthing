#!/usr/bin/env python

# Checksumthing.py


import os
from Checksumthing import manifest_formats
from Checksumthing import hashing
from scripts.args import get_args
import sys


def main():

    # Read in the user arguments
    args = get_args()
    args.i = os.path.abspath(args.i)
    print("Starting analysis on " + args.t + " type checksums in " + os.path.basename(args.i))

    # Calculate the length of the hash value for the given type.
    try:
        hash_length = hashing.get_hash_length(args.t)
    except KeyError as e:
        # If an invalid key is given, exit.
        print("Invalid hash type.")
        exit()

    # If output path specified, initialize manifest file
    if os.path.exists(args.outputPath):
        if sys.version_info[0] < 3:
            user_entry = raw_input("The specified output file already exists, do you want to overwrite? (y/n): ")
            if user_entry == "y":
                print("Manifest Overwritten! Have a nice day B^)")
                with open(args.outputPath, "w") as f:
                    f.write("")
            else:
                print("Quitting Script!")
                return
        else:
            user_entry = input("The specified output file already exists, do you want to overwrite? (y/n): ")
            if user_entry == "y":
                print("Manifest Overwritten! Have a nice day B^)")
                with open(args.outputPath, "w") as f:
                    f.write("")
            else:
                print("Quitting Script!")
                return
    else:
        with open(args.outputPath, "w") as f:
            f.write("")
        

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
            pre_hash_text = hashing.create_decoration(args.pre, filepath, args)
            post_hash_text = hashing.create_decoration(args.post, filepath, args)
            decorated_hash = hashing.decorate_hash(pre_hash_text, new_hash, post_hash_text, args.noSpace)
            
            if args.outputPath:
                manifest_file = manifest_formats.Manifest(manifest_formats.TextManifest())
                manifest_file.add_line(args.outputPath, filepath, decorated_hash)
            else:
                hashing.write_hash(decorated_hash, filepath)
            
            #if not quiet
            if not args.quiet:
                print("Finished Prossessing " + filepath)
            
if __name__ == '__main__':
    main()
