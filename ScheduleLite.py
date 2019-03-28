import urllib.request
import json


class ScheduleObject:
	def __init__(self, date):
		self.date = date
		self.url = "https://statsapi.web.nhl.com/api/v1/schedule"
		
		if date != None:
			self.url = self.url + "?date=" + self.date
		
		self.JSON_obj = self.get_JSON_object()
		self.num_games = self.get_num_games()
		self.games_list = self.make_games_list()
		self.game_ids = self.get_game_ids()
		self.game_state = get_game_state()
		
		
	
	def get_JSON_object(self):
		scheduleData = urllib.request.urlopen(self.url).read()
		return json.loads(scheduleData)
		
	def get_num_games(self):
		return self.JSON_obj["totalGames"]
	
	def get_game_ids(self):
		game_id_list = []
		
		
		for elem in self.games_list:
			game_id_list.append(elem["gamePk"])
		
		return game_id_list
		
	def make_games_list(self):
		return self.games_list = self.JSON_obj["dates"][0]["games"]
		
	def make_game_state(self):
		dict = {"abstractState" : None}
		return None
		
	
	def make_easy_JSON(self):
		return None
		
	def simple_view(self):
		x = 0
		for game in self.games_list:
			team = game["teams"]
			print(team["away"]["team"]["name"] + "  " +  str(team["away"]["score"]))
			print("\n vs \n")
			print(team["home"]["team"]["name"] + "  " +  str(team["home"]["score"]))
			print("\n\n\n")
	


if __name__ == "__main__":
	print("starting process \n =============================================================")
	date = input('Date of schedule: ')
	
	sc = ScheduleObject(date)

	sc.simple_view()
	
	print("\n ending process \n ===============================================================")
	

