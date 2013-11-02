api_key = 'API_KEY'
api_secret = 'API_SECRET'
if api_key == "API_KEY":
	print("You have not set your API_KEY, go to http://push.co/apps")
	import sys;sys.exit(1)

def push(msg, url=None, article=None, latitude=None, longitude=None, notification_type=None):
	# because push must be 140 characters
	if (len(msg) > 140):
		print("Your message has been truncated.")
	message = msg[0:140]
	opener = urllib2.build_opener()
	forms = {
			 "message"    : message,
	         "api_key"    : api_key,
	         "api_secret" : api_secret	                  
	        }
	if url is not None:
		forms['url'] = url
		forms["view_type"] = 1
	elif article is not None:
		forms['article'] = article
	elif longitude is not None or latitude is not None:
		if latitude == None or longitude == None:
			print("Please set both latitude and longitude")
		else:
			forms["view_type"] = 2
			forms['latitude'] = latitude
			forms['longitude'] = longitude
			
	if notification_type is not None:
		forms['notification_type'] = notification_type
		
	data = urllib.urlencode(forms)
	try:
		req = urllib2.Request('http://api.push.co//1.0/push', data)
		res = opener.open(req)
		login_html = res.read()
		print login_html
	except urllib2.HTTPError:
		print "Your message may be too long."