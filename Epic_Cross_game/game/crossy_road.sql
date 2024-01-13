-- Create database
CREATE DATABASE IF NOT EXISTS crossy_road;

-- Use database
USE crossy_road;

-- Table to store player information
CREATE TABLE Players (
    PlayerID INT PRIMARY KEY AUTO_INCREMENT,
    Username VARCHAR(255) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    HigherScoreLevel1 INT DEFAULT 0,
    HigherScoreLevel2 INT DEFAULT 0,
    HigherScoreLevel3 INT DEFAULT 0,
    TotalHigherScore INT DEFAULT 0
);

-- Table to store game levels
CREATE TABLE GameLevels (
    LevelID INT PRIMARY KEY,
    LevelName VARCHAR(50) NOT NULL,
    TimerSeconds INT CHECK (TimerSeconds > 0)
);


-- Inserting game Levels (difficulty levels)
INSERT INTO GameLevels (LevelID, LevelName, TimerSeconds)
VALUES (1, 'Easy', 30);  -- 30 seconds timer for easy mode

INSERT INTO GameLevels (LevelID, LevelName, TimerSeconds)
VALUES (2, 'Medium', 20);  -- 20 seconds timer for medium mode

INSERT INTO GameLevels (LevelID, LevelName, TimerSeconds)
VALUES (3, 'Hard', 10);  -- 10 seconds timer for hard mode
