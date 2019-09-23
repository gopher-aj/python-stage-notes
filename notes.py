#!/bin/bash

import argparse
import sys

def err_exit(msg):
	sys.stderr.write(msg + '\n')
	sys.exit()

def read_notes():
	
	body = input('enter the your notes, (Use # to quit and save from notes)\n')

def main():

	parser = argparse.ArgumentParser(description='Tool for adding insta notes')
	parser.add_argument('-t',
						'--title',
						action='store',
						required='True',
						help='set title to note.')

	args = parser.parse_args()

	if args.title:
		NOTE_TITLE = args.title
		read_notes()
		
if __name__ == '__main__':
	main()
