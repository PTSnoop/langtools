#!/usr/bin/python
# coding=utf-8

import random
import re
import sys

C = [
	'p',	't',	'k',	
	'ph',	'th',	'kh',	
	'f',	's','z','c',
	'm',	'n',	'ng',
	'u',	'i','l','r',
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
]

clusters = {}
clusters["pp"] = ":p"
clusters["pt"] = ":t"
clusters["pk"] = ":k"
clusters["pph"] = ":ph"
clusters["pth"] = ":th"
clusters["pkh"] = ":kh"
clusters["pf"]  = "pf"
clusters["ps"]  = "ps"
clusters["pz"]  = "ps"
clusters["pc"]  = "pr"
clusters["pm"]  = ":m"
clusters["pn"]  = ":n"
clusters["png"] = ":n"
clusters["pŋ"]  = ":n"
clusters["pl"]  = "pl"
clusters["pr"]  = "par"

clusters["tp"] = "tp"
clusters["tt"] = ":t"
clusters["tk"] = ":k"
clusters["tph"] = "tph"
clusters["tth"] = ":th"
clusters["tkh"] = ":kh"
clusters["tf"]  = "tf"
clusters["ts"]  = "ts"
clusters["tz"]  = "tz"
clusters["tc"]  = "tr"
clusters["tm"]  = "tm"
clusters["tn"]  = "tn"
clusters["tng"] = "tn"
clusters["tŋ"]  = "tn"
clusters["tl"]  = "tl"
clusters["tr"]  = "tar"

clusters["kp"] = "kp"
clusters["kt"] = "kt"
clusters["kk"] = ":k"
clusters["kph"] = "kph"
clusters["kth"] = "kth"
clusters["kkh"] = ":kh"
clusters["kf"]  = "kf"
clusters["ks"]  = "ks"
clusters["kz"]  = "kz"
clusters["kc"]  = ":c"
clusters["km"]  = "kng"
clusters["kn"]  = "kn"
clusters["kng"] = "kng"
clusters["kŋ"]  = "kŋ"
clusters["kl"]  = "kl"
clusters["kr"]  = "kar"

clusters["php"] = ":ph"
clusters["pht"] = ":th"
clusters["phk"] = ":kh"
clusters["phph"] = ":ph"
clusters["phth"] = ":th"
clusters["phkh"] = ":kh"
clusters["phf"]  = "pf"
clusters["phs"]  = "ps"
clusters["phz"]  = "ps"
clusters["phc"]  = "pr"
clusters["phm"]  = ":m"
clusters["phn"]  = ":n"
clusters["phng"] = ":n"
clusters["phŋ"]  = ":n"
clusters["phl"]  = "pl"
clusters["phr"]  = "par"

clusters["thp"] = ":p"
clusters["tht"] = ":th"
clusters["thk"] = ":k"
clusters["thph"] = ":ph"
clusters["thth"] = ":th"
clusters["thkh"] = ":kh"
clusters["thf"]  = "tf"
clusters["ths"]  = "ts"
clusters["thz"]  = "tz"
clusters["thc"]  = "tr"
clusters["thm"]  = ":m"
clusters["thn"]  = ":n"
clusters["thng"] = ":ng"
clusters["thŋ"]  = ":ŋ"
clusters["thl"]  = "tl"
clusters["thr"]  = "thar"

clusters["khp"] = ":p"
clusters["kht"] = ":t"
clusters["khk"] = ":kh"
clusters["khph"] = ":ph"
clusters["khth"] = ":th"
clusters["khkh"] = ":kh"
clusters["khf"]  = "kf"
clusters["khs"]  = "ks"
clusters["khz"]  = "kz"
clusters["khc"]  = ":c"
clusters["khm"]  = "kng"
clusters["khn"]  = "kn"
clusters["khng"] = "kng"
clusters["khŋ"]  = "kŋ"
clusters["khl"]  = "kl"
clusters["khr"]  = "khar"

clusters["fp"] = "pf"
clusters["ft"] = "tf"
clusters["fk"] = "kf"
clusters["fph"] = "pf"
clusters["fth"] = "tf"
clusters["fkh"] = "kf"
clusters["ff"]  = ":f"
clusters["fs"]  = ":s"
clusters["fz"]  = ":f"
clusters["fc"]  = ":z"
clusters["fm"]  = "fm"
clusters["fn"]  = "fn"
clusters["fng"] = "fn"
clusters["fŋ"]  = "fn"
clusters["fl"]  = "fl"
clusters["fr"]  = "far"

