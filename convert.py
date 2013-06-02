#!/usr/bin/python
# coding=utf-8

a2r = {}

a2r["i:"] = "ii"
a2r["ʉ:"] = "ʉʉ"
a2r["u:"] = "uu"
a2r["e:"] = "ee"
a2r["ø:"] = "øø"
a2r["o:"] = "oo"
a2r["a:"] = "aa"
a2r["E:"] = "a"
a2r["I:"] = "e"
a2r["O:"] = "ø"
a2r["1:"] = "ʉ"
a2r["2:"] = "u"
a2r[":"] = ""
a2r["E"] = "a"
a2r["I"] = "e"
a2r["O"] = "ø"
a2r["1"] = "ʉ"
a2r["2"] = "u"
a2r["ŋ"] = "ng"
a2r["j"] = "i"
a2r["w"] = "u"



a2i = {}

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
a2i["ii"] = "aj"
a2i["ei"] = "ej"
a2i["ai"] = "aj"
a2i["oi"] = "oj"
a2i["ui"] = "uj"
a2i["ie"] = "je"
a2i["ia"] = "ja"
a2i["io"] = "jo"
a2i["iu"] = "ju"
a2i["eu"] = "ew"
a2i["au"] = "aw"
a2i["ou"] = "ow"
a2i["uu"] = "uw"
a2i["ue"] = "we"
a2i["ua"] = "wa"
a2i["uo"] = "wo"
a2i["uu"] = "wu"

def alloToIpa(allo):
	for change in a2i:
		allo = allo.replace(change,a2i[change])
	return allo


def alloToRoman(allo):
	for change in a2r:
		allo = allo.replace(change,a2r[change])
	return allo


