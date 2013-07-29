#!/usr/bin/python


import sys,random,re
import sspace
from convert import *
from soundchange import *
from langthesaurus import *

if len(sys.argv) == 1 or sys.argv[1] == "help":
	print """Usage: 
	autogloss.py Qituva this be-PRES DEF gloss-text-SING.
or:
	autogloss.py Qituva in.txt out.txt
	"""
	sys.exit(0)

splitters = [" ","-","\n",",","*","!","?"]

def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def autogloss(lang,inGloss,interactive):
	engThes = Thesaurus()
	
	currword = ""
	finaltext = ""
	interlin = ""
	
	for char in inGloss:	
		
		if char not in splitters:
			currword += char
		else:
			print
			print finaltext 
			print interlin
			
			ownThesaurus = Thesaurus(lang+".txt")
			
			if currword == "":
				continue
			
			if interactive:
				while True:
					print
					print "Word: "+currword
					options = ownThesaurus.synonymmed(currword)
					if len(options) == 1 and "marker" in options[0].notes:
						chosenword = options[0].wordname
						interw = options[0].synonyms[0]
						break
					elif len(options) == 1:
						print "Found:"
						options[0].printWord()
						if "n" != raw_input("Use this word?"):
							chosenword = options[0].wordname
							interw = options[0].synonyms[0]
							break
					
					print
					print "Options:"
					print
						
					if len(options) == 0:
						options = ownThesaurus.searchForClosestWord(currword,engThes,2,-1)
					if options == False:
						options = []
					for o in range(len(options)):
						print o+1
						options[o].printWord()
					choice = raw_input("Choice - (n)ew, (s)earch, (t)emporary word, number: ")
					if choice == "s":
						currword = raw_input("New word to search for: ")
					elif choice == "t":
						chosenword = raw_input("New word: ")
						interw = currword
						break
					elif choice == "n":
						chosenword = sspace.wordAddWiz(lang)
						interw = currword
						break
					elif isNumber(choice):
						choice = int(choice)-1
						chosenword = options[choice].wordname
						interw = options[choice].synonyms[0]
						break
						
				
			else:
				ownThesaurus = Thesaurus(lang+".txt")
				options = ownThesaurus.synonymmed(currword)
				if len(options) == 0:
					options = ownThesaurus.searchForClosestWord(currword,engThes,2,-1)
					if options == False:
						print "No word available for "+currword
					sys.exit(0)
				chosenword = options[0].wordname
				interw = options[0].synonyms[0]
			
			interlin += interw
			interlin += char
			
			finaltext += chosenword
			finaltext += char
			
			currword = ""
			
		
	return finaltext,interlin

if __name__ == "__main__":
	lang = sys.argv[1]
	
	if ".txt" not in sys.argv[2]:
		inGloss = " ".join(sys.argv[2:])
		outGloss = False
		print autogloss(lang,inGloss,False)
		sys.exit(0)
		
	f = open(sys.argv[2])
	lines = f.readlines()
	f.close()
	
	if len(sys.argv) > 3:
		outfile = sys.argv[3]
	else:
		outfile = False
	
	for line in lines:
		result,interlin = autogloss(lang,line,True)
		result = result.replace(",",", ")
		if outfile:
			g = open(outfile,"a+")
			topline = soundchange(result.replace("-","").replace("\n",""))
			g.write(alloToRoman(topline+"\n"))
			g.write("["+alloToIpa(topline)+"]\n")
			g.write(result+"\n")
			g.write(interlin+"\n")
			g.write("\n")
			g.close()
		print
		print result
		
