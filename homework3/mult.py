#!/usr/bin/env python2
# ECE 2524 Homework 3 Problem 1 Tyler Adams

import sys
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
args = parser.parse_args()
#initialize variables
product = 1.0

while True:
   	   data = sys.stdin.readline() #reads in lines from 					       #standard input
           if len(data) ==0:
           	break # EOF
           elif data == '\n': #checks for an empty line and 				      #prints product if it is blank
		print product
  	   else:
		try:
    			product *= float(data)#multiples data
		except Exception as err: #deals with error 						 #handling
    			sys.stderr.write(str(err))
    			sys.exit(1)

print product
sys.exit(0)   	
