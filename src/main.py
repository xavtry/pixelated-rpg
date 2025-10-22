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

