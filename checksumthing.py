#!/usr/bin/env python

#checksumthing.py


import argparse
import subprocess
import os
import sys
import glob

def main():
	parser = argparse.ArgumentParser(description="The Ultimate Checksum Script!")
	parser.add_argument('-i','--inputDirectory',dest='i',help='The Directory To Process')
	parser.add_argument('-t','--typeOfHash',dest='t',default='md5',help='Select the checksum type to process')
	parser.add_argument('-ie','--inputExtension',dest='ie',default='.md5',help='Select the extension of the input files')
	args = parser.parse_args()
	
	print "Starting analysis on " + args.t + " type checksums in " + os.path.basename(args.i)
	
	print args.ie
	os.chdir(args.i)
	for filename in glob.glob('*' + args.ie, recursive=True):
	    print filename


#        with open(filename, 'r') as f:
            #text = f.read()
            #checkSum = text.split('*')[0].strip()
            #wavFile = text.split('*')[1].replace("\n", "")

            #checkSum_dict[str(wavFile)] = {}
            #checkSum_dict[str(wavFile)]['md5'] = checkSum
            #checkSum_dict[str(wavFile)]['md5_datetime'] = timestr
            #checkSum_dict[str(wavFile)]['filename'] = wavFile
	
main()