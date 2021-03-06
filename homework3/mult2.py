#!/usr/bin/env python2
# ECE 2524 Homework 3 Problem 2 Tyler Adams 

import sys
import argparse
import fileinput

#added three arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--ignore-blank', action='store_true', dest='blank', default = False)
parser.add_argument('file', nargs='*', type=str, default=sys.stdin)
parser.add_argument('--ignore-non-numeric', action='store_true', dest='white', default = False)
args = parser.parse_args()

#initialization
product = 1.0 

for line in fileinput.input(args.file):
    	if len(line) == 0:
    		break # EOF
    	elif line == '\n':	#check to see if there is a blank 					#line and if the user specified 				#the correct argument the 					#whitespace operation is nullified
		if args.blank:
			continue
		else:
			print product
    			product = 1
    	else:			#sums the product and ignores 					#strings that aren't numbers if 				#the argument is true, else it 					#displays an error
	 	try:
    	     		product *= float(line)
	 	except Exception as err:
			if args.white:
				continue
			else:
    	     			sys.stderr.write(str(err))
    	     			sys.exit(1)


print product
sys.exit(0)  


