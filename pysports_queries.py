#Connecting to MySQL
import mysql.connector

#Establishing the connection to MySQL's host and username via password while also assigning the information to 'db'.
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Koiqdys94617@",
    database="pysports"
)

#This is to establish that the curser will be using the tables of data from MySQL.
cursor = db.cursor()
    
cursor.execute("SELECT team_id, team_name, mascot FROM team")
teams = cursor.fetchall()
    
#The code below is structured so that the assignment format reqirments will be fulfilled.
print("-- DISPLAYING TEAM RECORDS --")

#The reason my there is an extra line stating 'print()', is becasue otherwise the outputted information is put very close together and is then hard to read. 
for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}".format(team[2]))
    print()

print("-- DISPLAYING PLAYER RECORDS --")

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")       
players = cursor.fetchall()

for player in players:
    print("Player ID: {}".format(player[0]))
    print("First Name: {}".format(player[1]))
    print("Last Name: {}".format(player[2]))
    print("Team ID: {}".format(player[3]))
    print()
    
db.close()