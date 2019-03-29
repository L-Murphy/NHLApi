import urllib.request
import json



class ScheduleObject:
	def __init__(self, date):
		self.date = date
		self.url = "https://statsapi.web.nhl.com/api/v1/schedule"
		
		if date != None:
			self.url = self.url + "?date=" + self.date
		
		self.JSON_obj = self.get_JSON_object()
		self.num_games = self.JSON_obj["totalGames"]
		self.game_ids = self.get_game_ids()
		self.games_list = self.make_games_list()
		
	
	def get_JSON_object(self):
		scheduleData = urllib.request.urlopen(self.url).read()
		return json.loads(scheduleData)
			
	def get_game_ids(self):
		game_id_list = []
		game_list = self.JSON_obj["dates"][0]["games"]
		
		for elem in game_list:
			game_id_list.append(elem["gamePk"])
		
		return game_id_list
		
	def make_games_list(self):
		lst = []
		for g in self.game_ids:
			game_obj = GameObject(g)
			lst.append(game_obj)
		return lst	
		
	def get_games(self):
		return self.games_list

	def __str__(self):
		for game in self.games_list:
			print("\n")
			game.display()
		return ""

class GameObject:
		def __init__(self, gameID):
			self.gameID = gameID
			self.url = "https://statsapi.web.nhl.com/api/v1/game/" + str(self.gameID) +"/feed/live"
			self.game_JSON = self.get_JSON_object()
			self.teams_JSON_obj = self.game_JSON["boxscore"]["teams"]
			#self.start_time =  self.convert_start_time()
			self.home_team = self.teams_JSON_obj["home"]
			self.away_team = self.teams_JSON_obj["away"]
			
		def get_JSON_object(self):
			gameData = urllib.request.urlopen(self.url).read()
			return json.loads(gameData)["liveData"]
		
		def convert_start_time(self):
			game_time = self.game_JSON["datetime"]["dateTime"].split("T") #[date, timeZ]
			game_time = game_time[1].split("Z") #[time, '']
			time_lst =  game_time[0].split(":") #[hour, minute, seconds]
			time_num_shift = int(time_lst[0]) - 11 #converts to EST the hours....Need to look at more. Fails for am games
			return str(time_num_shift) + ":" + time_lst[1] #makes into a human readable string
		
		def get_state(self):
			status = self.game_JSON["status"]
			return {"abstract" : status["abstractGameState"], "detailed" : status["detailedState"]}
		
		def display(self):
			ABV_away = str(self.away_team["team"]["abbreviation"])
			score_away = str(self.away_team["teamStats"]["teamSkaterStats"]["goals"])
			ABV_home = str(self.home_team["team"]["abbreviation"])
			score_home = str(self.home_team["teamStats"]["teamSkaterStats"]["goals"])

			period = str(self.game_JSON["linescore"]["currentPeriodOrdinal"])
			time = str(self.game_JSON["linescore"]["currentPeriodTimeRemaining"])

			print(ABV_away + "|" + score_away + "|" + period)
			print("vs")
			print(ABV_home + "|" + score_home + "|" + time)


'''
Not sure of the value of the team object at this point	
class TeamObject:
	def __init__(self, team_id):
		self.team_id = team_id
		self.url = "https://statsapi.web.nhl.com/api/v1/teams/" + str(self.team_id)
		self.team_JSON_obj = self.get_JSON_object()["teams"][0]
		self.team_name = self.team_JSON_obj["name"]
		self.team_abbreviation = self.team_JSON_obj["abbreviation"]
		print(self.team_name)

	def get_JSON_object(self):
		gameData = urllib.request.urlopen(self.url).read()
		return json.loads(gameData)
'''





if __name__ == "__main__":
	print("starting process \n =============================================================")
	sch = ScheduleObject(None)
	print(sch)
	print("\n ============================================================= \n end process")



	
