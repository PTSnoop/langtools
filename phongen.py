#!/usr/bin/python
# coding=utf-8

import random
import sys

C = [
	'p',	't',	'k',	
	'ph',	'th',	'kh',	
	'f',	's','z','c',
	'm',	'n',	'ng',
	'u',	'i','l','r',
]
C1 = [ 's','th','ph','n','c','n','l','kh','t','p','ng','m','r','f','i','u','k','z']
C2 = [ 'n','s','c','th','l','ph','kh','z','ng','m','f','k','p','t','r']

I = ['i','l','n','s']

V = [
	'i','ʉ',      'u',
	 'e','ø',  'o',
	     'a',
]
V1 = ['i','a','e','o','ia','ø','ai','u','ua','au','ʉ']
iV = ['a','e','o','ø','u','ʉ','au','ai']

def DistPick(A):
	size = len(A)+1
	B = []
	for thing in range(len(A)):
		B.append( 100-(1-((1/size)*thing) ))

	picknum = random.randint(0,sum(B))

	for thing in range(len(B)):
		if picknum < B[thing]:
			return A[thing]
		else:
			picknum -= B[thing]
	return A[0]

def NewWord():
	word = ""
	word += DistPick(C1)
	if random.random() < 0.3:
		word += DistPick(I)
		word += DistPick(iV)
	else:
		word += DistPick(V1)
	if random.random() < 0.6:
		word += DistPick(C2)
	if random.random() < 0.4:
		word += NewWord()
	return word

if __name__ == "__main__":

	word = ""
	if len(sys.argv) > 1:
		noOfWords = int(sys.argv[1])
	else:
		noOfWords = 1

	while True:
		word += NewWord()
		word += " "
		noOfWords -= 1
		if noOfWords <= 0:
			break
	print word
