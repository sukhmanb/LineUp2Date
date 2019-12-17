class Player:
    def __init__(self):
        # player_key,player_id,name,editorial_player_key,editorial_team_key,editorial_team_full_name,editorial_team_abbr,bye_weeks,uniform_number,display_position,headshot,is_undroppable,position_type,primary_position,selected_position
        self.player_key=None
        self.player_id=None
        self.fullname=None
        self.firstname=None
        self.lastname=None
        self.editorial_player_key=None
        self.editorial_team_key=None
        self.editorial_team_full_name=None
        self.editorial_team_abbr=None
        self.bye_weeks=None
        self.uniform_number=None
        self.display_position=None
        self.headshot=None
        self.is_undroppable=None
        self.position_type=None
        self.primary_position=None
        self.selected_position=None

    def playerencode(self):
        return self.__dict__

    def print(self):
        print('Player full name:',self.fullname)
        print('Player first name:',self.firstname)
        print('Player last name:',self.lastname)
        print('Player key:',self.player_key)
        print('Player id:',self.player_id)
        print('Player editorial_player_key:',self.editorial_player_key)
        print('Player editorial_team_key:',self.editorial_team_key)
        print('Player editorial_team_full_name:',self.editorial_team_full_name)
        print('Player editorial_team_abbr:',self.editorial_team_abbr)
        print('Player bye week:',self.bye_weeks)
        print('Player uniform number:',self.uniform_number)
        print('Player display position:',self.display_position)
        print('Player head shot:',self.headshot)
        print('Player is undroppable?:',self.is_undroppable)
        print('Player position type:',self.position_type)
        print('Player primary position:',self.primary_position)
        print('Player selected position:',self.selected_position)
        print('\n')



# {'player': [[{'player_key': '390.p.8780'}, {'player_id': '8780'},
# {'name': {'full': 'Matt Ryan', 'first': 'Matt', 'last': 'Ryan', 'ascii_first': 'Matt', 'ascii_last': 'Ryan'}},
# {'editorial_player_key': 'nfl.p.8780'}, {'editorial_team_key': 'nfl.t.1'},
# {'editorial_team_full_name': 'Atlanta Falcons'}, {'editorial_team_abbr': 'Atl'},
# {'bye_weeks': {'week': '9'}}, {'uniform_number': '2'}, {'display_position': 'QB'},
# {'headshot': {'url': 'https://s.yimg.com/iu/api/res/1.2/b0lvZ0mQFE92Uyw4Zsq1Yg--~C/YXBwaWQ9eXNwb3J0cztjaD0yMzM2O2NyPTE7Y3c9MTc5MDtkeD04NTc7ZHk9MDtmaT11bGNyb3A7aD02MDtxPTEwMDt3PTQ2/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08192019/8780.png', 'size': 'small'}, 'image_url': 'https://s.yimg.com/iu/api/res/1.2/b0lvZ0mQFE92Uyw4Zsq1Yg--~C/YXBwaWQ9eXNwb3J0cztjaD0yMzM2O2NyPTE7Y3c9MTc5MDtkeD04NTc7ZHk9MDtmaT11bGNyb3A7aD02MDtxPTEwMDt3PTQ2/https://s.yimg.com/xe/i/us/sp/v/nfl_cutout/players_l/08192019/8780.png'},
# {'is_undroppable': '0'},
# {'position_type': 'O'}, {'primary_position': 'QB'}, {'eligible_positions': [{'position': 'QB'}]},
# {'has_player_notes': 1}, {'has_recent_player_notes': 1}, {'player_notes_last_timestamp': 1573235400}],
# {'selected_position': [{'coverage_type': 'week', 'week': '10'}, {'position': 'QB'}, {'is_flex': 0}]}, {'is_editable': 1}]}
