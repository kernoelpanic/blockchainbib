#!/usr/bin/env python3

import sys

def run(filename):

	assert(filename.endswith('.bib'))

	with open(filename) as f:
		lines_orig = [l.rstrip() for l in f]

	lines = []
	for line in lines_orig:
		if '\\url' in line or ('howpublished' in line and 'http' in line):
			if not line[-1].endswith(','):
				# remove ',' character from previous line
				lines[-1] = lines[-1][:-1]
		else:
			lines.append(line)

	with open(filename[:-4] + '-urlremoved.bib', 'w') as f:
		for line in lines:
			f.write(line)
			f.write('\n')

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('Usage: ./remove-urls.py somebibfile.bib\n')
	else:
		run(sys.argv[1])