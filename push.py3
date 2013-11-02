import urllib.request, urllib.parse, urllib.error

api_key = 'API_KEY'
api_secret = 'API_SECRET'
if api_key == "API_KEY":
	print("You have not set your API_KEY (http://push.co/apps)")
	import sys;sys.exit(1)

def push(msg, url=None, article=None, latitude=None, longitude=None, notification_type=None):
	# because push must be 140 characters
	if (len(msg) > 140):
		print("Your message has been truncated.")
	message = msg[0:140]
	opener = urllib.request.build_opener()
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
		
	data = urllib.parse.urlencode(forms)
	try:
		req = urllib.request.Request('http://api.push.co//1.0/push', data.encode('UTF-8'))
		res = opener.open(req)
		data = res.read()
		print(data)
		# I could check this for "success":true
	except urllib.error.HTTPError:
		print("Your message may be too long.")
