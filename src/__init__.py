import os

# Define project directory structure
dirs = [
    "src",
    "src/assets",
    "src/assets/characters",
    "src/assets/backgrounds",
    "src/assets/ui",
    "src/assets/items"
]

# Define files to create in the src directory
files = [
    "src/__init__.py",
    "src/main.py",
    "src/game.py",
    "src/ui.py",
    "src/combat.py",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

# Define content to write into files
file_contents = {
    "requirements.txt": "pygame==2.1.0\n",
    "README.md": """
# Pixelated RPG Game

An Adventure RPG game with pixel art UI and gameplay. This game includes character creation, combat, and exploration, all done in a retro, pixelated style.

## Features
- 32-bit Pixel art character.
- Pixelated health and mana bars.
- Basic turn-based combat.
- Exploration and basic interaction.

## How to Run
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the game: `python src/main.py`
    """,
    ".gitignore": "__pycache__/\n*.pyc\n.DS_Store\n.idea/\n.vscode/\n"
}

# Create directories
for directory in dirs:
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory {directory} created")

# Create files and add basic content
for file in files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            # If file has defined content, write it
            if file in file_contents:
                f.write(file_contents[file])
            print(f"File {file} created")

# Create basic content for src/main.py
with open("src/main.py", "w") as f:
    f.write("""
import pygame
from src.game import Game

def main():
    pygame.init()

    # Game settings
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pixelated RPG Game")
    
    # Create game object
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
    """)
print("Project initialization complete!")

