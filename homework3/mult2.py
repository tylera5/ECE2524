#!/usr/bin/env python2
# ECE 2524 Homework 3 Problem 2 Tyler Adams 

import sys
import argparse
import fileinput

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--ignore-blank', action='store_true', dest='blank', default = False)
parser.add_argument('--file', action='store', dest='infile', default = 0, nargs ='+')
parser.add_argument('--ignore-non-numeric', action='store_true', dest='white', default = False)
args = parser.parse_args()

product = 1.0 
with open('argv.infile', 'r') as f:
	for line in fileinput.input():
    		if len(line) == 0:
    			break # EOF
    		elif line == '\n':
			if argv.blank:
				continue
			else:
				print product
    				product = 1
    		else:
	 		try:
    	     			product *= float(line)
	 		except Exception as err:
				if argv.white:
					continue
				else:
    	     				sys.stderr.write(str(err))
    	     				sys.exit(1)

print product
print argv.infile
sys.exit(0)  

