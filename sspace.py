#!/usr/bin/python
# coding=utf-8

import sys,os,random
from thesaurus import *

def help():
	print '''
Speechspace v0.2. Made by PTSnoop, may or may not be usable for other people.

Usage:
sspace.py add Qituva kebita throw,toss Here are a few comments
  This will add the word "kebita" to the dictionary of the Qituva language, with English synonyms "throw" and "toss".

sspace.py show Qituva kebita
  This will return the definition of the Qituva word "kebita", with any comments.

sspace.py find Qituva hurl
  This will return the Qituva word with the closest definition to the English word "hurl". In this case, it would return the word "kebita" throw, toss.

sspace.py find Qituva hurl 2
  This will return the Qituva word with the next closest definition, skipping the amount given.
	'''

def worseSearchForClosestWord(inword,langThes,spaceThes=0,depth=5,skip=0):
	if spaceThes == 0:
		spaceThes = Thesaurus()
	stack = [inword]
	skipwords = []

	for i in range(depth):
		for stackword in stack:
			if stackword in skipwords:
				continue
			# check if this word exists in the language
			exists = langThes.synonymmed(stackword)
			if exists != []:
				for existingword in exists:
					if existingword in skipwords:
						continue

					if skip == 0:
						return existingword
					else:
						skipwords.append(existingword)
						skip -= 1

		#if we're still here, we've not found it yet.
		stack = spaceThes.expand(stack)
					
	return False

def searchForClosestWord(inword,langThes,spaceThes=0,depth=2,skip=0):
	if spaceThes == 0:
		spaceThes = Thesaurus()
	stack = {}

	stack[inword] = 0
	skipwords = []

	for i in range(depth):
		newstack = {}
		for stackword in stack:
			if stack[stackword] != 0:
				continue
			if stackword in skipwords:
				continue
			# check if this word exists in the language
			exists = langThes.synonymmed(stackword)
			if exists != []:
				for existingword in exists:
					if existingword in skipwords:
						continue

					if skip == 0:
						return existingword
					else:
						skipwords.append(existingword)
						skip -= 1
			#if we're still here, we've not found it yet.
			synonyms = spaceThes.synonymmed(stackword)
			for synonym in synonyms:
				if synonym in stack:
					continue
				newstack[synonym.wordname] = 0
			stack[stackword] = 1
		for newstackword in newstack:
			stack[newstackword] = newstack[newstackword]
					
	return False
		
#import cProfile
#cProfile.run("oldSearchForClosestWord(\"spade\",Thesaurus(\"cthiote.txt\"),Thesaurus(),3,0)", "searchForClosestWord.profile")
#import pstats
#stats = pstats.Stats("searchForClosestWord.profile")
#stats.strip_dirs().sort_stats('time').print_stats()
#sys.exit(0)

if len(sys.argv) <= 1:
	help()
	sys.exit(0)

command = sys.argv[1]

# sspace add cthiote dhechøn throw,toss
if command == "add":
	lang = sys.argv[2]
	word = sys.argv[3]
	synonyms = sys.argv[4]
	synonyms = synonyms.split(",")
	notes = sys.argv[5:]
	comments = ""
	for note in notes:
		comments += note + " "
	ownThesaurus = Thesaurus(lang+".txt")
	
	foundwords = ownThesaurus.contains(word)
	if foundwords != []:
		print "Word already found."
		for foundword in foundwords:
			foundword.printWord()
		replace = raw_input("Replace it? y/n: ")
		if replace == "y":
			ownThesaurus.remove(word)
			ownThesaurus.add(word,synonyms,comments)
		else:
			continueAnyway = raw_input("Continue anyway? y/n: ")
			if continueAnyway != "y":
				sys.exit(0)
		
	ownThesaurus.add(word,synonyms,comments)
	
# sspace find cthiote throw 
elif command == "find":
	lang = sys.argv[2]
	word = sys.argv[3]

	if len(sys.argv) >= 5:
		skip = int(sys.argv[4])
	else:
		skip = 0
	ownThesaurus = Thesaurus(lang+".txt")
	engThesaurus = Thesaurus()
	
	foundword = searchForClosestWord(word,ownThesaurus,engThesaurus,2,skip)
	if foundword:
		foundword.printWord()
	else:
		print "Nothing found."
	sys.exit(0)
	
elif command == "show":
	lang = sys.argv[2]
	word = sys.argv[3]
	ownThesaurus = Thesaurus(lang+".txt")
	foundwords = ownThesaurus.contains(word)
	for word in foundwords:
		word.printWord()

else:
	help()

