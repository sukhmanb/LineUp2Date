import requests
import webbrowser
import urllib.parse
from pymongo import MongoClient
# from rauth.session import OAuth2Session
from rauth import OAuth2Service


class Yahoo_OAuth2:
	def __init__(self,email,consumer_key,consumer_secret,redirect_uri,isCallBack,code):
		self.email=email
		self.consumer_key=consumer_key
		self.consumer_secret=consumer_secret
		self.redirect_uri=redirect_uri
		self.isCallBack=isCallBack
		self.code=code
		# self.oauth = services[oauth_version]['SERVICE'](**service_params)
		# SEARCH MONGODB DATABASE FOR USER WITH THAT EMAIL. CHECK IF ACCESS TOKEN, GUID, REFRESH_TOKEN, ETC ARE NULL.
		user=MongoClient("mongodb://lineup2dateadmin:lineup2date@ds253388.mlab.com:53388/lineup2date").lineup2date.users.find_one({"email":self.email})
		if isCallBack:
			print("ISSA CALLBACK")
			# SINCE WE'RE DEALING WITH A CALLBACK, NEED TO GET ACCESS_TOKEN, WE HAVE CODE WITH US

		else:
			print("EITHER OBTAINING TOKEN FOR THE FIRST TIME OR REFRESHING TOKEN")
			# IF TRUE, THEN THIS IS THE FIRST TIME THE USER IS OBTAINING A TOKEN. THEY NEED TO GO THROUGH FULL WORKFLOW (I.E. BEING REDIRECTED, GETTING THE TOKEN). AT THE END, WRITE ACCESS_TOKEN, REFRESH_TOKEN, GUID ETC TO MONGODB
			if user["access_token"] is None:
				service = OAuth2Service(
				name='YahooOAuth2',
				client_id=self.consumer_key,
				client_secret=self.consumer_secret,
				access_token_url='https://api.login.yahoo.com/oauth2/get_token',
				authorize_url='https://api.login.yahoo.com/oauth2/request_auth',
				base_url='http://63d9ca0e.ngrok.io/signup/')
				params = {'redirect_uri': 'http://63d9ca0e.ngrok.io/signup/callback','response_type': 'code','email':self.email}
				print("PRINTING REDIRECT URL I GUESS")
				url=service.get_authorize_url(**params)
				print(url)
					# response=requests.get(url)
					# print(response.json())
			# ELSE, THE USER HAS A TOKEN AND MOST LIKELY JUST NEEDS TO UPDATE/REFRESH IT. IN THIS CASE, DON'T NEED TO BE REDIRECTED








# EXAMPLE URL : https://api.login.yahoo.com/oauth2/request_auth?client_secret=012a3f81690d4672b23f2bdb568f7c569819a367&redirect_uri=https%3A%2F%2Fwww.facebook.com%2F&response_type=code&client_id=dj0yJmk9NzZqeVlkN29IbFdFJmQ9WVdrOVZEWm5jVmx2TXpBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTlh
# https://api.login.yahoo.com/oauth2/request_auth?client_secret=012a3f81690d4672b23f2bdb568f7c569819a367&redirect_uri=https%3A%2F%2Fwww.facebook.com%2F&response_type=code&client_id=dj0yJmk9NzZqeVlkN29IbFdFJmQ9WVdrOVZEWm5jVmx2TXpBbWNHbzlNQS0tJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTlh
	# def getAuthorizationURL(self):
	# 	print("HELLOOO")
	# 	base_url = "https://api.login.yahoo.com/oauth2/request_auth?"
	# 	paramslist = {"client_secret":self.consumer_secret, "redirect_uri":self.redirect_uri,"response_type":"code","client_id":self.consumer_key}
	# 	url = base_url + urllib.parse.urlencode(paramslist)
	# 	webbrowser.open(url)
		# response=requests.get(url)
		# print(response

		# response = requests.get(base_url, params=paramslist)
		# print(response.json())
		# webbrowser.open(url)
