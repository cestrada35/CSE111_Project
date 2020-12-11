-- DROP TABLES --
DROP TABLE Developer;
DROP TABLE Game;
DROP TABLE Nation;
DROP TABLE Publisher;
DROP TABLE Region;
DROP TABLE Publisher_Developer;
DROP TABLE Publisher_Nation;
DROP TABLE Developer_Nation;
DROP TABLE SalesTime;


-- CREATE NECESSARY TABLES --
CREATE TABLE Game(
    g_rank decimal(2,0) not null,
    g_title varchar(32) not null,
    g_sales INTEGER not null,
    g_genre varchar(32) not null,
    g_releasedate date not null,
    g_platform varchar(32) not null,
    g_developer varchar(32) not null,
    g_publisher varchar not null
);
CREATE TABLE Publisher(
    p_publisher VARCHAR(32) PRIMARY KEY,
    p_doc date not null,
    p_employees integer not null,
    p_nationkey decimal(3,0),
    p_networth integer not null
);
CREATE TABLE Developer(
    d_developer VARCHAR(32) PRIMARY KEY,
    d_doc date not null,
    d_employees integer not null,
    d_nationkey decimal(3,0),
    d_networth integer not null
);
CREATE TABLE Nation(
    n_nationkey decimal(3,0) PRIMARY KEY,
    n_name char(25) not null,
    n_regionkey decimal(2,0) not null
);

CREATE TABLE Region(
    r_regionkey decimal(2,0),
    r_name char(25)
);

-- CREATE MANY TO MANY TABLES --
CREATE TABLE Publisher_Developer(
p_publisher VARCHAR(32),
d_developer VARCHAR(32),
FOREIGN KEY(p_publisher) REFERENCES Developer(p_publisher),
FOREIGN KEY(d_developer) REFERENCES Developer(d_developer)
);

CREATE TABLE Publisher_Nation(
p_publisher VARCHAR(32),
n_nationkey decimal(3,0),
FOREIGN KEY(p_publisher) REFERENCES Developer(p_publisher),
FOREIGN KEY(n_nationkey) REFERENCES Developer(n_nationkey)
);

CREATE TABLE Developer_Nation(
d_developer VARCHAR(32),
n_nationkey decimal(3,0),
FOREIGN KEY(d_developer) REFERENCES Developer(d_developer),
FOREIGN KEY(n_nationkey) REFERENCES Developer(n_nationkey)
);

INSERT INTO Publisher_Developer
VALUES ('Mojang Studios', 'Mojang Studios');
INSERT INTO Publisher_Developer
VALUES ('Rockstar Games', 'Rockstar North');
INSERT INTO Publisher_Developer
VALUES ('Rockstar Games', 'Rockstar Studios');
INSERT INTO Publisher_Developer
VALUES ('Electronic Arts', 'EA Mobile');
INSERT INTO Publisher_Developer
VALUES ('Nintendo', 'Nintendo EAD');
INSERT INTO Publisher_Developer
VALUES ('PUBG Corporation', 'PUBG Corporation');
INSERT INTO Publisher_Developer
VALUES ('Namco', 'Namco');
INSERT INTO Publisher_Developer
VALUES ('Re-Logic', 'Re-Logic');
INSERT INTO Publisher_Developer
VALUES ('505 Games', 'Good Science Studio');
INSERT INTO Publisher_Developer
VALUES ('Bethesda Softworks', 'Bethesda Studios');
INSERT INTO Publisher_Developer
VALUES ('Blizzard Entertainment', 'Blizzard Entertainment');
INSERT INTO Publisher_Developer
VALUES ('CD Projekt', 'CD Project Red');
INSERT INTO Publisher_Developer
VALUES ('Activision', 'Infinity ward');
INSERT INTO Publisher_Developer
VALUES ('Activision', 'Treyarch');
INSERT INTO Publisher_Developer
VALUES ('Xbox Game Studios', 'Good Science Studio');
INSERT INTO Publisher_Developer
VALUES ('Sega', 'Sonic Team');
INSERT INTO Publisher_Developer
VALUES ('2k Games', 'Gearbox Software');

