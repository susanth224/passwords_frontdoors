import commands
proxyList=["10.1.1.35","10.1.1.44","10.1.3.11"]

for p in proxyList:
	print p,":",
	try:
		print commands.getstatusoutput("curl --proxy http://n091130:prbbshr7@"+p+":3128/ --head http://www.google.co.in")[1]
	except:print "Not Working"
	print "-"*80
	



