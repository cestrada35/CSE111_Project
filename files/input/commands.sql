
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
    p_publisher VARCHAR(32) not null,
    p_doc date not null,
    p_employees integer not null,
    p_nationkey decimal(3,0),
    p_networth integer not null
);
CREATE TABLE Developer(
    d_developer VARCHAR(32) not null,
    d_doc date not null,
    d_employees integer not null,
    d_nationkey decimal(3,0),
    d_networth integer not null
);
CREATE TABLE Nation(
    n_nationkey decimal(3,0) not null,
    n_name char(25) not null,
    n_regionkey decimal(2,0) not null
);

CREATE TABLE Region(
    r_regionkey decimal(2,0) not null,
    r_name char(25) not null

);


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


-- DROP TABLE Game;