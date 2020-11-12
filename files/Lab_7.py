import sqlite3
from sqlite3 import Error
import json


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Opening database within: ", _dbFile)
    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("Successfully connected")
    except Error as e:
        print(e)
    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Closing database: ", _dbFile)

    try:
        _conn.close()
        print("Successfully closed database connection")
    except Error as e:
        print(e)

def readJson(jsf):
    print("++++++++++++++++++++++++++++++++++")
    print("Reading games from json file: ")
    try:
        #load json game objects
        print("Successfully games from json file")
        return json.load(jsf)
        # for game in games['Games']:
        #     print(game)
        # #good practice to close
        # jsf.close()
    except Error as e:
        print(e)


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating Game table")

    try:
        sql = """
            CREATE TABLE Game(
                    g_title varchar(32) not null,
                    g_releasedate DOUBLE not null,
                    g_sales DOUBLE not null,
                    g_developer varchar(32) not null);"""
        _conn.execute(sql) #execute defined command
        _conn.commit()
        print("Game table created")
    except Error as e:
        _conn.rollback()
        print(e)


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Deleting Game table")

    try:
        sql = """DROP TABLE Game"""
        _conn.execute(sql) #execute defined command

        _conn.commit()
        print("Game table has been deleted")
    except Error as e:
        _conn.rollback()
        print(e)


def populateTable(_conn, games):
    print("++++++++++++++++++++++++++++++++++")
    print("Populating Game table")

    try:
        for game in games['Games']:
            print(game['Title'])
            sql = "INSERT INTO Game VALUES (?, ?, ?, ?);"
            _conn.execute(sql, (game['Title'], game['Released'], game['TotalUnitSales(M)'], game['Developer']))
            #_conn.execute(sql, (game['g_title'], game['g_releasedate'], game['g_sales'], game['g_developer']))
            _conn.commit()
        print ("Game table populated")
    except Error as e:
        _conn.rollback()
        print(e)



def main():

    # pass database object as (r) raw string path to db file
    # and create database connection
    database = r"data/tpch.sqlite"
    conn = openConnection(database)

    # open and read data from json file
    jsf = open('input/data.json')
    games = readJson(jsf)
    for game in games['Games']:
        print(game['Title'])
        print(game['Released'])

    with conn:
        dropTable(conn)
        createTable(conn)
        populateTable(conn, games)
    # close connections for practice's sake
    jsf.close()
    closeConnection(conn, database)

if __name__ == '__main__':
    main()
