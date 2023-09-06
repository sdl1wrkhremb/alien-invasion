import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and get its rect attribute.
        self.image = pygame.image.load('images/enemy.png')
        self.rect = self.image.get_rect()

        # Start each new alien near the top of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store a float for the alien's exact horizontal position.
        self.x = float(self.rect.x)