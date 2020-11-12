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
        print("Successfully read games from json file")
        return json.load(jsf)
    except Error as e:
        print(e)


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating tables")

    try:
        sql = """
             CREATE TABLE Game(
            g_rank decimal(2,0) not null,
            g_title varchar(32) not null,
            g_sales INTEGER not null,
            g_genre varchar(32) not null,
            g_releasedate date not null,
            g_platform varchar(32) not null,
            g_developer varchar(32) not null,
            g_publisher varchar not null
        );"""
        _conn.execute(sql)
        sql = """
             CREATE TABLE Publisher(
                p_publisher VARCHAR(32) not null,
                p_doc date not null,
                p_employees integer not null,
                p_nationkey decimal(3,0),
                p_networth integer not null
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE Developer(
                d_developer VARCHAR(32) not null,
                d_doc date not null,
                d_employees integer not null,
                d_nationkey decimal(3,0),
                d_networth integer not null
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE Nation(
                n_nationkey decimal(3,0) not null,
                n_name char(25) not null,
                n_regionkey decimal(2,0) not null
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE Region(
                r_regionkey decimal(2,0) not null,
                r_name char(25) not null
            );"""
        _conn.execute(sql)
        _conn.commit()
        print("All tables have been created")
    except Error as e:
        _conn.rollback()
        print(e)


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Deleting tables")

    try:

        sql = """DROP TABLE Game"""
        _conn.execute(sql) #execute defined command
        sql = """DROP TABLE Publisher"""
        _conn.execute(sql)
        sql = """DROP TABLE Developer"""
        _conn.execute(sql)
        sql = """DROP TABLE Nation"""
        _conn.execute(sql)
        sql = """DROP TABLE Region"""
        _conn.execute(sql)

        _conn.commit()
        print("All tables have been deleted")
    except Error as e:
        _conn.rollback()
        print(e)


def populateGameTable(_conn, games):
    print("++++++++++++++++++++++++++++++++++")
    print("Populating Game table")

    try:
        for game in games['Games']:
            print("Inserting " + game['g_title'] + " into database")
            sql = "INSERT INTO Game VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
            _conn.execute(sql, (game['g_rank'], game['g_title'], game['g_sales'], game['g_genre'], game['g_releasedate'], game['g_platform'], game['g_developer'], game['g_publisher']))
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
    jsg = open('input/games.json')
    games = readJson(jsg)

    with conn:
        dropTable(conn)
        createTable(conn)
        populateGameTable(conn, games)

    # close connections for practice's sake
    jsg.close()
    closeConnection(conn, database)

if __name__ == '__main__':
    main()
