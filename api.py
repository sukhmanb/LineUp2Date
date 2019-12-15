from flask import Flask, request
from flask_restful import Resource, Api
import pymongo
from pymongo import MongoClient
from LineUp2Date.Yahoo_OAuth2 import Yahoo_OAuth2

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

	# AT THIS POINT THE USER HAS FILLED OUT THE REACT FORM WITH EMAIL. WE NEED TO GET THAT USER A TOKEN. THE PROCESS TO GET A TOKEN INVOLVES GETTING REDIRECTION FROM YAHOO_OAUTH SO WE HAVE TO INITALIZE A YAHOO_OAUTH OBJECT
	# email,consumer_key,consumer_secret,redirect_uri,response_type (code),redirect_uricode,grant_type(WHERE IS THIS),access_token,token_type,expire_in,refresh_token,guid
	# INSERT INTO DATABASE email/some unique user id, consumer_key, consumer_secret, redirect_uri, access token, refresh time (all those fields)
	user={"email":email,"consumer_key":app.config["CONSUMER_KEY"],"consumer_secret":app.config["CONSUMER_SECRET"],"redirect_uri":app.config["REDIRECT_URI"],"response_type":"code","access_token":None,"guid":None,"refresh_token":None,"token_time":None,"token_type":None}
	MongoClient(app.config["DATABASE_URI"]).lineup2date.users.insert_one(user)
	oauth2=Yahoo_OAuth2(email,app.config["CONSUMER_KEY"],app.config["CONSUMER_SECRET"],app.config["REDIRECT_URI"],False,None)
	MongoClient(app.config["DATABASE_URI"]).lineup2date.users.insert_one(user)

@app.route('/signup/callback/',methods=['GET'])
def callback():
	print('CALLBACK COMIN IN HOT')
	email = request.args.get('email')
	code = request.args.get('code')
	# RETRIEVE FROM DATABASE email/some unique user id, consumer_key, consumer_secret, and redirect_uri
	user=MongoClient(app.config["DATABASE_URI"]).lineup2date.users.find_one({"email":email})
	oauth2=Yahoo_OAuth2(email,user["consumer_key"],user["consumer_secret"],user["redirect_uri"],True,code)


	# Then oauth2=Yahoo_OAuth2(app.config["CONSUMER_KEY"],app.config["CONSUMER_SECRET"],app.config["REDIRECT_URI"])
	# IN Yahoo_OAuth2, go through the procedure as if its the first time (unless access token, refresh token, etc exist) in which case you look into refreshing

if __name__ == '__main__':
    app.run(debug=True)