INSERT INTO Developer_Nation
VALUES ('Mojang Studios', 4);
INSERT INTO Developer_Nation
VALUES ('Rockstar North', 5);
INSERT INTO Developer_Nation
VALUES ('EA Mobile', 6);
INSERT INTO Developer_Nation
VALUES ('Nintendo EAD', 1);
INSERT INTO Developer_Nation
VALUES ('PUBG Corporation', 3);
INSERT INTO Developer_Nation
VALUES ('Game Freak', 1);
INSERT INTO Developer_Nation
VALUES ('Nintendo R&D1', 1);
INSERT INTO Developer_Nation
VALUES ('Rockstar Studios', 1);
INSERT INTO Developer_Nation
VALUES ('Re-Logic', 6);
INSERT INTO Developer_Nation
VALUES ('Bethesda Game Studios', 6);
INSERT INTO Developer_Nation
VALUES ('Blizzard Entertainment', 6);
INSERT INTO Developer_Nation
VALUES ('CD Projekt Red', 7);
INSERT INTO Developer_Nation
VALUES ('Infinity Ward', 6);
INSERT INTO Developer_Nation
VALUES ('Treyarch', 6);
INSERT INTO Developer_Nation
VALUES ('Good Science Studios', 6);
INSERT INTO Developer_Nation
VALUES ('Good Science Studios', 6);
INSERT INTO Developer_Nation
VALUES ('EA Canada', 8);
INSERT INTO Developer_Nation
VALUES ('Konami', 1);
INSERT INTO Developer_Nation
VALUES ('Gearbox Software', 6);
INSERT INTO Developer_Nation
VALUES ('Sonic Team', 1);

INSERT INTO Publisher_Nation
VALUES ('Mojang Studios', 4);
INSERT INTO Publisher_Nation
VALUES ('Rockstar Games', 6);
INSERT INTO Publisher_Nation
VALUES ('Electronic Arts', 6);
INSERT INTO Publisher_Nation
VALUES ('Nintendo', 1);
INSERT INTO Publisher_Nation
VALUES ('PUBG Corporation', 3);
INSERT INTO Publisher_Nation
VALUES ('Namco', 1);
INSERT INTO Publisher_Nation
VALUES ('Re-Logic', 6);
INSERT INTO Publisher_Nation
VALUES ('505 Games', 0);
INSERT INTO Publisher_Nation
VALUES ('Bethesda Softworks', 6);
INSERT INTO Publisher_Nation
VALUES ('Blizzard Entertainment', 6);
INSERT INTO Publisher_Nation
VALUES ('CD Projekt', 7);
INSERT INTO Publisher_Nation
VALUES ('Activision', 6);
INSERT INTO Publisher_Nation
VALUES ('Xbox Game Studios', 6);
INSERT INTO Publisher_Nation
VALUES ('Sega', 6);
INSERT INTO Publisher_Nation
VALUES ('2k Games', 6);

