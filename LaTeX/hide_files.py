#!/usr/bin/python
"""Script to hide certain file types. It does this by adding all files with certain extensions to the .hidden file."""

import os

def hide(f):
	"""Should this file be hidden?"""
	for ext in EXTENSIONS:
		if f[-len(ext):] == ext:
			return True
	return False

EXTENSIONS = [".aux", ".log", ".out", ".synctex.gz"]	# which extensions should be hidden?
hidden_files = list()									# empty list to hold 

# loop files in current directory
for f in os.listdir("."):
	if hide(f):
		hidden_files.append(f)

# add list to .hidden
with open(".hidden", 'w') as f:
	f.write('\n'.join(hidden_files))