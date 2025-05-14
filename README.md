# Checkers Game with AI

This project is a Checkers game where you can play against an AI.

## How to Run

1.  **Make sure you have Python 3 and Pygame.**
    *   If you don't have Pygame, install it: `pip install pygame`
2.  **Open your terminal (like PowerShell or Command Prompt).**
3.  **Go to the project folder (`checkers` folder where `main.py` is).**
    ```powershell
    cd path\to\your\checkers_project_folder
    ```
4.  **Run the game:**
    ```powershell
    python main.py
    ```

## Code Layout

*   **`main.py`**: Starts and runs the game. Handles your mouse clicks and the AI's moves.
*   **`README.md`**: This file.
*   **`assets/` (folder)**:
    *   `crown.png`: Image for king pieces.
*   **`checkers/` (folder)**: Core game logic.
    *   `board.py`: Manages the game board and pieces on it.
    *   `constants.py`: Game settings like colors and sizes.
    *   `game.py`: Controls the game flow, turns, and rules.
    *   `piece.py`: Represents a single checker piece.
*   **`minimax/` (folder)**: AI logic.
    *   `algorithm.py`: Contains the Minimax algorithm the AI uses to decide moves.

*(You can generally ignore `__init__.py` files and `__pycache__` folders – they are for Python to organize the code.)*