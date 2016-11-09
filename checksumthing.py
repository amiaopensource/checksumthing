#!/usr/bin/env python

#checksumthing.py


import argparse
import subprocess
import os
import sys
import glob
import re

def main():
	parser = argparse.ArgumentParser(description="The Ultimate Checksum Script!")
	parser.add_argument('-i','--inputDirectory',dest='i',help='The Directory To Process')
	parser.add_argument('-t','--typeOfHash',dest='t',default='md5',help='Select the checksum type to process')
	parser.add_argument('-ie','--inputExtension',dest='ie',default='.md5',help='Select the extension of the input files')
	parser.add_argument('-c','--caseOutput',dest='c',default='lower',help='Define the case of the output hash letters. use lower or upper, defaults to lower')
	parser.add_argument('-b','--before',dest='b',default='',help='Any text entered here will appear before the hash in the sidecar file')
	parser.add_argument('-a','--after',dest='a',default='',help='Any text entered here will appear after the hash in the sidecar file')
	parser.add_argument('-ns','--noSpace',dest='ns',default=False,help='if true, the script will not add padding spaces to the before and after strings')
	
	args = parser.parse_args()
	
	print "Starting analysis on " + args.t + " type checksums in " + os.path.basename(args.i)
	
	if args.t == 'md5':
	    hashLength = 32
	elif args.t == 'sha1':
	    hashLength = 40
	elif args.t == 'sha256':
	    hashLength = 64
	
	
	
	os.chdir(args.i)
	for filename in glob.glob('*' + args.ie):
	    with open(filename, 'r+') as f:
	        text = f.read()
	        m = re.search('([0-9a-f]{' + str(hashLength) + '})',text, flags=re.IGNORECASE)
	        hashValue = m.group()
	        if args.c == 'lower':
	            hashValue = hashValue.lower()
	        elif args.c == 'upper':
	            hashValue = hashValue.upper()
            if args.ns:
                hashValue = args.b + hashValue + args.a
            else:
                hashValue = args.b + ' ' + hashValue + ' ' + args.a

            f.seek(0)
            f.write(hashValue)
            f.truncate()

	
main()