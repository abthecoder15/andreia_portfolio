# EpicCross Quest

## Description
Welcome to our team's collaborative project! We have built a crossy road game, where you navigate your way through levels, dodging traffic and racing against the clock. Earn points as time ticks down, facing 'Game Over' upon a misstep or a triumphant 'Congratulations' upon success. Conquer each level for a chance to bask in the 'Winner' screen. With an engaging soundtrack, it's a thrilling test of skill and strategy.

## Meet the Team
Our diverse team of dedicated individuals:

### Adele Davies
   - **Skills**: Great communicator and Builds relationships easily.
   - **Interests**: Fibre crafting like crochet, spinning, felting and lace-making, TTRPG, LARP and Going to gigs

### Andreia Byda
   - **Skills**: HTML, CSS, JavaScript, Python and MySQL.
   - **Interests**: Reading, Writing, Baking and DIY.

### Barakat Adesokan
   - **Skills**: HTML, SQL, Postman, Selenium and Pastry Making.
   - **Interests**: Reading and Travelling.

### Ilhan Farah
   - **Skills**: HTML, CSS, JavaScript, Python, MySQL.
   - **Interests**: Art and Sustainability.
   
### Vithursana Somasundaram
   - **Skills**: HTML, CSS, JavaScript, Python and MySQL.
   - **Interests**: Reading, Crocheting and Gym.
   
=======
## Table of Contents

- [Features](#features)
- [Installation Requirements](#installation-requirements)
- [Database Setup and Management](#database-setup-and-management)
- [Usage](#usage)


## Features

- Registration system: Allows users to register with unique usernames and hashed passwords.
- Login: Provides a secure login system for registered users.
- Character options: Allows user to play with selected character (four to choose from).
- Gameplay: Implements game levels, from Easy, to Medium and Hard. 
- Sound Effects: Incorporates sound effects for an immersive experience.
- Scoring system: Tracks and updates higher scores for each level and total higher score (SQL connection)
- Countdown timer: For the different levels.
- Moves using arrow keys on the keyboard- left, right, up and down keys


## Installation Requirements

1. **Python**: Ensure you have Python installed on your computer. If not, you can download it from the [official Python website](https://www.python.org/).

2. **MySQL Workbench**: Ensure you have MySQL Workbench installed on your computer. If not, you can download it [here](https://dev.mysql.com/downloads/workbench/)

3. **Check other requirements** You can find the project's dependencies in the **[requirements.txt](requirements.txt)** file.


## Database Setup and Management

1. Database Initialization:

   - Open **crossy_road.sql** in MySQL Workbench and run all the commands to set up the database.
   

2. Environment Setup:

   - Execute **db_utils.py** in your IDE to properly configure and initialize the environment for database connections.


3. Database Configuration:

Once you have opened all the files in your IDE:

1. Edit the following variables in **'config.py'** with your MySQL database connection details:

```bash
  DBConfig = {
    'host': '',
    'user': '',
    'password': '',
    'database': 'crossy_road'
}
```
2. Save the **'config.py'** file.


## Usage

1. Finally, run **main.py** to execute the program. You'll be welcomed with a screen prompt. Press Enter to proceed.


2. On the next screen, choose between **Register** or **Login**.

- If **Register** is selected, input a username and password, then press Enter. Proceed to Login after registration.

- If **Login** is chosen, input your username and password, then press Enter to proceed.

3. After logging in, a character selection screen appears. Choose a character by moving the arrow keys and level 1 will start with selected character.
If no character is selected after 10 seconds, a default character will be applied.

**Game Levels and Points:**
- The game initiates at Level 1 (Easy) with 30 seconds and 30 available points.
- Level 2 (Medium) follows with 20 seconds and 20 available points.
- Level 3 (Hard) concludes the game with 10 seconds and 10 available points.

**Point System:**
- Points decrease in sync with the timer. Longer time taken to cross results in lower scores.

**Game Flow:**
- If hit by a car or time runs out, a **Game Over** screen appears with a corresponding sound. Press Enter to try again.
- Successfully crossing displays a **Congratulations** screen with the current score and a cheerful sound.
- After crossing on Level 3, a **Winner** screen shows your **Total score** for all levels and a cheerful sound plays.
- The **background sound** plays throughout the game.