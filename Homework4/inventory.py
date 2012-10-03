#!/usr/bin/env python2
# ECE 2524 Homework (Tyler Adams)

import sys
import argparse
import fileinput
import shlex

def i_add(arg):
	with open(args.data, "a") as myfile:
		output = arg[0] + '\t' + arg[1] + '\t' + arg[2] + '\t' + arg[3] + '\n'
		print "SUCCESSFULLY ADDED NEW ENTRY:"
    		myfile.write(output)

def i_remove(arg):
	string = arg[0].split('=')
	content = open(args.data, 'r').read()
	contentList = content.split('\n')
	print "SUCCESSFULLY DELETED ENTRY:"
	for index, each in enumerate(contentList):
		if string[1] in each:
			contentList.pop(index)
	newContent = '\n'.join(contentList)
	open(args.data, 'w').write(newContent)
    	
def i_set(arg):
	string = arg[2].split('=')
	string2 = arg[0].split('=')
	content = open(args.data, 'r').read()
	contentList = content.split('\n')
		
def i_list(arg):
	with open(args.data, "r") as myfile:
		if (arg[0] == 'all' and len(arg) < 3):
			print "SUCCESSFULLY LISTED ALL ENTRIES:"
			for line in myfile:
				print line.strip()
		elif (arg[0] == 'all' and arg[1] == 'with'):
			string = arg[2].split('=')
			print "SUCCESSFULLY LISTED ALL ENTRIES:"
			for line in myfile:
       				if string[1] in line:
					print line.strip()
def i_exit(arg):
	sys.exit(0);

parser = argparse.ArgumentParser(description='Manipulate and display inventory from supplied datafile.')
parser.add_argument('-f', '--data-file', action='store', dest='data', help='enter the name of the data file')
args = parser.parse_args()



while True:
	try:
		Line = sys.stdin.readline()
		arg = shlex.split(Line)
		input_command = arg[0]
		arg.pop(0)
	except KeyboardInterrupt:
		sys.exit(0)
	if not Line:
		continue
	command = {'add': i_add, 'remove': i_remove, 'subtract': i_remove, 'set': i_set,
			  'update': i_set, 'list': i_list,  'view': i_list, 'display': i_list, 
			  'exit': i_exit, 'quit': i_exit}
	try:
		command[input_command](arg)
	except KeyError as e:
		sys.stderr.write("Invalid command: {}\n".format(input_command))
