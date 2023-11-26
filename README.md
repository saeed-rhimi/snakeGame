
# Classic Snake Game in Python

Welcome to the repository of a classic snake game implemented in Python using the Turtle graphics library. This project is a fun and interactive recreation of the iconic snake game. It's designed to be easy to understand and play, making it perfect for both beginners and experienced Python developers looking to revisit a classic.

## Features

- **Responsive Snake Movement:** Control the snake using keyboard inputs. The snake moves smoothly and responds promptly to turn commands.
- **Random Food Generation:** The game randomly places food items on the screen, challenging players to navigate and grow the snake.
- **Score Tracking:** Your current score increases as you eat food, and the high score is tracked and saved across game sessions.
- **Collision Detection:** The game ends if the snake collides with the wall or its own body, at which point a game over message is displayed.

## Components

- `main.py`: Sets up the game environment and contains the main game loop.
- `snake.py`: Defines the Snake class, managing its behavior, movement, and growth.
- `food.py`: Manages the appearance and placement of the food item in the game.
- `scoreboard.py`: Handles the display of the current and high scores, as well as the game over message.

## Prerequisites

To run this game, you will need Python installed on your computer. The game uses the Python Turtle module for graphics, which is a standard library in Python, so no additional installations are required.

## Installation

Clone this repository to your local machine using the following command:

```
git clone https://github.com/saeed-rhimi/snakeGame
```

Navigate to the directory where you cloned the repo and run the game:

```
cd snakeGame
python main.py
```

## How to Play

- Run `main.py` to start the game.
- Use the arrow keys on your keyboard to control the direction of the snake.
- Guide the snake to the food items. Each food item eaten will increase your score and extend the length of the snake.
- Avoid colliding with the walls or the snake's own body.
- Try to score as high as possible!

## Contributing

Contributions to improve the game or add new features are always welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

Special thanks to the Python and Turtle graphics communities for their valuable resources and support.
