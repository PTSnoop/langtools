#!/usr/bin/python
# coding=utf-8

import sys
sys.path.append(os.getcwd())
import soundchange
from langthesaurus import *
import random

splitters = [" ","-","\n",",","*","!","?"]

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

def crass(thesaurus,iworkingset,inset,outset,level):
	if level <= 0:
		thisword = ""
		for word in iworkingset:
			thisword += word.wordname
		for w in range(len(inset)):
			if inset[w] == thisword:
				outset[w].append(list(iworkingset))
		return outset
	else:
		for word in thesaurus.words:
			workingset = list(iworkingset)
			workingset.append(word)
			outset = crass(thesaurus,workingset,inset,outset,level-1)
	return outset
			

def parse(lang,intext):

	intext = intext.replace("í","i")
	intext = intext.replace("é","e")
	intext = intext.replace("á","a")
	intext = intext.replace("ó","o")
	intext = intext.replace("ú","u")
	intext = intext.replace("ǿ","ø")
	intext = intext.replace("ʉ́","ʉ")

	thesaurus = Thesaurus(lang+".txt")
	random.shuffle(thesaurus.words)

	text,splits = splat(intext)
	parsed = []
	for t in text:
		parsed.append([])

	for l in range(5):
		parsed = crass(thesaurus,[],text,parsed,l)
		print printness(parsed,splits)
		carryon = False
		for r in parsed:
			if len(r) == 0:
				carryon = True
		if not carryon:
			break

	return printness(parsed,splits)

def printness(parsed,splits):
	outstring = ""	
	splitnum = 0
	for thing in range(len(parsed)):
		if len(parsed[thing]) == 0:
			outstring += "XXX-"
		for t in parsed[thing]:
			for option in t:
				outstring += option.synonyms[0]
				outstring += "-"
			outstring = outstring[:-1]
			outstring += "/"
		outstring = outstring[:-1]
		outstring += splits[thing]

	return outstring

if __name__ == "__main__":
	#parse.py Qituva input.txt output.txt
	lang = sys.argv[1]
	thefile = sys.argv[2]
	outfile = False
	if len(sys.argv) > 3:
		outfile = sys.argv[3]

	indata = open(thefile,"r").read()
	parsed = parse(lang,indata)
	if outfile:
		open(outfile,"a+").write(parsed+"\n")
	else:
		print parsed

