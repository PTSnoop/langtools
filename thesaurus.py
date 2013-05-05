#!/usr/bin/python
# coding=utf-8

class Word:
	def __init__(self):
		self.wordname = ""
		self.synonyms = []
		self.notes = ""
		
	def fromThesaurus(self,data):
		dataa = data.split("#")
		datums = dataa[0].split(",")
		self.wordname = datums[0]
		self.synonyms = datums[1:]
		if len(dataa) > 1:
			self.notes = dataa[1]
		
	def fromData(self,wordname,synonyms,notes):
		self.wordname = wordname
		self.synonyms = synonyms
		self.notes = notes
		
	def printWord(self):
		print self.wordname
		dat = ""
		for datum in self.synonyms:
			dat += datum
			dat += ", "
		if len(dat) != 0:
			dat = dat[:-2]
		print dat
		if self.notes != "":
			print "Notes: " + self.notes

class Thesaurus:
	def __init__(self,datafile="/files/Files/conlang/langtools/mthes10/mthesaur.txt"):
		self.datafile = datafile
		self.words = []
		#try:
		th = open(datafile,"r")
		for line in th:
			w = Word()
			w.fromThesaurus(line[:-1])
			self.words.append(w)
		th.close()
		self.intact = True
		#except Exception, e:
		#	print e
		#	self.intact = False
		
	def remove(self,newword):
		removes = []
		for word in self.words:
			if word.wordname == newword:
				removes.append(word)
				f = open(self.datafile,"r")
				lines = f.readlines()
				f.close()
				for line in lines:
					if line.split(",")[0] == word.wordname:
						lines.remove(line)
						f = open(self.datafile,"w")
						f.writelines(lines)
						f.close()

		for word in removes:
			self.words.remove(word)

	def contains(self,newword):
		validwords = []
		for word in self.words:
			if word.wordname == newword:
				validwords.append(word)
		return validwords
		
	def synonymmed(self,newword):
		validwords = []
		for word in self.words:
			if newword in word.synonyms:
				validwords.append(word)
		return validwords

	def expand(self,inwords):
		expandedwords = []
		for word in self.words:
			for syn in word.synonyms:
				if syn in inwords:
					expandedwords.append(word)
		return expandedwords
					

	def oneLevelUp(self,wordset):
		outwords = []
		for word in wordset:
			newwords = self.synonymmed(word)
			for newword in newwords:
				outwords.append(newword.wordname)
		return outwords
		
	def add(self,wordName,synonyms,comments):
		w = Word()
		w.fromData(wordName,synonyms,comments)
		saveline = ""
		saveline += wordName + ","
		if len(synonyms) > 0:
			for synonym in synonyms:
				saveline += synonym + ","
			saveline = saveline[:-1]
		if comments != "":
			saveline += "#"
			saveline += comments
		saveline += "\n"
		th = open(self.datafile,"a+")
		th.write(saveline)
		th.close()

#if __name__ == "__main__":
#	import random
#	thesaurus = Thesaurus()
#	random.choice(thesaurus.words).printWord()