-- POPULATE TABLES MANUALLY --
INSERT INTO Game VALUES(1, 'Minecraft', 200000000, 'Adventure', '2011-11-18', 'Multi-Platform', 'Mojang Studios', 'Mojang Studios');
INSERT INTO Game VALUES(2, 'Grand Theft Auto V', 130000000, 'Action', '2013-09-17', 'Multi-Platform', 'Rockstar North', 'Rockstar Games');
INSERT INTO Game VALUES(3, 'Tetris (EA)', 100000000, 'Tile-Matching', '2006-09-12', 'Mobile',	'EA Mobile', 'Electronic Arts');
INSERT INTO Game VALUES(4, 'Wii Sports', 82900000, 'Sports', '2006-11-19', 'Wii', 'Nintendo EAD', 'Nintendo');
INSERT INTO Game VALUES(5, 'PUBG', 60000000, 'Battle Royale', '2017-12-20', 'Multi-Platform', 'PUBG Corporation', 'PUBG Corporation');
INSERT INTO Game VALUES(6, 'Super Mario Bros', 48240000, 'Platform', '1985-09-13', 'Multi-Platform', 'Nintendo', 'Nintendo');
INSERT INTO Game VALUES(7, 'Pokemon Red/Green/Blue/Yellow', 47520000, 'RPG', '1996-02-27', 'Multi-Platform', 'Game Freak', 'Nintendo');
INSERT INTO Game VALUES(8, 'Wii Fit', 43800000, 'Fitness', '2007-12-01', 'Wii','Nintendo EAD', 'Nintendo');
INSERT INTO Game VALUES(9, 'Tetris (Nintendo)', 43000000, 'Tile-Matching', '1989-06-14','GameBoy/NES', 'Nintendo R&D1', 'Nintendo');
INSERT INTO Game VALUES(10, 'Pac-Man', 39098000, 'Maze', '1980-07-01', 'Multi-Platform', 'Namco', 'Namco');
INSERT INTO Game VALUES(11, 'Mario Kart Wii', 37320000, 'Racing', '2008-04-10', 'Wii', 'Nintendo EAD', 'Nintendo');
INSERT INTO Game VALUES(12, 'Mario Kart 8', 33220000, 'Racing', '2014-05-29', 'Wii U / Switch', 'Nintendo EAD', 'Nintendo');
INSERT INTO Game VALUES(13, 'Wii Sports Resort', 33130000, 'Sports', '2009-04-25', 'Wii', 'Nintendo EAD', 'Nintendo');
INSERT INTO Game VALUES(14, 'Red Dead Redemption 2', 31000000, 'Action', '2018-10-26', 'Multi-Platform', 'Rockstar Studios', 'Rockstar Games');
INSERT INTO Game VALUES(15, 'New Super Mario Bros.', 30800000, 'Platform', '2006-05-15', 'Nintendo DS', 'Nintendo EAD', 'Nintendo');
INSERT INTO Game VALUES(16, 'Terraria', 30300000, 'Adventure', '2011-05-16', 'Multi-Platform','Re-Logic', 'Re-Logic/505 Games');
INSERT INTO Game VALUES(17, 'New Super Mario Bros Wii', 30300000, 'Platform', '2009-11-11', 'Wii', 'Nitendo EAD', 'Nintendo');
INSERT INTO Game VALUES(18, 'The Elder Scrolls V: Skyrim', 30000000, 'Action-RPG', '2011-11-11', 'Multi-Platform', 'Bethesda Game Studios', 'Bethesda Softworks');
INSERT INTO Game VALUES(19, 'Diablo III', 30000000, 'Hack and Slash', '2012-05-16', 'Multi-Platform', 'Blizzard Entertainment', 'Blizzard Entertainment');
INSERT INTO Game VALUES(20, 'Pokemon Gold/Silver/Crystal', 29490000, 'RPG', '1999-11-21', 'GameBoy Color', 'Game Freak', 'Nintendo');
INSERT INTO Game VALUES(21, 'Duck Hunt', 28300000, 'Light-Gun Shooter', '1984-04-21', 'NES', 'Nintendo R&D1', 'Nintendo');
INSERT INTO Game VALUES(22, 'Wii Play', 28020000, 'Party', '2006-12-02', 'Wii', 'Nintendo EAD', 'Nintendo');
INSERT INTO Game VALUES(23, 'The Witcher 3', 28000000, 'Action-RPG', '2015-05-19', 'Multi-Platform', 'CD Projekt Red', 'CD Projekt');
INSERT INTO Game VALUES(24, 'Grand Theft Auto: San Andreas', 27500000, 'Action', 'Multi-Platform', '2004-10-26', 'Rockstar North', 'Rockstar Games');
INSERT INTO Game VALUES(25, 'Call of Duty: Modern Warfare 3', 26500000, 'FPS', 'Multi-Platform', '2011-11-08', 'Infinity Ward', 'Activision');

