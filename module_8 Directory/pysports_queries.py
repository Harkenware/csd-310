SELECT PLAYER_ID, First_Name FROM PLAYER_1;

SELECT TEAM_ID, TEAM_NAME FROM TEAM;

cursor=db.cursor()
cursor.execute("SELECT TEAM_ID, TEAM_NAME FROM TEAM")
TEAMS= cursor.fetchall()
for TEAM in TEAMS:
print("PLAYER_ID:{}".format(Player_1[1]))

cursor=db.cursor()
cursor.execute("SELECT PLAYER_ID, First_Name FROM Player_1")
Players= cursor.fetchall()
for TEAM in TEAMS:
print("TEAM_ID:{}".format(TEAM[1]))
