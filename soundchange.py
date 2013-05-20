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

P = ['pp','tt','kk','ph','th','kh','b','d','g']
F = ['f','s','z','c']
N = ['ng','m','n','ŋ']
L = ['l','r']

I = ['i','j']

V = [
	'i','ʉ',      'u',
	 'e','ø',  'o',
	     'a',
	'E','I','O','1','2',
]

clusters = {}
clusters["pppp"] = "pp"
clusters["pptt"] = "tt"
clusters["ppkk"] = "kk"
clusters["ppph"] = "ph"
clusters["ppth"] = "th"
clusters["ppkh"] = "kh"
clusters["ppf"]  = "ppf"
clusters["pps"]  = "pps"
clusters["ppz"]  = "pps"
clusters["ppc"]  = "ppR"
clusters["ppm"]  = "m"
clusters["ppn"]  = "n"
clusters["ppng"] = "n"
clusters["ppŋ"]  = "n"
clusters["ppl"]  = "ppl"
clusters["ppr"]  = "ppar"

clusters["ttpp"] = "ttpp"
clusters["tttt"] = "tt"
clusters["ttkk"] = "kk"
clusters["ttph"] = "ttph"
clusters["ttth"] = "th"
clusters["ttkh"] = "kh"
clusters["ttf"]  = "ttf"
clusters["tts"]  = "tts"
clusters["ttz"]  = "ttz"
clusters["ttc"]  = "ttR"
clusters["ttm"]  = "ttm"
clusters["ttn"]  = "ttn"
clusters["ttng"] = "ttn"
clusters["ttŋ"]  = "ttn"
clusters["ttl"]  = "ttl"
clusters["ttr"]  = "ttar"

clusters["kkpp"] = "kkpp"
clusters["kktt"] = "kktt"
clusters["kkkk"] = "kk"
clusters["kkph"] = "kkph"
clusters["kkth"] = "kkth"
clusters["kkkh"] = "kh"
clusters["kkf"]  = "kkf"
clusters["kks"]  = "kks"
clusters["kkz"]  = "kkz"
clusters["kkc"]  = "c"
clusters["kkm"]  = "kkng"
clusters["kkn"]  = "kkn"
clusters["kkng"] = "kkng"
clusters["kkŋ"]  = "kkŋ"
clusters["kkl"]  = "kkl"
clusters["kkr"]  = "kkar"

clusters["phpp"] = "ph"
clusters["phtt"] = "th"
clusters["phkk"] = "kh"
clusters["phph"] = "ph"
clusters["phth"] = "th"
clusters["phkh"] = "kh"
clusters["phf"]  = "ppf"
clusters["phs"]  = "pps"
clusters["phz"]  = "pps"
clusters["phc"]  = "ppR"
clusters["phm"]  = "m"
clusters["phn"]  = "n"
clusters["phng"] = "n"
clusters["phŋ"]  = "n"
clusters["phl"]  = "ppl"
clusters["phr"]  = "ppar"

clusters["thpp"] = "pp"
clusters["thtt"] = "th"
clusters["thkk"] = "kk"
clusters["thph"] = "ph"
clusters["thth"] = "th"
clusters["thkh"] = "kh"
clusters["thf"]  = "ttf"
clusters["ths"]  = "tts"
clusters["thz"]  = "ttz"
clusters["thc"]  = "ttR"
clusters["thm"]  = "m"
clusters["thn"]  = "n"
clusters["thng"] = "ng"
clusters["thŋ"]  = "ŋ"
clusters["thl"]  = "ttl"
clusters["thr"]  = "thar"

clusters["khpp"] = "pp"
clusters["khtt"] = "tt"
clusters["khkk"] = "kh"
clusters["khph"] = "ph"
clusters["khth"] = "th"
clusters["khkh"] = "kh"
clusters["khf"]  = "kkf"
clusters["khs"]  = "kks"
clusters["khz"]  = "kkz"
clusters["khc"]  = "c"
clusters["khm"]  = "kkng"
clusters["khn"]  = "kkn"
clusters["khng"] = "kkng"
clusters["khŋ"]  = "kkŋ"
clusters["khl"]  = "kkl"
clusters["khr"]  = "khar"