INSERT INTO Publisher VALUES('Mojang Studios', '2009-05-01', 70, 4, 1500000000);
INSERT INTO Publisher VALUES('Rockstar Games', '1998-12-01', 2000, 6, 3500000000);
INSERT INTO Publisher VALUES('Electronic Arts', '1982-05-27', 9300, 6, 22900000000);
INSERT INTO Publisher VALUES('Nintendo', '1889-09-23', 6200, 1, 85000000000);
INSERT INTO Publisher VALUES('PUBG Corporation', '2017-09-01', 1000, 3, 4600000000);
INSERT INTO Publisher VALUES('Namco', '1955-06-01', 1066, 1, 6400000000); 
INSERT INTO Publisher VALUES('Re-Logic', '2011-01-01', 10, 6, 1000000000); 
INSERT INTO Publisher VALUES('505 Games', '2006-01-01', 37, 0, 187000000); 
INSERT INTO Publisher VALUES('Bethesda Softworks', '1986-06-28', 400, 6, 3000000000);
INSERT INTO Publisher VALUES('Blizzard Entertainment', '1991-02-01', 4700, 6, 20000000000);
INSERT INTO Publisher VALUES('CD Projekt', '1994-05-01', 1111, 7, 8100000000);
INSERT INTO Publisher VALUES('Activision', '1979-10-01', 9200, 6, 50000000000);

INSERT INTO Developer VALUES('Mojang Studios', '2009-05-01', 70, 4, 1500000000);
INSERT INTO Developer VALUES('Rockstar North', '2001-11-01', 650, 5, 3500000000); 
INSERT INTO Developer VALUES('EA Mobile', '2004-01-01', 800, 6, 5500000000); 
INSERT INTO Developer VALUES('Nintendo EAD', '1983-09-30', 6200, 1, 85000000000); 
INSERT INTO Developer VALUES('PUBG Corporation', '2017-09-01', 1000, 3, 4600000000); 
INSERT INTO Developer VALUES('Game Freak', '1989-04-26', 143, 1, 10000000); 
INSERT INTO Developer VALUES('Nintendo R&D1', '1972-01-01', 100, 1, 85000000000); 
INSERT INTO Developer VALUES('Namco', '1955-06-01', 1066, 1, 6400000000); 
INSERT INTO Developer VALUES('Rockstar Studios', '1998-12-01', 2000, 6, 3500000000);
INSERT INTO Developer VALUES('Re-Logic', '2011-01-01', 10, 6, 100000000); 
INSERT INTO Developer VALUES('Bethesda Game Studios', '2001-01-01', 400, 6, 3000000000);
INSERT INTO Developer VALUES('Blizzard Entertainment', '1991-02-01', 4700, 6, 20000000000);
INSERT INTO Developer VALUES('CD Projekt Red', '2002-02-01', 1111, 7, 2300000000);
INSERT INTO Developer VALUES('Infinity Ward', '2002-05-01', 444, 6, 3000000000);

INSERT INTO nation VALUES(0, 'Italy', 3);
INSERT INTO nation VALUES(1, 'JAPAN', 2);
INSERT INTO nation VALUES(2, 'SCOTLAND', 3);
INSERT INTO nation VALUES(3, 'SOUTH KOREA', 2);
INSERT INTO nation VALUES(4, 'SWEDEN', 3);
INSERT INTO nation VALUES(5, 'UNITED KINGDOM', 3);
INSERT INTO nation VALUES(6, 'UNITED STATES', 1);
INSERT INTO nation VALUES(7, 'POLAND', 3);

INSERT INTO region VALUES(0, 'AFRICA');
INSERT INTO region VALUES(1, 'AMERICA');
INSERT INTO region VALUES(2, 'ASIA');
INSERT INTO region VALUES(3, 'EUROPE');
INSERT INTO region VALUES(4, 'MIDDLE EAST');

