# THESE ARE THE METHODS THAT WILL BE NEEDED TO RETRIEVE DATA FROM THE YAHOO FANTASY API
from .Team import Team
from .Player import Player
import json
import simplejson

#RETURNS THE USERS TEAM NAMES ALONGSIDE ROSTERS (i.e. 'NFL':'Mollied Out Welker'&'Roster', 'NBA':'Load Management'&'Roster')
def getleaguesandteams(oauth2):
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
    nflteamkeys=[]
    nbateamkeys=[]
    nhlteamkeys=[]

    print("NFL:")
    for i in range(numnflteams):
        thenflteam=nflseasondictionary["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["teams"][str(i)]
        print(thenflteam)
        print("\n")
        nflteamkeys.append(thenflteam["team"][0][0]["team_key"])

    print("NBA:")
    for i in range(numnbateams):
        thenbateam=nbaseasondictionary["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["teams"][str(i)]
        print(thenbateam)
        print("\n")
        nbateamkeys.append(thenbateam["team"][0][0]["team_key"])

    # 0 NHL TEAMS IN THIS USERS CASE
	# print("NHL:")
	# for i in range(numnhlteams):
	# 	thenhlteam=nhlseasondictionary["fantasy_content"]["users"]["0"]["user"][1]["games"]["0"]["game"][1]["teams"][str(i)]
	# 	print(thenhlteam)
	# 	print("\n")
	# 	nhlteamkeys.append(thenhlteam["team"][0][0]["team_key"])
    print(nflteamkeys) #contains the NFL team keys of the teams that the current logged in user manages
    print(nbateamkeys) #contains the NBA team keys of the teams that the current logged in user manages
	# print(nhlteamkeys) #contains the NHL team keys of the teams that the current logged in user manages
    # These team keys can be used to retrieve the roster of the NFL and NBA teams the user manages
    print(len(nflteamkeys))
    nflteams=[]
    for i in range(len(nflteamkeys)):
        nflteams.append(Team("nfl",nflteamkeys[i],oauth2).dictionary)
        # nflleagueurl='https://fantasysports.yahooapis.com/fantasy/v2/team/'+nflteamkeys[i]+'/roster;'
        # print("NFL ROSTER:")
        # nflteamresponse=oauth2.session.get(nflleagueurl, params={"format": "json"})
        # # print(nflleagueresponse.json())
        # nflteamdictionary=nflteamresponse.json()
        # print(nflteamdictionary["fantasy_content"]["team"][0][4]["url"])
    print("NFL TEAMS LEAGUE NAME, URL, AND ROSTERS:")
    print(nflteams)
    print('\n')
    nbateams=[]
    for i in range(len(nbateamkeys)):
        nbateams.append(Team("nba",nbateamkeys[i],oauth2).dictionary)
    print("NBA TEAMS LEAGUE NAME, URL, AND ROSTERS:")
    print(nbateams)
    allteams=[]
    allteams=nflteams+nbateams
    allteamsjson=json.dumps(allteams)
    print("ALL TEAMS LEAGUE NAME, URL, AND ROSTERS:")
    print(allteamsjson)
    return allteamsjson
    # NOW HAVE ALL THE USERS TEAMS IN A JSON ARRAY [MOLLIED OUT WELKER,LOAD MANAGEMENT]
    # where MOLLIED OUT WELKER is a dictionary of team name, team url, game key, player 1,..,player n


	# Then oauth2=Yahoo_OAuth2(app.config["CONSUMER_KEY"],app.config["CONSUMER_SECRET"],app.config["REDIRECT_URI"])
	# IN Yahoo_OAuth2, go through the procedure as if its the first time (unless access token, refresh token, etc exist) in which case you look into refreshing
