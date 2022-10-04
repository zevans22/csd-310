import mysql.connector

#This will establish the connection to MySQL.
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Koiqdys94617@",
    database="pysports"
)

cursor = db.cursor()

#This code is the insert query for inserting the new record.
sql = "INSERT INTO player (player_id, first_name, last_name, team_id)\
    VALUES (21, 'Smeagol', 'Shire Folf;, 1)"

#This code was used to update the team id of the newly inserted record.
sql = "UPDATE player\
    SET team_id = 2\
    WHERE first_name = 'Smeagol'"

#The code below is the query used to delete the new record from the table.
sql = "DELETE FROM player\
    WHERE first_name = 'Smeagol'"


#Below is the inner join query that will display the data from the two tables.
sql = "SELECT player_id, first_name, last_name, team_name\
    FROM player\
    INNER JOIN team\
        ON player.team_id = team.team_id"


cursor.execute(sql)

rows = cursor.fetchall()

#Below code is formatted to meet the reqirements of the assignment. 
#The 'print (--DISPLAYING PLAYERS--)' will change depending on when the record will be instered, altered, and deleted.
print("-- DISPLAYING PLAYERS AFTER DELETE --")

for x in rows:
    print("Player ID: {}".format(x[0]))
    print("First Name: {}".format(x[1]))
    print("Last Name: {}".format(x[2]))
    print("Team Name: {}".format(x[3]))
    print()


input("Press any key to continue...")

db.close()