clusters["fpp"] = "ppf"
clusters["ftt"] = "ttf"
clusters["fkk"] = "kkf"
clusters["fph"] = "ppf"
clusters["fth"] = "ttf"
clusters["fkh"] = "kkf"
clusters["ff"]  = "f"
clusters["fs"]  = "s"
clusters["fz"]  = "f"
clusters["fc"]  = "z"
clusters["fm"]  = "fm"
clusters["fn"]  = "fn"
clusters["fng"] = "fn"
clusters["fŋ"]  = "fn"
clusters["fl"]  = "fl"
clusters["fr"]  = "far"

clusters["spp"] = "pps"
clusters["stt"] = "tts"
clusters["skk"] = "kks"
clusters["sph"] = "pps"
clusters["sth"] = "tts"
clusters["skh"] = "kks"
clusters["sf"]  = "fs"
clusters["ss"]  = "s"
clusters["sz"]  = "z"
clusters["sc"]  = "z"
clusters["sm"]  = "sm"
clusters["sn"]  = "sn"
clusters["sng"] = "sn"
clusters["sŋ"]  = "sn"
clusters["sl"]  = "sl"
clusters["sr"]  = "sar"

clusters["zpp"] = "ppz"
clusters["ztt"] = "ttz"
clusters["zkk"] = "kkz"
clusters["zph"] = "ppz"
clusters["zth"] = "ttz"
clusters["zkh"] = "kkz"
clusters["zf"]  = "ttz"
clusters["zs"]  = "ttz"
clusters["zz"]  = "z"
clusters["zc"]  = "ttz"
clusters["zm"]  = "zm"
clusters["zn"]  = "zm"
clusters["zng"] = "zm"
clusters["zŋ"]  = "zm"
clusters["zl"]  = "sl"
clusters["zr"]  = "zar"

clusters["cpp"] = "cpp"
clusters["ctt"] = "ctt"
clusters["ckk"] = "ckk"
clusters["cph"] = "cph"
clusters["cth"] = "cth"
clusters["ckh"] = "ckh"
clusters["cf"]  = "c"
clusters["cs"]  = "cs"
clusters["cz"]  = "cs"
clusters["cc"]  = "c"
clusters["cm"]  = "cm"
clusters["cn"]  = "cn"
clusters["cng"] = "cng"
clusters["cŋ"]  = "cŋ"
clusters["cl"]  = "cl"
clusters["cr"]  = "car"

clusters["mpp"] = "ppm"
clusters["mtt"] = "ttn"
clusters["mkk"] = "kkng"
clusters["mph"] = "ppm"
clusters["mth"] = "ttn"
clusters["mkh"] = "kkng"
clusters["mf"]  = "ttn"
clusters["ms"]  = "sn"
clusters["mz"]  = "zn"
clusters["mc"]  = "cng"
clusters["mm"]  = "m"
clusters["mn"]  = "n"
clusters["mng"] = "ng"
clusters["mŋ"]  = "ŋ"
clusters["ml"]  = "ml"
clusters["mr"]  = "mar"

clusters["npp"] = "ppm"
clusters["ntt"] = "ttn"
clusters["nkk"] = "kkng"
clusters["nph"] = "ppm"
clusters["nth"] = "ttn"
clusters["nkh"] = "kkng"
clusters["nf"]  = "ttn"
clusters["ns"]  = "sn"
clusters["nz"]  = "zn"
clusters["nc"]  = "cng"
clusters["nm"]  = "m"
clusters["nn"]  = "n"
clusters["nng"] = "ng"
clusters["nŋ"]  = "ŋ"
clusters["nl"]  = "nl"
clusters["nr"]  = "nar"

