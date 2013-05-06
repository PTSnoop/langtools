#/usr/bin/python
# coding=utf-8

import sys,os,random
from thesaurus import *

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
		continueAnyway = raw_input("Continue anyway? y/n: ")
		if continueAnyway != "y":
			sys.exit(0)
		
	ownThesaurus.add(word,synonyms,comments)
	
elif command == "thesaurus":
	lang = sys.argv[2]
	word = sys.argv[3]
	ownThesaurus = Thesaurus(lang+".txt")
	somewords = ownThesaurus.oneLevelUp(word)
	for someword in somewords:
		print someword
	
elif command == "find":
	lang = sys.argv[2]
	word = sys.argv[3]
	ownThesaurus = Thesaurus(lang+".txt")
	engThesaurus = Thesaurus()
	
	
	foundwords = ownThesaurus.contains(word)
	if foundwords != []:
		for foundword in foundwords:
			foundword.printWord()
			print
		sys.exit(0)
	
	foundwords = ownThesaurus.synonymmed(word)
	if foundwords != []:
		for foundword in foundwords:
			foundword.printWord()
			print
		sys.exit(0)
	
