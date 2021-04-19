database_of_players = {
"Salah" : {"name": "Mo Saleh", "games_2018": 38, "goals_2018": 22},
"Kane" : {"name": "Harry Kane", "games_2018": 28, "goals_2018": 17},
"Aguero" : {"name": "Sergio Aguero", "games_2018": 33, "goals_2018": 21},
"Lukaku" : {"name": "Romelu Lukaku", "games_2018": 32, "goals_2018": 12},
"Aubameyang" : {"name": "Pierre-Emerick Aubameyang", "games_2018": 26, "goals_2018": 17},
"Mane" : {"name": "Sadio Mane", "games_2018": 36, "goals_2018": 22},
"Vardy" : {"name": "Jamie Vardy", "games_2018": 34, "goals_2018": 18},
"Sterling" : {"name": "Raheem Sterling", "games_2018": 34, "goals_2018": 17},
"Hazard" : {"name": "Eden Hazard", "games_2018": 37, "goals_2018": 16}
}



def calculate_goal_average(games, goals):
    players_goal_average = round(goals / games, 2)
    return (players_goal_average)

for player in database_of_players.keys():
    print(player)

player_one_name = input("Select player one from the list\n")
player_two_name = input("Select player two from the list\n")

player_one_goal_average = calculate_goal_average(database_of_players[player_one_name]["games_2018"], 
                                                 database_of_players[player_one_name]["goals_2018"])
player_two_goal_average = calculate_goal_average(database_of_players[player_two_name]["games_2018"], 
                                                 database_of_players[player_two_name]["goals_2018"])
print("Welcome to my goal comparison tool\n")


print('{} has a  goal average of {} goals per game'.format(player_one_name, player_one_goal_average))
print('{} has a goal average of {} goals per game'.format(player_two_name, player_two_goal_average))

if (player_one_goal_average > player_two_goal_average):
    print ("{} ({}) is a more prolific goal scorer than {} ({})".format(player_one_name, player_one_goal_average, player_two_name, player_two_goal_average))
elif (player_two_goal_average > player_one_goal_average):
   print ("{} ({}) is a more prolific goal scorer than {} ({})".format(player_two_name, player_two_goal_average, player_one_name, player_one_goal_average)) 
else:
    print("{} ({}) is equally good as {} ({})" .format(player_one_name, player_two_goal_average, player_two_name, player_one_goal_average))