clusters["sp"] = "ps"
clusters["st"] = "ts"
clusters["sk"] = "ks"
clusters["sph"] = "ps"
clusters["sth"] = "ts"
clusters["skh"] = "ks"
clusters["sf"]  = "fs"
clusters["ss"]  = ":s"
clusters["sz"]  = ":z"
clusters["sc"]  = ":z"
clusters["sm"]  = "sm"
clusters["sn"]  = "sn"
clusters["sng"] = "sn"
clusters["sŋ"]  = "sn"
clusters["sl"]  = "sl"
clusters["sr"]  = "sar"

clusters["zp"] = "pz"
clusters["zt"] = "tz"
clusters["zk"] = "kz"
clusters["zph"] = "pz"
clusters["zth"] = "tz"
clusters["zkh"] = "kz"
clusters["zf"]  = "tz"
clusters["zs"]  = "tz"
clusters["zz"]  = ":z"
clusters["zc"]  = "tz"
clusters["zm"]  = "zm"
clusters["zn"]  = "zm"
clusters["zng"] = "zm"
clusters["zŋ"]  = "zm"
clusters["zl"]  = "sl"
clusters["zr"]  = "zar"

clusters["cp"] = "cp"
clusters["ct"] = "ct"
clusters["ck"] = "ck"
clusters["cph"] = "cph"
clusters["cth"] = "cth"
clusters["ckh"] = "ckh"
clusters["cf"]  = ":c"
clusters["cs"]  = "cs"
clusters["cz"]  = "cs"
clusters["cc"]  = ":c"
clusters["cm"]  = "cm"
clusters["cn"]  = "cn"
clusters["cng"] = "cng"
clusters["cŋ"]  = "cŋ"
clusters["cl"]  = "cl"
clusters["cr"]  = "car"

clusters["mp"] = "pm"
clusters["mt"] = "tn"
clusters["mk"] = "kng"
clusters["mph"] = "pm"
clusters["mth"] = "tn"
clusters["mkh"] = "kng"
clusters["mf"]  = "tn"
clusters["ms"]  = "sn"
clusters["mz"]  = "zn"
clusters["mc"]  = "cng"
clusters["mm"]  = "m"
clusters["mn"]  = "n"
clusters["mng"] = "ng"
clusters["mŋ"]  = "ŋ"
clusters["ml"]  = "ml"
clusters["mr"]  = "mar"

clusters["np"] = "pm"
clusters["nt"] = "tn"
clusters["nk"] = "kng"
clusters["nph"] = "pm"
clusters["nth"] = "tn"
clusters["nkh"] = "kng"
clusters["nf"]  = "tn"
clusters["ns"]  = "sn"
clusters["nz"]  = "zn"
clusters["nc"]  = "cng"
clusters["nm"]  = "m"
clusters["nn"]  = "n"
clusters["nng"] = "ng"
clusters["nŋ"]  = "ŋ"
clusters["nl"]  = "nl"
clusters["nr"]  = "nar"

clusters["ŋp"] = "pm"
clusters["ŋt"] = "tn"
clusters["ŋk"] = "kŋ"
clusters["ŋph"] = "pm"
clusters["ŋth"] = "tn"
clusters["ŋkh"] = "kŋ"
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

clusters["ngp"] = "pm"
clusters["ngt"] = "tn"
clusters["ngk"] = "kng"
clusters["ngph"] = "pm"
clusters["ngth"] = "tn"
clusters["ngkh"] = "kng"
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

clusters["lp"] = "pl"
clusters["lt"] = "tl"
clusters["lk"] = "kl"
clusters["lph"] = "pl"
clusters["lth"] = "tl"
clusters["lkh"] = "kl"
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

clusters["rp"] = "rap"
clusters["rt"] = "rat"
clusters["rk"] = "rak"
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
	outtext = outtext.replace("iau","e:")
	outtext = outtext.replace("iua","e:")
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
	#		outtext = outtext.replace("%sp%s" % (v1,v2), "%sb%s" % (v1,v2))
	#		outtext = outtext.replace("%st%s" % (v1,v2), "%sd%s" % (v1,v2))
	#		outtext = outtext.replace("%sph%s" % (v1,v2), "%sp%s" % (v1,v2))
	#		outtext = outtext.replace("%sth%s" % (v1,v2), "%st%s" % (v1,v2))

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

