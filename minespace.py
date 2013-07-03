#!/usr/bin/python
# coding=utf-8

import sys,os,random
#import phongen
from nitgen import *
from langthesaurus import *

def isInt(s):
	try:
		int(s)
		return True
	except:
		return False

def help():
	print '''
minespace.py Qituva Swadesh.txt
	'''

'''
sspace.worseSearchForClosestWord(inword,langThes,spaceThes=0,depth=5,skip=0)
sspace.searchForClosestWord(inword,langThes,spaceThes=0,depth=2,skip=0)
sspace.add(lang,word,synonyms,comments)
sspace.wordAddWiz(lang)
'''

if __name__ == "__main__":
	
	if len(sys.argv) <= 1:
		help()
		sys.exit(0)

	elif sys.argv[1] == "wordlist":
		lang = sys.argv[2]
		listfilename = sys.argv[3]
		
		listfile = open(listfilename,"r")
		wordlist = listfile.readlines()
		listfile.close()
		#random.shuffle(wordlist)

		engThesaurus = Thesaurus()
		ownThesaurus = Thesaurus(lang+".txt")

		wordsToTranslate = []

		for listword in wordlist:
			listword = listword.translate(None,".,!\n")
			engWords = engThesaurus.contains(listword)
			wordsToTranslate.extend(engWords)

		for engWord in wordsToTranslate:
			newWordName = NewWord()
			nSynonyms = random.randint(0,3)
			synonyms = []
			
			synonyms.append(engWord.wordname)

			for i in range(nSynonyms):
				currDef = random.choice(synonyms)
				possibleNewWords = engThesaurus.synonymmed(currDef)
				if len(possibleNewWords) > 0:
					newWord = random.choice(possibleNewWords)
					synonyms.append(newWord.wordname)
			
			print newWordName
			print synonyms
			print
			ownThesaurus.add(newWordName,synonyms,"")
	elif sys.argv[1] == "?":
		lang = sys.argv[2]

                engThesaurus = Thesaurus()
                ownThesaurus = Thesaurus(lang+".txt")

                while True:
			engWord = random.choice(engThesaurus.words)
                        newWordName = NewWord()
                        nSynonyms = random.randint(0,3)
                        synonyms = []

                        synonyms.append(engWord.wordname)

                        for i in range(nSynonyms):
                                currDef = random.choice(synonyms)
                                possibleNewWords = engThesaurus.synonymmed(currDef)
                                if len(possibleNewWords) > 0:
                                        newWord = random.choice(possibleNewWords)
                                        synonyms.append(newWord.wordname)

                        print newWordName
                        print synonyms
                        print
			alreadyHave = ownThesaurus.contains(newWordName)
			if len(alreadyHave) > 0:
				print "Already exists."
				for word in alreadyHave:
					word.printWord()
			fine = raw_input("Add this new word? ")
			if fine != "n":
	                        ownThesaurus.add(newWordName,synonyms,"")
			print


	elif sys.argv[1][0] == "?" and isInt(sys.argv[1][1:]):
                lang = sys.argv[2]

                engThesaurus = Thesaurus()
                ownThesaurus = Thesaurus(lang+".txt")

                wordsToTranslate = []
                for i in range(int(sys.argv[1][1:])):
                        wordsToTranslate.append(random.choice(engThesaurus.words))

                for engWord in wordsToTranslate:
                        newWordName = NewWord()
                        nSynonyms = random.randint(0,3)
                        synonyms = []

                        synonyms.append(engWord.wordname)

                        for i in range(nSynonyms):
                                currDef = random.choice(synonyms)
                                possibleNewWords = engThesaurus.synonymmed(currDef)
                                if len(possibleNewWords) > 0:
                                        newWord = random.choice(possibleNewWords)
                                        synonyms.append(newWord.wordname)

                        print newWordName
                        print synonyms
                        print
                        alreadyHave = ownThesaurus.contains(newWordName)
                        if len(alreadyHave) > 0:
                                print "Already exists."
                                for word in alreadyHave:
                                        word.printWord()
                        fine = raw_input("Add this new word? ")
                        if fine != "n":
                                ownThesaurus.add(newWordName,synonyms,"")
			print


	elif isInt(sys.argv[1]):
		lang = sys.argv[2]

                engThesaurus = Thesaurus()
                ownThesaurus = Thesaurus(lang+".txt")

		wordsToTranslate = []
		for i in range(int(sys.argv[1])):
			wordsToTranslate.append(random.choice(engThesaurus.words))

		for engWord in wordsToTranslate:
                        newWordName = NewWord()
                        nSynonyms = random.randint(0,3)
                        synonyms = []

                        synonyms.append(engWord.wordname)

                        for i in range(nSynonyms):
                                currDef = random.choice(synonyms)
                                possibleNewWords = engThesaurus.synonymmed(currDef)
                                if len(possibleNewWords) > 0:
                                        newWord = random.choice(possibleNewWords)
                                        synonyms.append(newWord.wordname)

                        print newWordName
                        print synonyms
                        print
                        ownThesaurus.add(newWordName,synonyms,"")

