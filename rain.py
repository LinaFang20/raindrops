import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
	"""A class to manage rain drops."""

	def __init__ (self, rd_game):
		"""Initialize the rain drop and set its starting position."""
		super().__init__()

		self.screen = rd_game.screen
		###self.settings = rd_game.settings
		###self.screen_rect = rd_game.screen.get_rect()

		# Load the rain drop image and get its rect.
		self.image = pygame.image.load('images/rain.bmp')
		self.rect = self.image.get_rect()

		#Start each new rain drop near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the star's exact vertical position.
		self.y = float(self.rect.y)