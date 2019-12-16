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
	user={"email":email,"consumer_key":app.config["CONSUMER_KEY"],"consumer_secret":app.config["CONSUMER_SECRET"],"redirect_uri":app.config["REDIRECT_URI"],"response_type":"code","access_token":None,"xoauth_yahoo_guid":None,"refresh_token":None,"expires_in":None,"token_type":None,"token_time":None}
	MongoClient(app.config["DATABASE_URI"],retryWrites='false').lineup2date.users.insert_one(user)
	oauth2=Yahoo_OAuth2(email,app.config["CONSUMER_KEY"],app.config["CONSUMER_SECRET"],app.config["REDIRECT_URI"],False,None)

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

@app.route('/home',methods=['GET'])
def getleaguesandteams():
	email = request.args.get('email')
	user=MongoClient(app.config["DATABASE_URI"]).lineup2date.users.find_one({"email":email})
	oauth2=Yahoo_OAuth2(email,user["consumer_key"],user["consumer_secret"],user["redirect_uri"],False,None)
	thebaseurl='https://fantasysports.yahooapis.com/fantasy/v2/'
	nflurl=thebaseurl+'users;use_login=1/games;game_keys=nfl/teams' #returns my 2019 nfl team information
	nbaurl=thebaseurl+'users;use_login=1/games;game_keys=nba/teams' #returns my 2019 nba teams information
	nhlurl=thebaseurl+'users;use_login=1/games;game_keys=nhl/teams' #returns my 2019 nba teams information
	nflresponse=oauth2.session.get(nflurl, params={"format": "json"})
	nbaresponse=oauth2.session.get(nbaurl, params={"format": "json"})
	nhlresponse=oauth2.session.get(nhlurl, params={"format": "json"})

	nflseasondictionary=nflresponse.json()
	nbaseasondictionary=nbaresponse.json()
	nhlseasondictionary=nhlresponse.json()


	numnflteams=len(nflseasondictionary["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["teams"])-1
	numnbateams=len(nbaseasondictionary["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["teams"])-1
	numnhlteams=len(nhlseasondictionary["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["teams"])-1
	nflleagueids=[]
	nbaleagueids=[]
	nhlleagueids=[]

	print("NFL:")
	for i in range(numnflteams):
		thenflteam=nflseasondictionary["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["teams"][str(i)]
		print(thenflteam)
		print("\n")
		nflleagueids.append(thenflteam["team"][0][0]["team_key"])

	print("NBA:")
	for i in range(numnbateams):
		thenbateam=nbaseasondictionary["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["teams"][str(i)]
		print(thenbateam)
		print("\n")
		nbaleagueids.append(thenbateam["team"][0][0]["team_key"])

    # 0 NHL TEAMS IN THIS USERS CASE
	# print("NHL:")
	# for i in range(numnhlteams):
	# 	thenhlteam=nhlseasondictionary["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["teams"][str(i)]
	# 	print(thenhlteam)
	# 	print("\n")
	# 	nhlleagueids.append(thenhlteam["team"][0][0]["team_key"])
	print(nflleagueids) #contains the NFL team keys of the teams that the current logged in user manages
	print(nbaleagueids) #contains the NBA team keys of the teams that the current logged in user manages
	# print(nhlleagueids) #contains the NHL team keys of the teams that the current logged in user manages
    # These team keys can be used to retrieve the roster of the NFL and NBA teams the user manages

	# Then oauth2=Yahoo_OAuth2(app.config["CONSUMER_KEY"],app.config["CONSUMER_SECRET"],app.config["REDIRECT_URI"])
	# IN Yahoo_OAuth2, go through the procedure as if its the first time (unless access token, refresh token, etc exist) in which case you look into refreshing

if __name__ == '__main__':
    app.run(debug=True)
