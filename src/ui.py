import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 16)

    def draw_health_bar(self):
        # Draw the health bar (pixel art style)
        health_bar_rect = pygame.Rect(10, 10, 200, 20)  # Position and size
        pygame.draw.rect(self.screen, (255, 0, 0), health_bar_rect)  # Red background
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(10, 10, 150, 20))  # Green fill (example health)

    def draw_mana_bar(self):
        # Draw the mana bar (pixel art style)
        mana_bar_rect = pygame.Rect(10, 40, 200, 20)  # Position and size
        pygame.draw.rect(self.screen, (0, 0, 255), mana_bar_rect)  # Blue background
        pygame.draw.rect(self.screen, (0, 255, 255), pygame.Rect(10, 40, 100, 20))  # Cyan fill (example mana)

    def draw_player(self, x, y):
        # Draw player sprite (32x32 pixel block for now)
        player_color = (0, 255, 0)  # Green color for the player
        pygame.draw.rect(self.screen, player_color, pygame.Rect(x, y, 32, 32))  # Draw a rectangle as the player

    def draw_button(self, text, x, y, width, height):
        # Draw a button
        button_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(self.screen, (255, 255, 0), button_rect)  # Yellow button
        pygame.draw.rect(self.screen, (0, 0, 0), button_rect, 2)  # Black border

        # Add text on the button
        text_surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, (x + 5, y + 5))

