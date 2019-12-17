from .Player import Player
class Team:
    def __init__(self,game_key,team_key,oauth2):
        self.game_key=game_key
        self.team_key=team_key
        self.setteamnameandroster(oauth2)
    def setteamnameandroster(self,oauth2):
        url='https://fantasysports.yahooapis.com/fantasy/v2/team/'+self.team_key+'/roster;'
        # SET team_name
        if self.game_key=="nfl":
            nflteamresponse=oauth2.session.get(url, params={"format": "json"})
            nflteamdictionary=nflteamresponse.json()
            self.team_name=nflteamdictionary["fantasy_content"]["team"][0][2]["name"]
            self.team_url=nflteamdictionary["fantasy_content"]["team"][0][4]["url"]
            self.roster={}
            self.dictionary={}
            self.dictionary["team_name"]=self.team_name
            self.dictionary["team_url"]=self.team_url
            self.dictionary["game_key"]=self.game_key

            i=0
            fields = ['player_key','player_id','name','editorial_player_key','editorial_team_key','editorial_team_full_name','editorial_team_abbr','bye_weeks','uniform_number','display_position','headshot','is_undroppable','position_type','primary_position']
            while i<len(nflteamdictionary['fantasy_content']['team'][1]['roster']['0']['players'].keys())-1:
                playerjson=nflteamdictionary['fantasy_content']['team'][1]['roster']['0']['players'][str(i)]
                # pprint.pprint(playerjson)

                # print(len(playerjson['player'][0]))
                player=Player()
                j=0
                # print(playerjson['player'][0])
                # print('Length of the players json object is ',len(playerjson['player'][0]))
                while (j<len(playerjson['player'][0])):
                    try:
                        thelist=list(playerjson['player'][0][j].keys())
                    except AttributeError:
                        thelist=[]
                    # print(thelist)
                    k=0
                    while k<len(thelist):
                        # print(thelist[k])
                        # print(playerjson['player'][0][j])
                        if thelist[k] in fields:
                            setattr(player,thelist[k],playerjson['player'][0][j])
                        k+=1
                    j+=1
                player.selected_position=playerjson['player'][1]
                player.player_key=player.player_key['player_key']
                player.player_id=player.player_id['player_id']
                player.fullname=player.name['name']['full']
                player.firstname=player.name['name']['first']
                player.lastname=player.name['name']['last']
                player.editorial_player_key=player.editorial_player_key['editorial_player_key']
                player.editorial_team_key=player.editorial_team_key['editorial_team_key']
                player.editorial_team_full_name=player.editorial_team_full_name['editorial_team_full_name']
                player.editorial_team_abbr=player.editorial_team_abbr['editorial_team_abbr']
                player.bye_weeks=player.bye_weeks['bye_weeks']['week']
                player.uniform_number=player.uniform_number['uniform_number']
                player.display_position=player.display_position['display_position']
                player.is_undroppable=player.is_undroppable['is_undroppable']
                player.position_type=player.position_type['position_type']
                player.primary_position=player.primary_position['primary_position']
                player.selected_position=player.selected_position['selected_position'][1]['position']
                player.print()
                self.roster[player.fullname]=player
                self.dictionary[player.fullname]=player.playerencode()
                # rosterlist.append(player)


    				# print(playerjson['player'][0][j].keys())
    			# print(thelist)

    			# playerjson['player'][0] contains all info except for selected_position, this is in [1]

    			#
    			# print(playerjson.keys()) -> 'players' so everything located in playerjson['players']
    			# PROBLEM IS THAT FOR WHATEVER REASON FOR JUJU AND ADAM THIELEN THE 'EDITORIAL_TEAM_FULL_NAME' OCCUR AT DIFFERENT INDICES
    			# FOR JUJU AND THIELEN: playerjson['player'][0][5] -> 'editorial_player_key' WHEREAS FOR THE OTHER PLAYERS it is 'editorial_team_full_name'
    			# print(playerjson)
    			# print(playerjson)
    			# print(playerjson['player'][0][2]['name']['last'])
    			# print(playerjson['player'][0])
    			# [{'player_key': '390.p.8780'}, {'player_id': '8780'}, {'name': {'full': 'Matt Ryan', 'first': 'Matt', 'last': 'Ryan', 'ascii_first': 'Matt', 'ascii_last': 'Ryan'}}, {'editorial_player_key': 'nfl.p.8780'}, {'editorial_team_key': 'nfl.t.1'}, {'editorial_team_full_name': 'Atlanta Falcons'}, {'editorial_team_abbr': 'Atl'}, {'bye_weeks': {'week': '9'}}, {'uniform_number': '2'}, {'display_position': 'QB'}, {'headshot': {'url': 'https://s.yimg.com/iu/api/res/1.2/b0lvZ0mQFE92Uyw4Zsq1Yg--~C/YXBwaWQ9eXNwb3J0cztjaD0yMzM2O2NyPTE7Y3c9MTc5MDtkeD04NTc7ZHk9MDtmaT11bGNyb3A7aD02MDtxPTEwMDt3PTQ2/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08192019/8780.png', 'size': 'small'}, 'image_url': 'https://s.yimg.com/iu/api/res/1.2/b0lvZ0mQFE92Uyw4Zsq1Yg--~C/YXBwaWQ9eXNwb3J0cztjaD0yMzM2O2NyPTE7Y3c9MTc5MDtkeD04NTc7ZHk9MDtmaT11bGNyb3A7aD02MDtxPTEwMDt3PTQ2/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08192019/8780.png'}, {'is_undroppable': '0'}, {'position_type': 'O'}, {'primary_position': 'QB'}, {'eligible_positions': [{'position': 'QB'}]}, {'has_player_notes': 1}, [], {'player_notes_last_timestamp': 1573235400}]
    			# print(playerjson['player'][1])
    			# position will be QB,WR,WR,RB,RB,W/R/T,BN,BN,BN,BN,BN,BN,BN,K,DEF
    			# {'selected_position': [{'coverage_type': 'week', 'week': '10'}, {'position': 'QB'}, {'is_flex': 0}]}, {'is_editable': 1}]}
    			# print(playerjson['player'][2])
    			# {'is_editable': 1}

    			# For all players:
    			# playerjson['player'][0][0] -> player_key
    			# playerjson['player'][0][1] -> player_id
    			# playerjson['player'][0][2] -> name information

    			# Extract the player_key,player_id,first_name,last_name,team_name,team_name_abbr,uniform_number,natural_position,head_shot from playerjson['player'][0]

    			# Extract the position and is_starter from playerjson['player'][1]

    			# print(playerjson['player'][0])
    			# player=Player()
                i+=1
            print(self.roster.keys())

            # SOMEHOW SET ROSTER, ROSTER WILL BE COMPOSED OF PLAYERS (PLAYER OBJECTS)
            # SHOULD I HAVE A PLAYER CLASS OR NO? PROBABLY SHOULD HAVE IT, PROBLEM IS NESTING OF JSON OBJECTS SO RESEARCH ON THAT
        elif self.game_key=="nba":
            nbateamresponse=oauth2.session.get(url, params={"format": "json"})
            nbateamdictionary=nbateamresponse.json()
            print("NBA TEAM DICTIONARY")
            print(nbateamdictionary)
            self.team_name=nbateamdictionary["fantasy_content"]["team"][0][2]["name"]
            self.team_url=nbateamdictionary["fantasy_content"]["team"][0][4]["url"]
            print(self.team_name)
            print(self.team_url)
            self.roster={}
            self.dictionary={}
            self.dictionary["team_name"]=self.team_name
            self.dictionary["team_url"]=self.team_url
            self.dictionary["game_key"]=self.game_key
            i=0
            fields = ['player_key','player_id','name','editorial_player_key','editorial_team_key','editorial_team_full_name','editorial_team_abbr','uniform_number','display_position','headshot','is_undroppable','position_type','primary_position','eligible_positions']
            while i<len(nbateamdictionary['fantasy_content']['team'][1]['roster']['0']['players'].keys())-1:
                playerjson=nbateamdictionary['fantasy_content']['team'][1]['roster']['0']['players'][str(i)]
                # pprint.pprint(playerjson)

                # print(len(playerjson['player'][0]))
                player=Player()
                j=0
                # print(playerjson['player'][0])
                # print('Length of the players json object is ',len(playerjson['player'][0]))
                while (j<len(playerjson['player'][0])):
                    try:
                        thelist=list(playerjson['player'][0][j].keys())
                    except AttributeError:
                        thelist=[]
                    # print(thelist)
                    k=0
                    while k<len(thelist):
                        # print(thelist[k])
                        # print(playerjson['player'][0][j])
                        if thelist[k] in fields:
                            setattr(player,thelist[k],playerjson['player'][0][j])
                        k+=1
                    j+=1
                player.selected_position=playerjson['player'][1]
                player.player_key=player.player_key['player_key']
                player.player_id=player.player_id['player_id']
                player.fullname=player.name['name']['full']
                player.firstname=player.name['name']['first']
                player.lastname=player.name['name']['last']
                player.editorial_player_key=player.editorial_player_key['editorial_player_key']
                player.editorial_team_key=player.editorial_team_key['editorial_team_key']
                player.editorial_team_full_name=player.editorial_team_full_name['editorial_team_full_name']
                player.editorial_team_abbr=player.editorial_team_abbr['editorial_team_abbr']
                player.uniform_number=player.uniform_number['uniform_number']
                player.display_position=player.display_position['display_position']
                player.is_undroppable=player.is_undroppable['is_undroppable']
                player.position_type=player.position_type['position_type']
                player.primary_position=player.primary_position['primary_position']
                player.selected_position=player.selected_position['selected_position'][1]['position']
                player.print()
                self.roster[player.fullname]=player
                self.dictionary[player.fullname]=player.playerencode()
                i+=1
            print(self.roster.keys())