INSERT INTO SalesTime
VALUES (11, 24000, 26200, "Mario Kart Wii")
INSERT INTO SalesTime
VALUES (12, 24000, 26100, "Mario Kart 8")
INSERT INTO SalesTime
VALUES (13, 24000, 25900, "Wii Sports Resort")
INSERT INTO SalesTime
VALUES (14, 24000, 25800, "Red Dead Redemtion 2")
INSERT INTO SalesTime
VALUES (15, 24000, 25700, "New Super Mario Bros")
INSERT INTO SalesTime
VALUES (16, 24000, 25600, "Terraria")
INSERT INTO SalesTime
VALUES (17, 24000, 25500, "New Super Mario Bros Wii")
INSERT INTO SalesTime
VALUES (18, 24000, 25400, "The Elder Scrolls V: Skrim")
INSERT INTO SalesTime
VALUES (19, 24000, 25300, "Diablo III")
INSERT INTO SalesTime
VALUES (20, 24000, 25200, "Pokemon Gold/Silver/Crystal	")
INSERT INTO SalesTime
VALUES (21, 24000, 25100, "Duck Hunt")
INSERT INTO SalesTime
VALUES (22, 24000, 25000, "Wii Play")
INSERT INTO SalesTime
VALUES (23, 24000, 24900, "The Witcher 3")
INSERT INTO SalesTime
VALUES (24, 24000, 24800, "Grand Theft Auto: San Andreas")
INSERT INTO SalesTime
VALUES (25, 24000, 24700, "Call of Duty: Modern Warfare 3")
INSERT INTO SalesTime
VALUES (26, 24000, 24600, "Call of Duty: Black Ops")
INSERT INTO SalesTime
VALUES (27, 24000, 24500, "Grand Theft Auto IV")
INSERT INTO SalesTime
VALUES (28, 24000, 24400, "Pokemon Sun/Moon")
INSERT INTO SalesTime
VALUES (29, 24000, 24300, "Pokemon Diamond/Pearl/Platinum")
INSERT INTO SalesTime
VALUES (30, 24000, 24200, "Call of Duty: Black Ops II")
INSERT INTO SalesTime
VALUES (31, 24000, 24100, "Kinect Adventures!")
INSERT INTO SalesTime
VALUES (32, 24000, 24000, "FIFA 18")
INSERT INTO SalesTime
VALUES (33, 24000, 23900, "Sonic the Hedgehog")
INSERT INTO SalesTime
VALUES (34, 24000, 23800, "Nintendogs")
INSERT INTO SalesTime
VALUES (35, 24000, 23700, "Mario Kart DS")
INSERT INTO SalesTime
VALUES (36, 24000, 23600, "Call of Duty: Modern Warfare 2")
INSERT INTO SalesTime
VALUES (37, 24000, 23500, "Pokemon Ruby / Sapphire / Emerald")
INSERT INTO SalesTime
VALUES (38, 24000, 23400, "Borderlands 2")
INSERT INTO SalesTime
VALUES (39, 24000, 23300, "Super Mario World")
INSERT INTO SalesTime
VALUES (40, 24000, 23200, "Frogger")

-- RETURN TABLE CONTENTS --
SELECT *
FROM Game;

SELECT *
FROM Publisher
ORDER BY p_publisher ASC;

SELECT *
FROM Developer
ORDER BY d_developer ASC;

SELECT *
FROM nation;

SELECT *
FROM region;






