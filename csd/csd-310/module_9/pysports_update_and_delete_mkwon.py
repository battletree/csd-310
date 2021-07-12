# Mitchell D. Kwon
# CSD 310
# MOD 9.2

import mysql.connector
from mysql.connector import errorcode

# import statements

config = {
    "user": "pysports_user",
    "password": "Littlecat1!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}


# configuration settings

def player_info(cursor, title):
    # a method to perform an inner join between the player and team tables and to print results
    cursor.execute(
        "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()
    # getting the results fromt the cursor

    print("\n -- {} --".format(title))

    for player in players:
        print(" Player ID {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))
        # a loop to retrieve and print player data


try:

    db = mysql.connector.connect(**config)

    cursor = db.cursor()
    # getting the cursor object

    add_player = ("INSERT INTO player(first_name, last_name, team_id)" 
                  "VALUES(%s, %s, %s)")
    # this should insert a player

    player_data = ("alpha", "omegon", 1)
    # data for inserted player

    cursor.execute(add_player, player_data)

    db.commit()

    player_info(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    update_player = ("UPDATE player SET team_id = 2, first_name = 'alpharius', last_name = 'omegon' WHERE first_name = 'alpha'")
    # updating the new player insert with the correct information

    cursor.execute(update_player)

    player_info(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    delete_player = ("DELETE FROM player WHERE first_name = 'alpharius'")
    # deleting newly inserted player information

    cursor.execute(delete_player)

    player_info(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n\ Press any key to continue...")

except mysql.connector.Error as err:
    # execept block to take errors

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
    # last call
