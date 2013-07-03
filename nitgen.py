#!/usr/bin/python
# coding=utf-8

import random
import sys

'''
p t_d t_- k q
  D   Z   C
   l  j
m     n

i I  U u
 e @ o
  a Q

p t c k q
  d z h
  l j
m   n

i y w u
 e ə o
  a å

CV(D,Z,C)
'''

C = [
	'p','t','c','k','q',
  	    'd','z','h',
            'cz',
  	    'l','j',
	'm','n',
]
C1 = ['t','m','d','q','k','h','p','tn','n','c','cz','l','pn','z','j']
C2 = [ 'h','z','d' ]

V = [
	'i','y','w','u',
 	  'e','ə','o',
  	    'a','å',
]

V1 = ['a','i','e','å','ə','u','o','y','w']
R = ['r']

def DistPick(A):
	size = len(A)+1
	B = []
	for thing in range(len(A)):
		B.append( int(100*(1-((1.0/size)*thing) )))

	picknum = random.randint(0,sum(B))

	for thing in range(len(B)):
		if picknum < B[thing]:
			return A[thing]
		else:
			picknum -= B[thing]
	return A[0]

def NewWord(pitched=False):
	word = ""
	letter = DistPick(C1)
	word += letter
	if random.random() < 0.1:
		#word += letter
		word += DistPick(R)
	letter = DistPick(V1)
	word += letter
	if random.random() < 0.1:
		#word += letter
		word += DistPick(R)
	if random.random() < 0.15:
		word += DistPick(C2)
	if random.random() < 0.5:
		word += NewWord(pitched)
	return word

if __name__ == "__main__":

	word = ""
	paragraph = False
	capital = False

	if len(sys.argv) > 1:
		if sys.argv[1] == "lipsum":
			paragraph = True
			noOfWords = random.randint(600,1000)
			capital = True
		else:
			noOfWords = int(sys.argv[1])
	else:
		noOfWords = 1

	while True:
		nw = NewWord()
		if capital:
			nw = nw.capitalize()
			capital = False
		word += nw
		if paragraph and random.random() < 0.15:
			word += "."
			capital = True
			if random.random() < 0.3:
				word += "\n\n"
		elif paragraph and random.random() < 0.15:
			word += ","
		if noOfWords <= 1:
			break
		word += " "
		noOfWords -= 1
	if paragraph:
		word += "."
	print word
