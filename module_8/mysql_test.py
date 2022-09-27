import mysql.connector
from mysql.connector import errorcode

config = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Koiqdys94617@",
    database="pysports"
)
try:
    db = mysql.connector.connect(**config)
    print("\n Database user{} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print( " The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified databae does not exist")

    else:
        print(err)
finally:
    db.close()
