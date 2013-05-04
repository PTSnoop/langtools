#!/usr/bin/python
# coding=utf-8

import random
import sys

C = [
	'pp',	'tt',	'kk',	
	'ph',	'th',	'kh',	
	#'b',	'd',	'g',	
	'f'	's',	'c',
	'm',	'n',	'ng',
		'i','l','r',
]
V = [
	'i','ʉ',      'u',
	 'e','ø',  'o',
	     'a',
]
D = ['au','ai','ia','ua']

word = ""
if len(sys.argv) > 1:
	noOfWords = int(sys.argv[1])
else:
	noOfWords = 1
while True:
	word += random.choice(C)
	if random.random() < 0.3:
		word += "i"
	if random.random() < 0.7:
		word += random.choice(V)
	else:
		word += random.choice(D)
	if random.random() < 0.7:
		if random.random() < 0.5:
			word += random.choice(C)
		word += " "
		noOfWords -= 1
		if noOfWords <= 0:
			break
print word
