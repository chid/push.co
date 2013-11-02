api_key = 'API_KEY'
api_secret = 'API_SECRET'
if api_key == "API_KEY":
	print("You have not set your API_KEY, go to http://push.co/apps")
	import sys;sys.exit(1)

def pushMessage(msg, url=None):	
	# because push must be 140 characters
	if (len(msg) > 140):
		print("Your message has been truncated.")
	message = msg[0:140]
	opener = urllib2.build_opener()
	forms = {
			 "message": message ,
	         "api_key": api_key,
	         "api_secret"        : api_secret	                  
	        }
	if url is not None:
		forms['url'] = url
		forms["view_type"] = 1
		
	data = urllib.urlencode(forms)
	try:
		req = urllib2.Request('http://api.push.co//1.0/push', data)
		res = opener.open(req)
		login_html = res.read()
		print login_html
	except urllib2.HTTPError:
		print "Your message may be too long."