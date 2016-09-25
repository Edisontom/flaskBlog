DROP TABLE if EXISTS entries;
CREATE TABLE entries(
id INTEGER PRIMARY KEY autoincrement,
title text NOT NULL,
text text NOT NULL,
image text NOT NULL,
music text NOT NULL
);