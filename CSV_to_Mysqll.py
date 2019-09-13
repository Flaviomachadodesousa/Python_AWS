from __future__ import print_function
import mysql.connector
import csv
import logging
from mysql.connector import errorcode

logging.basicConfig(
    filename="csv_to_mysql.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",datefmt='%d/%m/%Y %I:%M:%S'
    )

def csv_db_mysql():

	# Database connection
	_User = input('Your User ')
	_Password = input('Your Password ')
	_Host = input('Your Host ')
	_Port = input('Your Port ')
	_Database = input('Your Database ')


    myfile = input('Enter the CSV you want to import into the bank. ')
    logging.debug(myfile)

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

        cursor = cnx.cursor()
        logging.debug(cnx)

        # Entering the table you want to insert
        table_want = input('Which table do you want to insert ')
        logging.debug(table_want)

        # Opening CSV File 'r' mode Read
        with open(myfile, 'r') as fin:
            dr = csv.DictReader(fin)  # comma is the default delimiter
            # for on each line inside in CSV
            to_db = [(i['bucket_nome'], i['status'], i['usr_id'], i['bkp'], i['mach_id'], i['bkpset'], i['file'], i['size'], i['date modified'], i['etag'], i['storage']) for i in dr]
            logging.debug(to_db)
        # Insert into database
        cursor.executemany("INSERT INTO {} (bucket_nome, status, usr_id, bkp, mach_id, bkpset, file, size, date modified, etag, storage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);".format(table_want),to_db)
        logging.debug(cursor.executemany)

        # Commit on the bank
        cnx.commit()
        logging.debug(cnx.commit())

        # closing cursor connection
        cursor.close()

        # closing database connection
        cnx.close()
        logging.debug(cnx.close())

csv_db_mysql()