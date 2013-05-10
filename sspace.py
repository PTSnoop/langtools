#!/usr/bin/python
# coding=utf-8

import sys,os,random
from langthesaurus import *

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

sspace.py wordlist Qituva Swadesh.txt
  This will let you work through the given word list, randomly generating suggestions.
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

def add(lang,word,synonyms,comments):
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
	add(lang,word,synonyms,comments)
	
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
	
# sspace show cthiote throw 
elif command == "show":
	lang = sys.argv[2]
	word = sys.argv[3]
	ownThesaurus = Thesaurus(lang+".txt")
	foundwords = ownThesaurus.contains(word)
	if foundwords != []:
		for foundword in foundwords:
			foundword.printWord()
			print
		sys.exit(0)
	
	for word in foundwords:
		word.printWord()

# sspace wordlist cthiote swadesh.txt
elif command == "wordlist":
	lang = sys.argv[2]
	listfilename = sys.argv[3]
	import phongen
	import random

	listfile = open(listfilename,"r")
	wordlist = listfile.readlines()
	listfile.close()
	#random.shuffle(wordlist)

	engThesaurus = Thesaurus()


	for listword in wordlist:
		ownThesaurus = Thesaurus(lang+".txt")
		print
		foundword = searchForClosestWord(listword,ownThesaurus,engThesaurus,2)
		print "New word: "+listword
		if foundword:
			print "Closest match:"
			foundword.printWord()
		else:
			print "No similar words found."
		while True:
			decide = raw_input("Add a new word? y/n/(s)earch: ")
			if decide == "s":
				searchword = raw_input("Search for: ")
				foundword = searchForClosestWord(searchword,ownThesaurus,engThesaurus,2)
				if foundword:
					print "Closest match:"
					foundword.printWord()
				else:
					print "No similar words found."
			else:
				break
		
		if decide != "y":
			continue

		while True:
			suggestion = phongen.NewWord()
			print "Suggested word: "+suggestion
			decide = raw_input("(u)se, (g)enerate new, (c)hange: ")
			if decide == "u":
				chosenword = suggestion
				break
			elif decide == "c":
				chosenword = raw_input("New word: ")
				break

		synonyms = raw_input("Synonyms:" )
		synonyms = synonyms.split(",")
		notes = raw_input("Notes:" )
		add(lang,chosenword,synonyms,notes)
		print "Word added."

else:
	help()

