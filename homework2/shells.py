#!/usr/bin/python

# ECE 2524 Homework 2 Problem 1 Tyler Adams
with open('/etc/passwd', 'r') as f:
    #read_data = f.read() #read the whole file at once
    # or read it line by line
    for line in f:
	t = line.split(':')
        print t[0] + '\t' + t[6].rstrip('\n')

