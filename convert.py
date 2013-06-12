#!/usr/bin/python
# coding=utf-8

from collections import OrderedDict

C = [
        'p',    't',    'k',
        'ph',   'th',   'kh',
        'f',    's','z','c',
        'm',    'n',    'ng',
        'u',    'i','l','r',
        'ŋ',
]

P = ['p','t','k','ph','th','kh','b','d','g']
F = ['f','s','z','c']
N = ['ng','m','n','ŋ']
L = ['l','r']

I = ['i','j']

V = [
        'i','ʉ',      'u',
         'e','ø',  'o',
             'a',
        'E','I','O','1','2',
        'í','ʉ́',      'ú',
         'é','ǿ',  'ó',
             'á',
        'É','Í','Ó','Ý','ǿ',
]
Vna = [
        'i','ʉ',      'u',
         'e','ø',  'o',
             'a',
        'E','I','O','1','2',
]
Va = [
        'í','ʉ́',      'ú',
         'é','ǿ',  'ó',
             'á',
        'É','Í','Ó','Ý','ǿ',
]


a2r = OrderedDict()

a2r["i:"] = "íi"
a2r["ʉ:"] = "ʉ́ʉ"
a2r["u:"] = "úu"
a2r["e:"] = "ée"
a2r["ø:"] = "ǿø"
a2r["o:"] = "óo"
a2r["a:"] = "áa"
a2r["E:"] = "a"
a2r["I:"] = "e"
a2r["O:"] = "ø"
a2r["1:"] = "ʉ"
a2r["2:"] = "u"
a2r['É:'] = "á"
a2r['Í:'] = "é"
a2r['Ó:'] = "ǿ"
a2r['Ý:'] = "ʉ́"
a2r[":"] = ""
a2r["E"] = "a"
a2r["I"] = "e"
a2r["O"] = "ø"
a2r["1"] = "ʉ"
a2r["2"] = "u"
a2r['É'] = "á"
a2r['Í'] = "é"
a2r['Ó'] = "ǿ"
a2r['Ý'] = "ʉ́"
a2r["ŋ"] = "ng"
a2r["j"] = "i"
a2r["w"] = "u"






a2i = OrderedDict()

a2i["ph"] = "pʰ"
a2i["th"] = "tʰ"
a2i["kh"] = "kʰ"
a2i["ng"] = "ŋ"
a2i["p"] = "p"
a2i["t"] = "t"
a2i["k"] = "k"
a2i["f"] = "f"
a2i["s"] = "s"
a2i["z"] = "ʃ"
a2i["c"] = "x"
a2i["m"] = "m"
a2i["n"] = "n"
a2i["ŋ"] = "ŋ"
a2i["u"] = "u"
a2i["i"] = "i"
a2i["l"] = "l"
a2i["r"] = "ʁ"
a2i[" i"] = " j"
a2i[" ʉ"] = " ʔy"
a2i[" u"] = " w"
a2i[" e"] = " ʔe"
a2i[" ø"] = " ʔø"
a2i[" o"] = " ʔo"
a2i[" a"] = " ʔa"
a2i[" E"] = " ʔɛ"
a2i[" I"] = " ʔɪ"
a2i[" O"] = " ʔɔ"
a2i[" 1"] = " ʔɨ"
a2i[" 2"] = " ʔø"

a2i['í'] = "i"
a2i['ʉ́'] = "ý"
a2i['ú'] = "ú"
a2i['é'] = "é"
a2i['ǿ'] = "ǿ"
a2i['ó'] = "ó"
a2i['á'] = "á"
a2i['É'] = "ɛ́"
a2i['Í'] = "ɪ́"
a2i['Ó'] = "ɔ́"
a2i['Ý'] = "ᵻ́"
a2i["i"] = "i"
a2i["ʉ"] = "y"
a2i["u"] = "u"
a2i["e"] = "e"
a2i["ø"] = "ø"
a2i["o"] = "o"
a2i["a"] = "a"
a2i["E"] = "ɛ"
a2i["I"] = "ɪ"
a2i["O"] = "ɔ"
a2i["1"] = "ɨ"
a2i["2"] = "ø"
a2i["ii"] = "ij"
a2i["ei"] = "ej"
a2i["øi"] = "øj"
a2i["ʉi"] = "ʉj"
a2i["ai"] = "aj"
a2i["oi"] = "oj"
a2i["ui"] = "uj"
a2i["ie"] = "je"
a2i["iø"] = "jø"
a2i["iʉ"] = "jʉ"
a2i["ia"] = "ja"
a2i["io"] = "jo"
a2i["iu"] = "ju"
a2i["eu"] = "ew"
a2i["øu"] = "øw"
a2i["ʉu"] = "ʉw"
a2i["au"] = "aw"
a2i["ou"] = "ow"
a2i["uu"] = "uw"
a2i["ue"] = "we"
a2i["uø"] = "wø"
a2i["uʉ"] = "wʉ"
a2i["ua"] = "wa"
a2i["uo"] = "wo"
a2i["uu"] = "wu"

a2i["íi"] = "íj"
a2i["éi"] = "éj"
a2i["ǿi"] = "ǿj"
a2i["ʉ́i"] = "ʉ́j"
a2i["ái"] = "áj"
a2i["ói"] = "ój"
a2i["úi"] = "új"
a2i["ié"] = "jé"
a2i["iǿ"] = "jǿ"
a2i["iʉ́"] = "jʉ́"
a2i["iá"] = "já"
a2i["ió"] = "jó"
a2i["iú"] = "jú"
a2i["éu"] = "éw"
a2i["ǿu"] = "ǿw"
a2i["ʉ́u"] = "ʉ́w"
a2i["áu"] = "áw"
a2i["óu"] = "ów"
a2i["úu"] = "úw"
a2i["ué"] = "wé"
a2i["uǿ"] = "wǿ"
a2i["uʉ́"] = "wʉ́"
a2i["uá"] = "wá"
a2i["uó"] = "wó"
a2i["uú"] = "wú"


def alloToIpa(allo):
	for change in a2i:
		allo = allo.replace(change,a2i[change])

#	for c in C:
#		for v in range(len(Va)):
#			allo = allo.replace(" %s%s" % (c,Vna[v])," %s%s" % (c,Va[v]))

	newallo = ""
	for word in allo.split(" "):
		accented = False 
		for letter in Va:
			if letter in word:
				accented = True
				break

		if accented:
			newword = word
		else:
			newword = ""
			for c in range(len(word)):
				char = word[c]
				if not accented:
					if char == "i" or char == "u":
						try:
							if word[c+1] not in Vna or (word[c+1] == "i" or word[c+1] == "u"):
								if char == "i":
									char = "í"
								else:
									char = "ú"
								accented = True
						except:
							if char == "i":
								char = "í"
							else:
								char = "ú"
							accented = True
					elif char in Vna:
						for w in range(len(Vna)):
							if char == Vna[w]:
								char = Va[w]
								accented = True
								break
				newword += char				

		newallo += newword + " "
				
	return newallo


def alloToRoman(allo):
	for change in a2r:
		allo = allo.replace(change,a2r[change])
	return allo


