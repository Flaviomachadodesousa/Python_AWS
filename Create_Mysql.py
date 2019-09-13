from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode
import logging

# Logging Configuration
logging.basicConfig(
    filename="create_Mysql.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",datefmt='%d/%m/%Y %I:%M:%S'
    )

def create_db():

	# Database connection
	_User = input('Your User ')
	_Password = input('Your Password ')
	_Host = input('Your Host ')
	_Port = input('Your Port ')
	_Database = input('Your Database ')

    # Database connection
    try:
        cnx = mysql.connector.connect(user=_User,password=_Password,host=_Host,port=_Port,database=_Database)
        logging.debug(cnx)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your username or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("The database does not exist.")
        else:
            print(err)
    else:
        print("Connected")
        create_table = input('Enter the name of the table you want to create ')
        logging.debug(create_table)

        # Query for table creation within database
        table = (
            "CREATE TABLE {} ("
            " bkt_id INT(11) NOT NULL AUTO_INCREMENT,"
            " bucket_name varchar(50),"
            " status varchar(10),"
            " usr_id varchar(70),"
            " bkp varchar(70),"
            " mach_id varchar(30),"
            " bkpset varchar(30),"
            " file varchar(60),"
            " size INT(10),"
            " date_modified varchar(30),"
            " etag varchar(255),"
            " storage varchar(30),"
            " action varchar(30),"
            " PRIMARY KEY (bkt_id)"
            ") ENGINE=InnoDB"
        ).format(create_table)
        logging.debug(table)

        # Cursor opens cursor connection
        cursor = cnx.cursor()
        logging.debug(cursor)

        try:
            # Execution for table creation
            cursor.execute(table)
            print('Table {} successfully created'.format(create_table))
        except mysql.connector.Error as err:
            print("Failed to create table: {}".format(err))
            exit(1)

        cnx.commit()
        logging.debug(cnx.commit())
        cnx.close()
        logging.debug(cnx.close())

create_db()