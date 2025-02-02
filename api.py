from flask import Flask, request, jsonify,redirect
from flask_restful import Resource, Api
import pymongo
from pymongo import MongoClient
from LineUp2Date.Yahoo_OAuth2 import Yahoo_OAuth2
from LineUp2Date.commonmethods import *
import urllib

from flask_cors import CORS
import jsonpickle

app = Flask(__name__, instance_relative_config=True)

app.config.from_pyfile('config.py')

print(app.config["CONSUMER_KEY"])
CORS(app)

print("yeeeow")


@app.route('/signup',methods=['POST'])
def signup():
	email = request.json['email']
	print(email)
	print('SIGNUP FROM REACT APP COMING IN HOTT')
	checkuser=MongoClient(app.config["DATABASE_URI"]).lineup2date.users.find_one({"email":email})
    # If this user is already signed up and has obtained an access token, send them to the home screen.
	if checkuser!=None and checkuser["access_token"]!=None:
		baseurl="/home?"
		emailparams={"email":email}
		redirect_uri = baseurl + urllib.parse.urlencode(emailparams)
		return redirect(redirect_uri)
    # This user has signed up but hasn't completed the OAuth process
	if checkuser!=None and checkuser["access_token"]==None:
		oauth2=Yahoo_OAuth2(email,app.config["CONSUMER_KEY"],app.config["CONSUMER_SECRET"],app.config["REDIRECT_URI"],False,None)

	# OTHERWISE WE ARE DEALING WITH A USER THAT HAS FILLED OUT THE REACT FORM WITH EMAIL. WE NEED TO GET THAT USER A TOKEN. THE PROCESS TO GET A TOKEN INVOLVES GETTING REDIRECTION FROM YAHOO_OAUTH SO WE HAVE TO INITALIZE A YAHOO_OAUTH OBJECT
	# email,consumer_key,consumer_secret,redirect_uri,response_type (code),redirect_uricode,grant_type(WHERE IS THIS),access_token,token_type,expire_in,refresh_token,guid
	# INSERT INTO DATABASE email/some unique user id, consumer_key, consumer_secret, redirect_uri, access token, refresh time (all those fields)
	user={"email":email,"consumer_key":app.config["CONSUMER_KEY"],"consumer_secret":app.config["CONSUMER_SECRET"],"redirect_uri":app.config["REDIRECT_URI"],"response_type":"code","access_token":None,"xoauth_yahoo_guid":None,"refresh_token":None,"expires_in":None,"token_type":None,"token_time":None}
	MongoClient(app.config["DATABASE_URI"],retryWrites='false').lineup2date.users.insert_one(user)
	oauth2=Yahoo_OAuth2(email,app.config["CONSUMER_KEY"],app.config["CONSUMER_SECRET"],app.config["REDIRECT_URI"],False,None)
	return {'auth_url':oauth2.auth_url}
	print(type(oauth2))

@app.route('/signup/callback',methods=['GET'])
def callback():
	print('CALLBACK COMIN IN HOT')
	email = request.args.get('email')
	code = request.args.get('code')
	print(email)
	print(code)
	# RETRIEVE FROM DATABASE email/some unique user id, consumer_key, consumer_secret, and redirect_uri
	user=MongoClient(app.config["DATABASE_URI"]).lineup2date.users.find_one({"email":email})
	oauth2=Yahoo_OAuth2(email,user["consumer_key"],user["consumer_secret"],user["redirect_uri"],True,code)
	# baseurl="http:localhost:3000/home?"
	# emailparams={"email":email}
	# redirect_uri = baseurl + urllib.parse.urlencode(emailparams)
	return redirect('/authorized')

@app.route('/authorized',methods=['GET'])
def authorized():
	return '<div><h3>Authorized! Close the initial window and click <a target="_blank" href="http://localhost:3000">here</a> to access the application.</h3></div>'
@app.route('/home',methods=['GET'])
def home():
	email = request.args.get('email')
	print("EMAIL IS")
	print(email)
	user=MongoClient(app.config["DATABASE_URI"]).lineup2date.users.find_one({"email":email})
	oauth2=Yahoo_OAuth2(email,user["consumer_key"],user["consumer_secret"],user["redirect_uri"],False,None)
	print("GETTING THE DATA")
	return getleaguesandteams(oauth2)

if __name__ == '__main__':
    app.run(debug=True)
