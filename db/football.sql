CREATE USER football;
CREATE DATABASE football;
GRANT ALL PRIVILEGES ON DATABASE football TO football;

\c football football

DROP TABLE IF EXISTS fixtures;
DROP TABLE IF EXISTS leagues;
DROP TABLE IF EXISTS teams;

CREATE TABLE leagues(
id INT4 PRIMARY KEY,
name VARCHAR(255) NOT NULL,
country VARCHAR(255),
country_code VARCHAR(255),
season VARCHAR(255),
season_start VARCHAR(255),
season_end VARCHAR(255),
logo VARCHAR(255),
flag VARCHAR(255),
standings BOOLEAN
);

CREATE TABLE teams(
id INT4 PRIMARY KEY,
name VARCHAR(255) NOT NULL,
code VARCHAR(255),
logo VARCHAR(255)
);

CREATE TABLE fixtures(
id INT4 PRIMARY KEY,
event_date VARCHAR(255) NOT NULL,
event_timestamp VARCHAR(255) NOT NULL,
league INT4 REFERENCES leagues(id) NOT NULL,
round TEXT,
home_team INT4 REFERENCES teams(id) NOT NULL,
away_team INT4 REFERENCES teams(id) NOT NULL,
status VARCHAR(255),
status_short VARCHAR(255),
goals_home_team INT4 NOT NULL,
goals_away_team INT4 NOT NULL,
halftime_score VARCHAR(255) NOT NULL,
final_score VARCHAR(255) NOT NULL,
penalty VARCHAR(255), 
elapsed INT4
);

-- ALTER TABLE leagues
-- ADD country VARCHAR(255),
-- ADD country_code VARCHAR(255),
-- ADD season VARCHAR(255),
-- ADD season_start VARCHAR(255),
-- ADD season_end VARCHAR(255),
-- ADD logo VARCHAR(255),
-- ADD flag VARCHAR(255),
-- ADD standings BOOLEAN;

-- ALTER TABLE teams
-- ADD code VARCHAR(255),
-- ADD logo VARCHAR(255)


        -- "fixture_id": "2839",
        -- "event_timestamp": "1534185000",
        -- "event_date": "2018-08-13T18:30:00+00:00",
        -- "league_id": "9",
        -- "round": "2. Bundesliga - 2",
        -- "homeTeam_id": "192",
        -- "awayTeam_id": "182",
        -- "homeTeam": "FC Koln",
        -- "awayTeam": "Union Berlin",
        -- "status": "Match Finished",
        -- "statusShort": "FT",
        -- "goalsHomeTeam": "1",
        -- "goalsAwayTeam": "1",
        -- "halftime_score": "1 - 0",
        -- "final_score": "1 - 1",
        -- "penalty": null,
        -- "elapsed": "93",
        -- "firstHalfStart": "1534185060",
        -- "secondHalfStart": "1534188780"
 

-- \COPY articles(id,link) FROM './data/top_stories.csv' DELIMITER ',' CSV HEADER;
-- SELECT count(*) from articles;

-- \COPY articles TO './full_data_top_stories.csv' WITH (FORMAT CSV, HEADER);
-- docker cp 2e14fd6a0fd1:/full_data_top_stories.csv ./server/db

-- ALTER TABLE articles
-- ALTER COLUMN engagedMinutes TYPE real;

-- ALTER TABLE articles
-- ADD wordCount INT4;
-- ADD views INT4,
-- ADD visits INT4,
-- ADD recirc INT4,
-- ADD engaged INT4;

-- alter role football WITH PASSWORD 'FBmodel1';
-- ALTER TABLE articles
-- ADD relativeReadingTime REAL;

-- SELECT ROUND(AVG(score)) FROM articles WHERE author = 4411;--
-- SELECT AVG(wordCount) FROM articles;

-- SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'articles';

-- Articles written by authors
-- SELECT
--   authors.*,
--   count(articles.author) as number_of_articles
-- FROM authors
-- LEFT JOIN articles
-- ON (authors.id = articles.author)
-- GROUP BY authors.id
-- ORDER BY number_of_articles DESC;