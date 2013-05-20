#!/usr/bin/python
# coding=utf-8

import sys
from langthesaurus import *
import random

def curse(thesaurus,word,iwordlist,level):
	if word == "":
		return [""]
		
	if level < 0:
		baseword = ""
		for listword in iwordlist:
			baseword += listword.wordname
		if baseword == word:
			return iwordlist
		else:
			return False

	else:
		level -= 1
		for listword in thesaurus.words:
			wordlist = list(iwordlist)
			wordlist.append(listword)
			#if level > 0:
			#	deb = ""
			#	for w in wordlist:
			#		deb += w.wordname
			#	print word
			#	print deb
			check = curse(thesaurus,word,wordlist,level)
			if check:
				return check
	return False


def check(thesaurus,word,level):
	wordlist = []
	return curse(thesaurus,word,wordlist,level)
	
splitters = [" ","-","\n",".",",","*","!","?"]

def splat(text):
	currword = ""
	outtext = []
	outsplits = []
	for char in text:
		if char in splitters:
			outtext.append(currword)
			outsplits.append(char)
			currword = ""
		else:
			currword += char
	outtext.append(currword)
	outsplits.append(" ")
	outsplits.append(" ")
	return outtext,outsplits
	

def parse(lang,intext):
	thesaurus = Thesaurus(lang+".txt")
	random.shuffle(thesaurus.words)

	text,splits = splat(intext)
	parsed = []
	for word in text:
		for l in range(4):
			print word,l
			found = check(thesaurus,word,l)
			if found:
				break
		parsed.append(found)

	outtext = ""
	for par in range(len(parsed)):
		if parsed[par]:
			for mark in parsed[par]:
				if type(mark) == str:
					outtext += mark
				else:
					outtext += mark.synonyms[0]
				outtext += "-"
			outtext = outtext[:-1]
			outtext += splits[par][0]
		else:
			outtext += "XXX"
			outtext += splits[par][0]

	return outtext

if __name__ == "__main__":
	# parse.py Qituva input.txt
	#lang = sys.argv[1]
	#thefile = sys.argv[2]

	print parse("necthioth","unai ttsattanon, phethiaph nausnophan, kkathaphnophan, kkʉttnophan khauflakk, niʉ sloløsnophan, niʉppnʉf ia iauc.")
	#print parse("necthioth","unai ttsattanon")
