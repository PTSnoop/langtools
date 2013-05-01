f = open("walsdump.txt","r")
g = open("walsparsed.txt","a")

flines = f.readlines()
glines = []

for line in flines:
	print line
	if line.find(":") != -1:
		title = line.split(":")[1][1:-1]
		glines.append("\t),\n")
		glines.append("\t\n")
		glines.append("\t\"%s\" => array(\n" % title)
	elif line.find("(") != -1:
		ref = line.split("\t")
		aspect = ref[1]
		countraw = ref[2]
		count = countraw.split(" ")[0][1:]
		glines.append("\t\t\"%s\" => %s,\n" % (aspect,count) )

g.writelines(glines)
		
