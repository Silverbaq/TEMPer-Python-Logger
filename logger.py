#!/usr/bin/python
import subprocess
import MySQLdb
from time import sleep

temp = "empty"

def ReadTempetur():
    global temp
    temp = subprocess.Popen("sudo temper-poll -c -q", shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
    print "The tempeture is %s C" %(temp.rstrip())

def AddToDB():
    # Open database connection
    db = MySQLdb.connect("localhost","temper","repmet","TEMPer")
    
    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # prepares the sql query
    sql = "INSERT INTO TEMPer.Log(TempeturC,Location)VALUES('%s','Pi1')"%(temp)

    try:

        # execute SQL query using execute() method.
        cursor.execute(sql)

        # Commit your changes in the database
        db.commit()

        # Fetch a single row using fetchone() method.
        # data = cursor.fetchone()

        # disconnect from server
        db.close()
    except:
	# Rollback in vase there is any error
	db.rollback()

def main():
    while (True):
        ReadTempetur()
	AddToDB()
	# Sleeps for a minut
	sleep(60)

main()
