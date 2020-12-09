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

def readJson(js):
    print("++++++++++++++++++++++++++++++++++")
    print("Reading from json file: ")
    try:
        #load json game objects
        print("Successfully read from json file")
        return json.load(js)
    except Error as e:
        print(e)

def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Creating tables")

    try:
        sql = """
            CREATE TABLE Developer (
            id          INTEGER      NOT NULL
                                    PRIMARY KEY AUTOINCREMENT,
            d_developer VARCHAR (32) NOT NULL,
            d_doc       DATE         NOT NULL,
            d_employees INTEGER      NOT NULL,
            d_networth  INTEGER      NOT NULL,
            d_nationkey INTEGER,
            FOREIGN KEY (
                d_nationkey
            )
            REFERENCES Nation (n_nationkey) 
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE Game (
            id            INTEGER        NOT NULL
                                        PRIMARY KEY AUTOINCREMENT,
            g_rank        DECIMAL (2, 0) NOT NULL,
            g_title       VARCHAR (32)   NOT NULL,
            g_sales       NUMERIC        NOT NULL,
            g_genre       VARCHAR (32)   NOT NULL,
            g_releasedate DATE           NOT NULL,
            g_platform    VARCHAR (32)   NOT NULL,
            g_developer   INTEGER,
            g_publisher   INTEGER,
            FOREIGN KEY (
                g_publisher
            )
            REFERENCES Publisher (id),
            FOREIGN KEY (
                g_developer
            )
            REFERENCES Developer (id) 
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE Nation (
            n_nationkey INTEGER   NOT NULL
                                PRIMARY KEY AUTOINCREMENT,
            n_name      CHAR (25) NOT NULL,
            n_regionkey INTEGER,
            FOREIGN KEY (
                n_regionkey
            )
            REFERENCES Region (r_regionkey) 
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE Publisher (
            id          INTEGER      NOT NULL
                                    PRIMARY KEY AUTOINCREMENT,
            p_publisher VARCHAR (32) NOT NULL,
            p_doc       DATE         NOT NULL,
            p_employees INTEGER      NOT NULL,
            p_networth  INTEGER      NOT NULL,
            p_nationkey INTEGER,
            FOREIGN KEY (
                p_nationkey
            )
            REFERENCES Nation (n_nationkey) 
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE Region (
            r_regionkey INTEGER   NOT NULL
                                PRIMARY KEY AUTOINCREMENT,
            r_name      CHAR (25) NOT NULL
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
            sql = "INSERT INTO Game VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);"
            _conn.execute(sql, (game['id'],game['g_rank'], game['g_title'], game['g_sales'], game['g_genre'], game['g_releasedate'], game['g_platform'], game['g_developer'], game['g_publisher']))
            _conn.commit()
        print ("Game table populated")
    except Error as e:
        _conn.rollback()
        print(e)

def populatePublisherTable(_conn, publishers):
    print("++++++++++++++++++++++++++++++++++")
    print("Populating Publisher table")

    try:
        for pub in publishers['Publishers']:
            print("Inserting " + pub['p_publisher'] + " into database")
            sql = "INSERT INTO Publisher VALUES (?, ?, ?, ?, ?, ?);"
            _conn.execute(sql, (pub['id'],pub['p_publisher'],pub['p_doc'],pub['p_employees'],pub['p_networth'],pub['p_nationkey']))
            _conn.commit()
        print ("Publisher table populated")
    except Error as e:
        _conn.rollback()
        print(e)

def populateDeveloperTable(_conn, developers):
    print("++++++++++++++++++++++++++++++++++")
    print("Populating Developer table")

    try:
        for dev in developers['Developer']:
            print("Inserting " + dev['d_developer'] + " into database")
            sql = "INSERT INTO Developer VALUES (?, ?, ?, ?, ?, ?);"
            _conn.execute(sql, (dev['id'],dev['d_developer'],dev['d_doc'],dev['d_employees'],dev['d_networth'],dev['d_nationkey']))
            _conn.commit()
        print ("Developer table populated")
    except Error as e:
        _conn.rollback()
        print(e)

def populateNationTable(_conn, nations):
    print("++++++++++++++++++++++++++++++++++")
    print("Populating Nation table")

    try:
        for nat in nations['Nations']:
            print("Inserting " + nat['n_name'] + " into database")
            sql = "INSERT INTO Nation VALUES (?, ?, ?);"
            _conn.execute(sql, (nat['n_nationkey'],nat['n_name'],nat['n_regionkey']))
            _conn.commit()
        print ("Nation table populated")
    except Error as e:
        _conn.rollback()
        print(e)

def populateRegionTable(_conn, regions):
    print("++++++++++++++++++++++++++++++++++")
    print("Populating Region table")

    try:
        for reg in regions['Region']:
            print("Inserting " + reg['r_name'] + " into database")
            sql = "INSERT INTO Region VALUES (?, ?);"
            _conn.execute(sql, (reg['r_regionkey'],reg['r_name']))
            _conn.commit()
        print ("Region table populated")
    except Error as e:
        _conn.rollback()
        print(e)

def main():
    # pass database object as (r) raw string path to db file
    # and create database connection
    database = r"db.sqlite3"
    conn = openConnection(database)

    # open and read data from json file
    jsg = open('input/games.json')
    games = readJson(jsg)
    jsp = open('input/publisher.json')
    publishers = readJson(jsp)
    jsd = open('input/developer.json')
    developers = readJson(jsd)
    jsn = open('input/nation.json')
    nations = readJson(jsn)
    jsr = open('input/region.json')
    regions = readJson(jsr)

    with conn:
        dropTable(conn)
        createTable(conn)
        populateGameTable(conn, games)
        populatePublisherTable(conn, publishers)
        populateDeveloperTable(conn, developers)
        populateNationTable(conn, nations)
        populateRegionTable(conn, regions)
    # close connections for practice's sake
    jsg.close()
    jsp.close()
    jsd.close()
    jsn.close()
    jsr.close()
    closeConnection(conn, database)

if __name__ == '__main__':
    main()
