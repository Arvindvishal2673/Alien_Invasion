# Alien Invasion 

A classic 2D space shooter game built with Python and Pygame. The player controls a spaceship at the bottom of the screen and must shoot down waves of incoming aliens.



---

##  How to Play

Your goal is to shoot down as many aliens as possible to get the highest score. The game ends if an alien hits your ship or reaches the bottom of the screen. You have three ships in total.

### Controls

* **Move Left:**  (Left Arrow Key)
* **Move Right:**  (Right Arrow Key)
* **Shoot:** **Spacebar**
* **Quit Game:** **Q**

---

##  Features

* Classic arcade-style gameplay.
* A scoring system that tracks your current and high score.
* Increasingly challenging waves of aliens.
* Sound effects for shooting and background music.
* A "Play" button to start and restart the game.

---
##  Tools and Technologies

* **Python:** The core programming language used for the game's logic.
* **Pygame:** A cross-platform set of Python modules designed for writing video games. It provides functionalities for graphics, sound, and user input.
* **cx_Freeze:** A tool used to package the Python script into a standalone executable file, making it easy to run the game on Windows without needing to install Python.

---

##  Installation and Setup

To run this game on your local machine, you'll need to have Python and the Pygame library installed.

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-directory>
    ```

2.  **Install Pygame:**
    ```bash
    pip install pygame
    ```

3.  **Run the game:**
    ```bash
    python alien_invasion.py
    ```

**Note:** Make sure all the asset files (`ship2.bmp`, `alien3.bmp`, `shot.mp3`, `track1.WAV`) are in the same directory as the Python scripts.

---

##  Project Structure

The project is organized into several modules, each handling a specific part of the game's logic:

* `alien_invasion.py`: This is the main driver of the game. It creates the game window, initializes all the game components (like the ship, aliens, and scoreboard), and contains the main game loop that processes events, updates game elements, and redraws the screen.

* `setting.py`: A configuration file that holds a `Setting` class. This class centralizes all the important variables of the game, such as the screen size, background color, ship speed, bullet properties, and alien speed. This makes it easy to tweak the game's behavior from one place.

* `ship.py`: Defines the `Ship` class, which is responsible for the player's spaceship. It handles loading the ship's image, positioning it on the screen, and managing its movement based on player input.

* `alien.py`: Defines the `Alien` class. This class manages the behavior of a single alien, including loading its image, setting its initial position, and updating its position as it moves across and down the screen.

* `bullets.py`: Contains the `Bullet` class. This class manages the bullets fired by the player's ship. It defines their appearance, speed, and direction of travel.

* `game_states.py`: This file contains the `Game_stats` class, which tracks real-time game statistics. It manages data like the player's score and the number of ships remaining. It also keeps track of the high score across game sessions.

* `scoreboard.py`: This module contains the `SCORING_SYSTEM` class, which is responsible for displaying the score, high score, and remaining ships on the screen. It renders this text information as images.

* `buttom.py`: (Note: filename might be a typo for `button.py`) This file defines the `Buttom` class, which creates the clickable "Play" button that appears on the screen when the game is not active, allowing the player to start a new game.

* `setup.py`: A utility script that uses the `cx_Freeze` library to package the game and all its assets into a standalone executable file for Windows. This allows the game to be run on computers that do not have Python or Pygame installed.
