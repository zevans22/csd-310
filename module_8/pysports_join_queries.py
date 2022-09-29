import mysql.connector

#The code below it used t oconnect to the MySQL database.
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Koiqdys94617@",
    database="pysports"
)

cursor = db.cursor()

#Below is the MySQL INNER JOIN Query being repersented by 'sql'.
sql = "SELECT player_id, first_name, last_name, team_name\
    FROM player\
    INNER JOIN team\
        ON player.team_id = team.team_id"

#Below will ensure that the code will execute the MySQL INNER JOIN Query.
cursor.execute(sql)

rows = cursor.fetchall()

#The below code is structured so that the format reqirements are fulfilled. 
print("--DISPLAYING PLAYER RECORDS--")

for x in rows:
    print("Player ID: {}".format(x[0]))
    print("First Name: {}".format(x[1]))
    print("Last Name: {}".format(x[2]))
    print("Team Name: {}".format(x[3]))
    print()


input("Press any key to continue...")

db.close()