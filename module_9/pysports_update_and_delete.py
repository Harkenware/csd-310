//Christopher Morales
//Module 9
//7-10-22
import mysql.connector
from mysql.connector import errorcode
config={
	"user": "root",
	"password": "Zombiezilla1954",
	"host": "127.0.0.1",
	"database": "pysports",
	"raise_on_warnings": True
}
INSERT INTO player (first_name, last_name, team_id)
	VALUES('Pippin', 'Took', 1);

print("--- Displaying team players---")
mycursor = mydb.cursor()
mycursor.execute("SELECT team_id, first_name, last_name, team_name")
team = mycursor.fetchall()
for player in team:
    print("first name: {}".format(player[1]))
    print("last name: {}".format(player[2]))
    print("team name: {}".format(player[3]))
    print("team ID: {}".FROM team WHERE team_name = 'Team Gandalf'))
    print("\n")

SELECT player_id, first_name, last_name, team_name
FROM player
INNER JOIN team
	ON player.team_id= team.team_id;

DELETE FROM player
WHERE first_name = 'smeagol';
