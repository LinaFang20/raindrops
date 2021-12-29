import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
	"""A class to manage rain drops."""

	def __init__ (self, rd_game):
		"""Initialize the rain drop and set its starting position."""
		super().__init__()

		self.screen = rd_game.screen
		self.settings = rd_game.settings
		self.screen_rect = rd_game.screen.get_rect()

		# Load the rain drop image and get its rect.
		self.image = pygame.image.load('images/rain.bmp')
		self.rect = self.image.get_rect()

		#Start each new rain drop near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Store the star's exact vertical position.
		self.y = float(self.rect.y)

	def check_bottom (self):
		"""Return True if rain is at the bottom of the screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >screen_rect.bottom:
			return True
		else:
			return False

	def update (self):
		"""Move the rain drops towards bottom."""
		self.y += self.settings.rain_drop_speed
		self.rect.y = self.y