import urllib.request
import json

print("starting process \n =============================================================")

class ScheduleObject:
	def __init__(self, date):
		self.date = date
		self.url = "https://statsapi.web.nhl.com/api/v1/schedule"
		
		if date != None:
			self.url = self.url + "?date=" + self.date
		
		self.JSON_obj = self.get_JSON_object()
		self.num_games = self.get_num_games()
		self.game_ids = self.get_game_ids()
		self.games_list = self.make_games_list()
		
	
	def get_JSON_object(self):
		scheduleData = urllib.request.urlopen(self.url).read()
		return json.loads(scheduleData)
		
	def get_num_games(self):
		return self.JSON_obj["totalGames"]
	
	def get_game_ids(self):
		game_id_list = []
		game_list = self.JSON_obj["dates"][0]["games"]
		
		for elem in game_list:
			game_id_list.append(elem["gamePk"])
		
		return game_id_list
		
	def make_games_list(self):
		self.games_list = []
		for g in self.game_ids:
			self.games_list.append(GameObject(g))
		
		
	def get_games(self):
		return self.games_list

class GameObject:
		def __init__(self, gameID):
			self.gameID = gameID
			self.url = "https://statsapi.web.nhl.com/api/v1/game/" + str(self.gameID) +"/feed/live"
			self.game_JSON = self.get_JSON_object()
			self.teams_JSON_obj = self.get_teams()
			self.home_team = TeamObject(self.get_home_team_obj()["id"])
			self.away_team = TeamObject(self.get_away_team_obj()["id"])
			
		def get_JSON_object(self):
			gameData = urllib.request.urlopen(self.url).read()
			return json.loads(gameData)
		
		def get_teams(self):
			return self.game_JSON["liveData"]["boxscore"]["teams"]
		
		def get_away_team_obj(self):
			return self.teams_JSON_obj["away"]["team"]
		
		def get_home_team_obj(self):
			return self.teams_JSON_obj["home"]["team"]
		
class TeamObject:
	def __init__(self, team_id):
		self.team_id = team_id
		self.url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(self.team_id)
		self.team_JSON_obj = self.get_JSON_object()["teams"][0]
		self.team_name = self.team_JSON_obj["name"]
		self.team_abbreviation = self.team_JSON_obj["abbreviation"]

	def get_JSON_object(self):
		gameData = urllib.request.urlopen(self.url).read()
		return json.loads(gameData)



sc = ScheduleObject(None)

print("\n ============================================================= \n end process")




	
