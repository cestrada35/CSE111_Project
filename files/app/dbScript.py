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
        sql = """
            CREATE TABLE Developer_Nation (
            d_developer VARCHAR (32),
            n_nationkey DECIMAL (3, 0),
            FOREIGN KEY (
                d_developer
            )
            REFERENCES Developer (d_developer),
            FOREIGN KEY (
                n_nationkey
            )
            REFERENCES Developer (n_nationkey) 
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE Publisher_Developer (
            p_publisher VARCHAR (32),
            d_developer VARCHAR (32),
            FOREIGN KEY (
                p_publisher
            )
            REFERENCES Developer (p_publisher),
            FOREIGN KEY (
                d_developer
            )
            REFERENCES Developer (d_developer) 
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE Publisher_Nation (
            p_publisher VARCHAR (32),
            n_nationkey DECIMAL (3, 0),
            FOREIGN KEY (
                p_publisher
            )
            REFERENCES Developer (p_publisher),
            FOREIGN KEY (
                n_nationkey
            )
            REFERENCES Developer (n_nationkey) 
            );"""
        _conn.execute(sql)
        sql = """
            CREATE TABLE SalesTime (
            id           INTEGER      NOT NULL
                                    PRIMARY KEY AUTOINCREMENT,
            st_firstyear INTEGER,
            st_alltime   INTEGER,
            st_game      VARCHAR (32) 
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
        sql = """DROP TABLE Developer_Nation"""
        _conn.execute(sql)
        sql = """DROP TABLE Publisher_Developer"""
        _conn.execute(sql)
        sql = """DROP TABLE Publisher_Nation"""
        _conn.execute(sql)
        sql = """DROP TABLE SalesTime"""
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

def populateManytoManyTables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populating Many 2 Many Tables")
    try:
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Mojang Studios', 'Mojang Studios');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Rockstar Games', 'Rockstar North');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Rockstar Games', 'Rockstar Studios');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Electronic Arts', 'EA Mobile');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Nintendo', 'Nintendo EAD');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('PUBG Corporation', 'PUBG Corporation');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Namco', 'Namco');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Re-Logic', 'Re-Logic');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('505 Games', 'Good Science Studio');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Bethesda Softworks', 'Bethesda Studios');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Blizzard Entertainment', 'Blizzard Entertainment');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('CD Projekt', 'CD Project Red');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Activision', 'Infinity ward');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Activision', 'Treyarch');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Xbox Game Studios', 'Good Science Studio');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('Sega', 'Sonic Team');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Developer
        VALUES ('2k Games', 'Gearbox Software');"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Mojang Studios', 4);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Rockstar North', 5);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('EA Mobile', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Nintendo EAD', 1);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('PUBG Corporation', 3);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Game Freak', 1);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Nintendo R&D1', 1);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Rockstar Studios', 1);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Re-Logic', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Bethesda Game Studios', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Blizzard Entertainment', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('CD Projekt Red', 7);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Infinity Ward', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Treyarch', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Good Science Studios', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Good Science Studios', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('EA Canada', 8);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Konami', 1);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Gearbox Software', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Developer_Nation
        VALUES ('Sonic Team', 1);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Mojang Studios', 4);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Rockstar Games', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Electronic Arts', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Nintendo', 1);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('PUBG Corporation', 3);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Namco', 1);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Re-Logic', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('505 Games', 0);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Bethesda Softworks', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Blizzard Entertainment', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('CD Projekt', 7);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Activision', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Xbox Game Studios', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('Sega', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO Publisher_Nation
        VALUES ('2k Games', 6);"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (11, 24000, 26200, "Mario Kart Wii");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (12, 24000, 26100, "Mario Kart 8");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (13, 24000, 25900, "Wii Sports Resort");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (14, 24000, 25800, "Red Dead Redemtion 2");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (15, 24000, 25700, "New Super Mario Bros");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (16, 24000, 25600, "Terraria");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (17, 24000, 25500, "New Super Mario Bros Wii");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (18, 24000, 25400, "The Elder Scrolls V: Skrim");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (19, 24000, 25300, "Diablo III");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (20, 24000, 25200, "Pokemon Gold/Silver/Crystal	");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (21, 24000, 25100, "Duck Hunt");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (22, 24000, 25000, "Wii Play");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (23, 24000, 24900, "The Witcher 3");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (24, 24000, 24800, "Grand Theft Auto: San Andreas");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (25, 24000, 24700, "Call of Duty: Modern Warfare 3");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (26, 24000, 24600, "Call of Duty: Black Ops");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (27, 24000, 24500, "Grand Theft Auto IV");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (28, 24000, 24400, "Pokemon Sun/Moon");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (29, 24000, 24300, "Pokemon Diamond/Pearl/Platinum");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (30, 24000, 24200, "Call of Duty: Black Ops II");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (31, 24000, 24100, "Kinect Adventures!");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (32, 24000, 24000, "FIFA 18");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (33, 24000, 23900, "Sonic the Hedgehog");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (34, 24000, 23800, "Nintendogs");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (35, 24000, 23700, "Mario Kart DS");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (36, 24000, 23600, "Call of Duty: Modern Warfare 2");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (37, 24000, 23500, "Pokemon Ruby / Sapphire / Emerald");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (38, 24000, 23400, "Borderlands 2");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (39, 24000, 23300, "Super Mario World");"""
        _conn.execute(sql)
        sql = """
        INSERT INTO SalesTime
        VALUES (40, 24000, 23200, "Frogger");"""
        _conn.execute(sql)
        _conn.commit()
        print ("Many 2 Many tables populated")
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
        populateManytoManyTables(conn)
        
    # close connections for practice's sake
    jsg.close()
    jsp.close()
    jsd.close()
    jsn.close()
    jsr.close()
    closeConnection(conn, database)

if __name__ == '__main__':
    main()
