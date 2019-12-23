import requests
import webbrowser
import urllib.parse
from pymongo import MongoClient
# from rauth.session import OAuth2Session
from rauth import OAuth2Service
import json
import time
# import base64
from requests.auth import HTTPBasicAuth



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
		service = OAuth2Service(
		name='YahooOAuth2',
		client_id=self.consumer_key,
		client_secret=self.consumer_secret,
		access_token_url='https://api.login.yahoo.com/oauth2/get_token',
		authorize_url='https://api.login.yahoo.com/oauth2/request_auth',
		base_url='http://63d9ca0e.ngrok.io/signup/')
		user=MongoClient("mongodb://lineup2dateadmin:lineup2date@ds253388.mlab.com:53388/lineup2date",retryWrites='false').lineup2date.users.find_one({"email":self.email})
		if isCallBack:
			print("ISSA CALLBACK")
			# SINCE WE'RE DEALING WITH A CALLBACK, NEED TO GET ACCESS_TOKEN, WE HAVE CODE WITH US
			print(self.code)
			# base_url = "https://api.login.yahoo.com/oauth2/get_token?"
			# paramslist={"client_id":self.consumer_key,"client_secret":self.consumer_secret,"redirect_uri":self.redirect_uri,"code":self.code,"grant_type":"authorization_code"}
			# clientidsecret=self.consumer_key+":"+self.consumer_secret
			# base64clientidsecret=base64.b64encode(clientidsecret)
			# authorizationtype="Basic "+base64clientidsecret
			paramsbody={"grant_type":"authorization_code","redirect_uri":self.redirect_uri,"code":self.code}
			# headers = {"Authorization":authorizationtype,'Content-type': 'application/x-www-form-urlencoded'}
			# # url = base_url + urllib.parse.urlencode(paramslist)
			# # print(url)
			# res = requests.post('https://api.login.yahoo.com/oauth2/get_token',data=json.dumps(paramsbody),headers=headers)
			res = requests.post("https://api.login.yahoo.com/oauth2/get_token", auth=HTTPBasicAuth(self.consumer_key,self.consumer_secret), data=paramsbody)
			print("GETTING THE ACCESS_TOKEN")
			print(res)
			print(res.json())
			tokendictionary=res.json()
			token_time=time.time()
			access_token=tokendictionary.get("access_token")
			refresh_token=tokendictionary.get("refresh_token")
			expires_in=tokendictionary.get("expires_in")
			token_type=tokendictionary.get("token_type")
			xoauth_yahoo_guid=tokendictionary.get("xoauth_yahoo_guid")
			newvalues = { "$set": {"access_token":access_token,"refresh_token":refresh_token,"expires_in":expires_in,"token_type":token_type,"xoauth_yahoo_guid":xoauth_yahoo_guid,"token_time":token_time } }
			updateduser=MongoClient("mongodb://lineup2dateadmin:lineup2date@ds253388.mlab.com:53388/lineup2date",retryWrites='false').lineup2date.users.update_one({"email":self.email},newvalues)
			self.access_token=access_token
			self.refresh_token=refresh_token
			self.expires_in=expires_in
			self.token_type=token_type
			self.xoauth_yahoo_guid=xoauth_yahoo_guid
			self.token_time=token_time
			self.session = service.get_session(token=self.access_token)
			print("PRINTING SELF.SESSION")
			print(self.session)


			# paramslist={"code":self.code,"grant_type":"authorization_code","redirect_uri":self.redirect_uri}
            # RETURNS BAD KEY, TRY DOING IT YOURSELF WITHOUT USING RAUTH
			# session=service.get_auth_session(data=data)

		else:
			print("EITHER OBTAINING TOKEN FOR THE FIRST TIME, REFRESHING TOKEN, OR JUST MAKING SURE TOKEN ISN'T EXPIRED")
			# IF TRUE, THEN THIS IS THE FIRST TIME THE USER IS OBTAINING A TOKEN. THEY NEED TO GO THROUGH FULL WORKFLOW (I.E. BEING REDIRECTED, GETTING THE TOKEN). AT THE END, WRITE ACCESS_TOKEN, REFRESH_TOKEN, GUID ETC TO MONGODB
			if user["access_token"] is None:
				# params = {'redirect_uri': 'http://63d9ca0e.ngrok.io/signup/callback','response_type': 'code','email':self.email}
				print("PRINTING REDIRECT URL I GUESS")
				# url=service.get_authorize_url(**params)
				base_url = "https://api.login.yahoo.com/oauth2/request_auth?"
				redirect_uri = self.redirect_uri+"?"
				emailparams={"email":self.email}
				redirect_uri = redirect_uri + urllib.parse.urlencode(emailparams)
				paramslist = {"client_secret":self.consumer_secret, "redirect_uri":redirect_uri,"response_type":"code","client_id":self.consumer_key,"email":self.email}
				url = base_url + urllib.parse.urlencode(paramslist)
				print(url)
				self.auth_url=url
				# redirect(url)
				# webbrowser.open(url)
					# response=requests.get(url)
					# print(response.json())
			# ELSE, THE USER HAS A TOKEN AND MOST LIKELY JUST NEEDS TO UPDATE/REFRESH IT. IN THIS CASE, DON'T NEED TO BE REDIRECTED
			else:
				self.access_token=user["access_token"]
				self.refresh_token=user["refresh_token"]
				self.expires_in=user["expires_in"]
				self.token_type=user["token_type"]
				self.xoauth_yahoo_guid=user["xoauth_yahoo_guid"]
				self.token_time=user["token_time"]
				elapsed_time=time.time()-self.token_time
				if elapsed_time > 3540:
					# 1 minute until the token is about to expire
					print("TOKEN EXPIRED")
					paramsbody={"grant_type":"refresh_token","redirect_uri":self.redirect_uri,"refresh_token":self.refresh_token}
					res = requests.post("https://api.login.yahoo.com/oauth2/get_token", auth=HTTPBasicAuth(self.consumer_key,self.consumer_secret), data=paramsbody)
					print("GETTING THE REFRESH TOKEN")
					print(res)
					print(res.json())
					tokendictionary=res.json()
					token_time=time.time()
					access_token=tokendictionary.get("access_token")
					refresh_token=tokendictionary.get("refresh_token")
					expires_in=tokendictionary.get("expires_in")
					token_type=tokendictionary.get("token_type")
					xoauth_yahoo_guid=tokendictionary.get("xoauth_yahoo_guid")
					newvalues = { "$set": {"access_token":access_token,"refresh_token":refresh_token,"expires_in":expires_in,"token_type":token_type,"xoauth_yahoo_guid":xoauth_yahoo_guid,"token_time":token_time } }
					updateduser=MongoClient("mongodb://lineup2dateadmin:lineup2date@ds253388.mlab.com:53388/lineup2date",retryWrites='false').lineup2date.users.update_one({"email":self.email},newvalues)
					self.access_token=access_token
					self.refresh_token=refresh_token
					self.expires_in=expires_in
					self.token_type=token_type
					self.xoauth_yahoo_guid=xoauth_yahoo_guid
					self.token_time=token_time
					self.session = service.get_session(token=self.access_token)
					print("PRINTING SELF.SESSION")
					print(self.session)
				else:
					print("TOKEN ISN'T EXPIRED")
					self.session = service.get_session(token=self.access_token)
					print("PRINTING SELF.SESSION")
					print(self.session)
        # BELOW WORKS NOW
		# thebaseurl='https://fantasysports.yahooapis.com/fantasy/v2/'
		# theurl=thebaseurl+'users;use_login=1/games/teams' #returns all my teams
		# response=self.session.get(theurl, params={"format": "json"})
		# print(response.json())






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
