
# Snake Game Project

This is a simple Snake Game implemented in Python using the turtle module. The game involves controlling a snake to eat food while avoiding collision with walls and itself. Each time the snake eats food, it grows longer and the player's score increases.


## Features

🐍Snake Movement: Use arrow keys to control the snake's direction (Up, Down, Left, Right).

🍊Food Generation: Randomly placed food on the screen that the snake eats.

📑Scoreboard: Displays the current score and the high score.

🔝High Score Tracking: Stores the high score in a text file (data.txt) that persists between game sessions.

👉Collision Detection: Ends the game if the snake hits the wall or itself, and resets the game.




## How to Run

1. Clone this repository to your local machine.

2. Ensure you have Python installed (preferably version 3.6 or higher).

3. Run the main.py file to start the game:
    pythonmain.py

4. Use the arrow keys to control the snake and start playing.
## File Structure

Snake_Game_Project/

├── food.py          # Manages the food creation and                  random positioning.

├── main.py          # Main game logic and event listeners.

├── scoreboard.py    # Handles scoring and high score persistence.

├── snake.py         # Implements snake behavior and controls.

├── data.txt         # Stores the high score.
## Dependencies

✔️Python: Make sure Python is installed on your system.

✔️turtle: Comes pre-installed with Python, so no additional installation is required.

✔️random: Python's built-in library for random number generation.


## Code Explanation


🍊food.py

Handles the food creation and positioning:

Uses a small blue dot as food.

Randomly places the food on the screen whenever it is eaten.

🧑‍💻main.py

Controls the overall game loop and screen setup:

Initializes the screen, snake, food, and scoreboard.

Sets up keyboard listeners for snake movement.

Contains the main game loop for collision detection and game updates.


📑scoreboard.py

Manages scoring and high score tracking:

Displays the current score and the high score.

Updates the high score in data.txt after each game.

🐍snake.py

Implements the snake's behavior:

Creates the snake and handles its movement.

Detects collisions and resets the game when necessary.

Grows the snake when it eats food.
## Controls

👆Up: Move the snake upward.

👇Down: Move the snake downward.

👈Left: Move the snake to the left.

👉Right: Move the snake to the right. 


![image alt](https://github.com/AkshitMunjal/Snake_Game_Python/blob/a3f6dbd98724d5439ab2dc6ce5019c2caa4d464a/Snake_Game.png)


