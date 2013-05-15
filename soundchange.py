#!/usr/bin/python
# coding=utf-8

import random
import re
import sys

C = [
	'pp',	'tt',	'kk',	
	'ph',	'th',	'kh',	
	'f',	's','z','c',
	'm',	'n',	'ng',
	'u',	'i','l','r',
	'ŋ',
]

I = ['i','j']
N = ['ng','m','n','ŋ']

V = [
	'i','ʉ',      'u',
	 'e','ø',  'o',
	     'a',
	'E','I','O','1','2',
]


def soundchange(intext):
	print
	outtext = intext.lower()
	outtext = outtext.replace("\n","")
	print outtext
	outtext = outtext.replace("ng","ŋ")
	# vowel assimilation
	outtext = outtext.replace("iau","e")
	outtext = outtext.replace("iua","e")
	print outtext

	for v1 in V:
	#	if v1 != "i":
		for v2 in V:
	#			if v2 != "i":
			outtext = outtext.replace("%su%s" % (v1,v2),"%sw%s" % (v1,v2))

	for v1 in V:
		for v2 in V:
			if v1 != "u" and v2 != "u" and v1 != "i" and v2 != "i":
				outtext = outtext.replace("%s%s" % (v1,v2),"%sr1" % (v1))
				#outtext = outtext.replace("%s%s" % (v1,v2),"%sr1" % v1)
	print outtext

	#consonant shunting
	for v1 in V:
		for v2 in V:
			outtext = outtext.replace("%spp%s" % (v1,v2), "%sb%s" % (v1,v2))
			outtext = outtext.replace("%stt%s" % (v1,v2), "%sd%s" % (v1,v2))
			outtext = outtext.replace("%sph%s" % (v1,v2), "%spp%s" % (v1,v2))
			outtext = outtext.replace("%sth%s" % (v1,v2), "%stt%s" % (v1,v2))

	print outtext
	#umlaut
	for c1 in C:
		outtext = outtext.replace("e%si" % c1, "I%si" % c1)
		outtext = outtext.replace("o%si" % c1, "ø%si" % c1)
		outtext = outtext.replace("a%si" % c1, "E%si" % c1)

	for c1 in C:
		if c1 not in V:
			for c2 in C:
				outtext = outtext.replace("%su%si" % (c1,c2), "%sʉ%si" % (c1,c2))
		
	print outtext
	for n in N:
		for v in V:
			outtext = outtext.replace("%s%s%s" % (n,v,n), "%s%s%s" % (n,n,v))
	#		for n2 in N:
	#			outtext = outtext.replace("%s%s%s" % (n,v,n2), "%s%s%s" % (n,n2,v))
	print outtext
	for c in C:
		for v in V:
			outtext = outtext.replace("%sŋ%s" % (c,v), "%sŋ%s" % (c,v))
			outtext = outtext.replace("%sng%s" % (c,v), "%sng%s" % (c,v))
			outtext = outtext.replace("%sm%s" % (c,v), "%sm%s" % (c,v))
			outtext = outtext.replace("%sn%s" % (c,v), "%sn%s" % (c,v))

	print outtext
	for n in N:
		outtext = outtext.replace("ŋ%s" % n, "%s" % n)
		outtext = outtext.replace("ng%s" % n, "%s" % n)
		outtext = outtext.replace("m%s" % n, "%s" % n)
		outtext = outtext.replace("n%s" % n, "%s" % n)

	print outtext
	#distinguish 'i' and 'j'
	for c in C:
		for v in V:
			outtext = outtext.replace("%si%s" % (c,v), "%sj%s" % (c,v))

	outtext = outtext.replace("jo","jO")
	outtext = outtext.replace("jø","jO")
	outtext = outtext.replace("jʉ","j1")
	outtext = outtext.replace("je","ja")
	outtext = outtext.replace("jE","ja")
	#outtext = outtext.replace("j","i")
	print outtext
	for v1 in V:
		for v2 in V:
			if v1 != "u" and v2 != "u" and v1 != "i" and v2 != "i":
				outtext = outtext.replace("%s%s" % (v1,v2),"%sl1" % (v1))
	print outtext
	outtext = outtext.replace("ŋ","ng")
	print outtext
	return outtext

if __name__ == "__main__":

	infile = sys.argv[1]
	outfile = sys.argv[2]

	inf = open(infile,"r")
	outf = open(outfile,"a+")

	for line in inf.readlines():
		outline = soundchange(line)
		outf.write(line)
		outf.write(outline)
		outf.write("\n")

	inf.close()
	outf.close()