-- 20 SAMPLE SQL COMMANDS PHASE 2--
-- 1    insert Antarctica as a region
INSERT INTO Region(r_regionkey, r_name)
VALUES (5, "ANTARCTICA");
-- 2   change antarctica to poland based on key
UPDATE Region
SET r_name = "Poland"
WHERE r_regionkey = 5;
-- 3    delete poland from the region table
DELETE FROM Region
WHERE r_name = "Poland";
-- 4    return all the games that "Mojang Studios" have developed
SELECT  g_title
FROM    Game, Developer
WHERE   g_developer = Developer.id
AND     d_developer = 'Mojang Studios';
-- 5     return all the games that were developed in Japan
SELECT  g_title as JapanGames
FROM    Game, Developer, Nation
WHERE   g_developer = Developer.id
AND     d_nationkey = n_nationkey
AND     n_name = "JAPAN";
-- 6     return all publishers located in the U.S.
SELECT  p_publisher as Publishers
FROM    Publisher
WHERE   p_nationkey = 6;
-- 7    return the publisher in the U.S. and Sweden
SELECT  p_publisher as Pubs
FROM    Publisher
WHERE   p_nationkey = 6
UNION 
SELECT  p_publisher
FROM    Publisher
WHERE   p_nationkey = 4;
-- 8     return the salary of the highest grossing developer
SELECT  MAX(d_networth) as MaxDevWorth, d_developer as Developer
FROM    Developer;
-- 9     return the name of the developer that makes the most that is located in the U.S.
SELECT Name as RichestUSDeveloper
FROM    (SELECT  MAX(d_networth), d_developer as Name
         FROM    Developer
         WHERE   d_nationkey = 6);
-- 10    return all developers that are not located in the U.S.
SELECT  d_developer as RichestnonUSDevelopers
FROM    Developer, Nation
WHERE   d_nationkey = n_nationkey
EXCEPT 
SELECT  d_developer
FROM    Developer, Nation
WHERE   d_nationkey = n_nationkey
AND     d_nationkey  = 6;
-- 11    return all the games that sold over 85 million copies
SELECT  g_title as bestSellers
FROM    Game
WHERE   g_sales > 85000000;
-- 12    publishers that were established after the year 1995
SELECT  p_publisher as Publishers
FROM    Publisher
WHERE   (p_doc > '1995-01-01');
-- 13    insert Clash of clans for fun
INSERT INTO Game(id, g_rank, g_title, g_sales, g_genre, g_releasedate, g_platform, g_developer, g_publisher)
VALUES (41, 41, "Clash of Clans", 1, "Action", '2000-01-01', "Mobile", 2, 3);
-- 14   change Clash of clans to Clash royale
UPDATE Game
SET g_title = "Clash Royale"
WHERE g_title = "Clash of Clans";
-- 15    delete Clash Royale from the database
DELETE FROM Game
WHERE g_title = "Clash Royale";
-- 16   return only the top 10 games in descending order
SELECT  g_title as Rank
FROM    Game
ORDER BY g_sales DESC
LIMIT 10;
-- 17   return games and their sales, that were released from 2010 to 2015
SELECT  g_title as Game, g_sales as Total
FROM    Game
WHERE g_releasedate
BETWEEN '2010-01-01' AND '2015-12-30';
-- 18   return all games whose developers were located in ASIA
SELECT  g_title as Game
FROM    Game, Developer, Nation, Region
WHERE   g_developer = Developer.id
AND     d_nationkey = n_nationkey
AND     n_regionkey = r_regionkey
AND     r_regionkey = 2;
-- 19   return everything from every table combined!
SELECT  *
FROM    Game, Developer, Publisher, Nation, Region
WHERE   g_developer = Developer.id
AND     g_publisher = Publisher.id
AND     d_nationkey = n_nationkey
AND     n_regionkey = r_regionkey;
-- 20   return all multi-platform titles and their sales
SELECT  g_title as Game,  g_sales as Total
FROM    Game
WHERE   g_platform = 'Multi-Platform'



--just some more test queries 
SELECT * FROM Game

INSERT INTO Game
VALUES (41, 41, 'Toy Story', 200000, 'action', '2018-01-01' , 'Mobile', 4, 5);

DELETE FROM Game
WHERE g_title = 'Toy Story'


SELECT * FROM Nation

INSERT INTO Nation
VALUES (9, 'EST', 1);

DELETE FROM Nation
WHERE n_name = 'EST'
