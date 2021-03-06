#Mitchell D. Kwon
#CSD 310
#MOD 9.2

import mysql.connector
from mysql.connector import errorcode
#import statements

config = {
    "user": "pysports_user",
    "password": "Littlecat1!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}
#configuration settings

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")
    #inner join query

    players = cursor.fetchall()
    #getting results from cursor

    print("\n --DISPLAYING PLAYER RECECORDS --")

    for player in players:
        print(" Player ID:{}\n First Name: {}\n Last Name: {}\n Team Name: {}\n" .format(player[0], player[1], player[2], player[3]))
        #a loop to retrieve and print player data

    input("\n\n Press any key to continue...")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()