#!/usr/bin/python
# coding=utf-8

import sys,os,random
sys.path.append(os.getcwd())

import sspace
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

	from phongen import *

	if len(sys.argv) <= 1:
		help()
		sys.exit(0)

	if sys.argv[1][0] == "?":
		check = True
		sys.argv[1] = sys.argv[1][1:]
	else:
		check = False
		lang = sys.argv[2]

	if sys.argv[1] == "wordlist":
		lang = sys.argv[2]
		listfilename = sys.argv[3]
		
		listfile = open(listfilename,"r")
		wordlist = listfile.readlines()
		listfile.close()
		#random.shuffle(wordlist)

		engThesaurus = Thesaurus()
		ownThesaurus = Thesaurus(lang+".txt")

		wordsToTranslate = []
		failwords = []
		for listword in wordlist:
			listword = listword.translate(None,".,!\n")
			engWords = engThesaurus.contains(listword)
			if len(engWords) == 0:
				failwords.append(listword)
			wordsToTranslate.extend(engWords)
		if len(failwords) > 0:
			print "Failed on:"
			print failwords
			sys.exit(0)
		
		random.shuffle(wordsToTranslate)
		for engWord in wordsToTranslate:
			ownThesaurus = Thesaurus(lang+".txt")
			fine = "n"
			while fine == "n":
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
				if check:
					if len(alreadyHave) > 0:
						print "Already exists."
						for word in alreadyHave:
							word.printWord()

					foundwords = []
					for syn in synonyms:
						fsyn = sspace.searchForClosestWord(syn,ownThesaurus,engThesaurus,2)
						if fsyn:
							foundwords.append(fsyn)
					if len(foundwords) > 0:
						print "Closest matches:"
						for fw in foundwords:
							fw.printWord()
					else:
						print "No similar words found."
	
					fine = raw_input("Add this new word? ")
					if fine != "n" and fine != "s":
						ownThesaurus.add(newWordName,synonyms,"")
				else:
					fine = "y"
					ownThesaurus.add(newWordName,synonyms,"")
				print
		sys.exit(0)

	if sys.argv[1] == '':
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
			if check:
				if len(alreadyHave) > 0:
					print "Already exists."
					for word in alreadyHave:
						word.printWord()

				foundwords = []
				for syn in synonyms:
					fsyn = sspace.searchForClosestWord(syn,ownThesaurus,engThesaurus,2)
					if fsyn:
						foundwords.append(fsyn)
				if len(foundwords) > 0:
					print "Closest matches:"
					for fw in foundwords:
						fw.printWord()
				else:
					print "No similar words found."

				fine = raw_input("Add this new word? ")
				if fine != "n":
					ownThesaurus.add(newWordName,synonyms,"")
			else:
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
			ownThesaurus = Thesaurus(lang+".txt")
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
			if check:
				if len(alreadyHave) > 0:
					print "Already exists."
					for word in alreadyHave:
						word.printWord()

				foundwords = []
				for syn in synonyms:
					fsyn = sspace.searchForClosestWord(syn,ownThesaurus,engThesaurus,2)
					if fsyn:
						foundwords.append(fsyn)
				if len(foundwords) > 0:
					print "Closest matches:"
					for fw in foundwords:
						fw.printWord()
				else:
					print "No similar words found."

				fine = raw_input("Add this new word? ")
       				if fine != "n":
					ownThesaurus.add(newWordName,synonyms,"")
			else:
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
			ownThesaurus = Thesaurus(lang+".txt")
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


			if check:
				fine = raw_input("Add this new word? ")
       				if fine != "n":
					ownThesaurus.add(newWordName,synonyms,"")
			else:
				ownThesaurus.add(newWordName,synonyms,"")

