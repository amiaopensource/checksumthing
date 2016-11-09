#!/usr/bin/env python

#checksumthing.py


import argparse
import subprocess
import os
import sys

def main():
	parser = argparse.ArgumentParser(description="The Ultimate Checksum Script!")
	parser.add_argument('-i','--input',dest='i',help='The Directory To Process')
	parser.add_argument('-t','--typeOfHash',dest='t',default='md5',help='Select the checksum type to process')
	args = parser.parse_args()
	
	print "Starting analysis on " + args.t + " type checksums in " + os.path.basename(args.i)
	
	
main()