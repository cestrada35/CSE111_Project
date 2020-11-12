

CREATE TABLE Game(
                g_title varchar(32) not null,
                g_releasedate date not null,
                g_sales INTEGER not null,
                g_developer varchar(32) not null);

SELECT * 
FROM Game

INSERT INTO Game VALUES ("Minecraft", 2009, 200, "Markus Persson");

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


-- DROP TABLE Game;