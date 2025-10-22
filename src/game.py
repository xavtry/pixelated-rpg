import pygame
from src.ui import UI

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.ui = UI(self.screen)

        # Initial position of player
        self.player_x = 400
        self.player_y = 300
        self.player_width = 32
        self.player_height = 32

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        # Move player (simple WASD movement)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x -= 5
        if keys[pygame.K_RIGHT]:
            self.player_x += 5
        if keys[pygame.K_UP]:
            self.player_y -= 5
        if keys[pygame.K_DOWN]:
            self.player_y += 5

    def draw(self):
        self.screen.fill((0, 0, 0))  # Black background
        self.ui.draw_health_bar()
        self.ui.draw_mana_bar()
        self.ui.draw_player(self.player_x, self.player_y)
        pygame.display.update()

