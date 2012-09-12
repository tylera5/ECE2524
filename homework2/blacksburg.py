#!/usr/bin/python

# ECE 2524 Homework 2 Problem 2 Tyler Adams
s = 'ACCOUNT INFORMATION FOR BLACKSBURG RESIDENTS'
print s

str = ", "

with open("account.txt", 'r') as f:
    #read_data = f.read() #read the whole file at once
    # or read it line by line
    for line in f:
	t = line.split()
	if t[3] == "Blacksburg":
		seq = (t[4], t[1], t[0], t[2]);
		print str.join(seq)
