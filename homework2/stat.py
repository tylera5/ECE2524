#!/usr/bin/python

# ECE 2524 Homework 2 Problem 3 Tyler Adams
s = 'ACCOUNT SUMMARY'
print s
d = 0
c = 0
maximum = 0
minimum = 2000
with open("account.txt", 'r') as f:
    #read_data = f.read() #read the whole file at once
    # or read it line by line
	
    for line in f:
	t = line.split()
	my_number_string = t[2]
	num = float(my_number_string)
	d = d + num
	c = c + 1	
	if num > maximum:
		maximum = num
		name = t[1]
	if num < minimum:
		minimum = num
		name2 = t[1]


print "Total Amount Owed = " + str(d)
print "Average Amount Owed = " + str(d/c)
print "Maximum Amount Owed = " + str(maximum) + " by " + str(name)
print "Minimum Amount Owed = " + str(minimum) + " by " + str(name2)
