-- Table definitions for the tournament project. 
-- The purpose of this file is to set up our data structure: the tables and views. 
--

-- drop if exists
DROP DATABASE IF EXISTS tournament;

-- create database
Create database tournament;

-- connect the database
\c tournament

-- drop if exists
DROP TABLE IF EXISTS Players CASCADE;
DROP TABLE IF EXISTS Matches CASCADE;

DROP VIEW IF EXISTS counts CASCADE;
DROP VIEW IF EXISTS win_count CASCADE;
DROP VIEW IF EXISTS standings CASCADE;

-- create tables
create table Players (	ID serial primary key,
						Name text
);
create table Matches (	ID serial primary key,
						winner serial references Players(ID),
						loser serial references Players(ID)
);

-- create view to display the number of matches attended of each player
create view counts as
	select Players.ID as ID, count(Matches.ID) as matches_attended 
	from Players left join Matches
	on Players.ID = Matches.winner or Players.ID = Matches.loser
	group by Players.ID;

-- create view to display the number of matches winned of each player
create view win_count as
	select Players.ID, count(Matches.loser) as wins
	from Players left join Matches
	on Players.ID = Matches.winner
	group by Players.ID
	order by wins DESC;

-- create view for the info of each player (ID, Name, the number of winned, the number of matches attended)
create view standings as
	select Players.ID as id, Players.Name as name, wins, matches_attended as matches
	from Players, counts, win_count
	where Players.ID = counts.ID and Players.ID = win_count.ID
	order by wins DESC;