clusters["ŋpp"] = "ppm"
clusters["ŋtt"] = "ttn"
clusters["ŋkk"] = "kkŋ"
clusters["ŋph"] = "ppm"
clusters["ŋth"] = "ttn"
clusters["ŋkh"] = "kkŋ"
clusters["ŋf"]  = "fŋ"
clusters["ŋs"]  = "sn"
clusters["ŋz"]  = "zn"
clusters["ŋc"]  = "cŋ"
clusters["ŋm"]  = "m"
clusters["ŋn"]  = "n"
clusters["ŋng"] = "ng"
clusters["ŋŋ"]  = "ŋ"
clusters["ŋl"]  = "ŋl"
clusters["ŋr"]  = "ŋar"

clusters["ngpp"] = "ppm"
clusters["ngtt"] = "ttn"
clusters["ngkk"] = "kkng"
clusters["ngph"] = "ppm"
clusters["ngth"] = "ttn"
clusters["ngkh"] = "kkng"
clusters["ngf"]  = "fng"
clusters["ngs"]  = "sn"
clusters["ngz"]  = "zn"
clusters["ngc"]  = "cng"
clusters["ngm"]  = "m"
clusters["ngn"]  = "n"
clusters["ngng"] = "ng"
clusters["ngŋ"]  = "ŋ"
clusters["ngl"]  = "ngl"
clusters["ngr"]  = "ngar"

clusters["lpp"] = "ppl"
clusters["ltt"] = "ttl"
clusters["lkk"] = "kkl"
clusters["lph"] = "ppl"
clusters["lth"] = "ttl"
clusters["lkh"] = "kkl"
clusters["lf"]  = "fl"
clusters["ls"]  = "sl"
clusters["lz"]  = "zl"
clusters["lc"]  = "cl"
clusters["lm"]  = "ml"
clusters["ln"]  = "nl"
clusters["lng"] = "ngl"
clusters["lŋ"]  = "ŋl"
clusters["ll"]  = "l"
clusters["lr"]  = "lar"

clusters["rpp"] = "rapp"
clusters["rtt"] = "ratt"
clusters["rkk"] = "rakk"
clusters["rph"] = "raph"
clusters["rth"] = "rath"
clusters["rkh"] = "rakh"
clusters["rf"]  = "raf"
clusters["rs"]  = "ras"
clusters["rz"]  = "raz"
clusters["rc"]  = "rac"
clusters["rm"]  = "ram"
clusters["rn"]  = "ran"
clusters["rng"] = "rang"
clusters["rŋ"]  = "raŋ"
clusters["rl"]  = "ral"
clusters["rr"]  = "r"

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

	#voicing - probably forget this
	#for v1 in V:
	#	for v2 in V:
	#		outtext = outtext.replace("%spp%s" % (v1,v2), "%sb%s" % (v1,v2))
	#		outtext = outtext.replace("%stt%s" % (v1,v2), "%sd%s" % (v1,v2))
	#		outtext = outtext.replace("%sph%s" % (v1,v2), "%spp%s" % (v1,v2))
	#		outtext = outtext.replace("%sth%s" % (v1,v2), "%stt%s" % (v1,v2))

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
	
	for cc in clusters:	
		outtext = outtext.replace(cc,clusters[cc])

	print outtext

	outtext = outtext.replace("ŋ","ng")
	print outtext
	return outtext

if __name__ == "__main__":

	infile = sys.argv[1]
	if len(sys.argv) > 2:
		outfile = sys.argv[2]
	else:
		outfile = False

	inf = open(infile,"r")
	if outfile:
		outf = open(outfile,"a+")

	for line in inf.readlines():
		outline = soundchange(line)
		if outfile:
			outf.write(line)
			outf.write(outline)
			outf.write("\n")

	inf.close()
	if outfile:
		outf.close()

