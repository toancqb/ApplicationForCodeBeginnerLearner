import pygame
from define import *
from operations import *
from ft_lib import *

class Board():
	def __init__(self, screen):
		self.screen = screen
		self.init_arena()
		self.st = [(1,1)]
		self.op_max = 3

	def draw2(self):
		for i in range(PX):
			if i % 9 == 0:
				color = GRIS
			else:
				color = GRIS_B
			pygame.draw.line(self.screen, color, (i*CELL, 0), (i*CELL, SCREEN_HEIGHT))
		for i in range(PY):
			if i % 9 == 0:
				color = GRIS
			else:
				color = GRIS_B
			pygame.draw.line(self.screen, color, (0, i*CELL), (SCREEN_WIDTH, i*CELL))

		
	def draw(self):
		for i in range(PX):
			if i % 9 == 0:
				color = GRIS
			else:
				color = GRIS_B
			pygame.draw.line(self.screen, color, (i*CELL, 0), (i*CELL, SCREEN_HEIGHT))
		for i in range(PY):
			if i % 9 == 0:
				color = GRIS
			else:
				color = GRIS_B
			pygame.draw.line(self.screen, color, (0, i*CELL), (SCREEN_WIDTH, i*CELL))

		for y in range(PY):
			for x in range(PX):
				if self.ar[x][y] == 1:
					pygame.draw.rect(self.screen, ORANGE, (x*CELL,y*CELL, CELL, CELL))
					pygame.draw.rect(self.screen, BLACK, (x*CELL+1,y*CELL+1, CELL-2, CELL-2))
				elif self.ar[x][y] == 2:
					pygame.draw.rect(self.screen, BLACK, (x*CELL,y*CELL, CELL, CELL))
					pygame.draw.rect(self.screen, GREEN, (x*CELL+1,y*CELL+1, CELL-2, CELL-2))
				elif self.ar[x][y] == 3:
					pygame.draw.rect(self.screen, BLACK, (x*CELL,y*CELL, CELL, CELL))
					pygame.draw.rect(self.screen, ORANGE, (x*CELL+1,y*CELL+1, CELL-2, CELL-2))
				elif self.ar[x][y] == -1:
					pygame.draw.rect(self.screen, GRIS_B, (x*CELL,y*CELL, CELL, CELL))
					#pygame.draw.rect(self.screen, GRIS_B, (x*CELL+1,y*CELL+1, CELL-2, CELL-2))

	def init_arena(self):
		self.ar = [[ -1 for i in range(PY)] for i in range(PX)]

	def init_level_test(self):
		tx, ty = 4, 2
		self.ar = [[ 0 for i in range(PY)] for i in range(PX)]
		##
		self.ar[tx+6][ty+2] = 1
		self.p = (tx+6,ty+2)
		self.ar[tx+2][ty+6] = 3
		self.P = (tx+2,ty+6)

	def init_level_1(self):
		self.op_max = 2
		tx, ty = 4, 2
		self.ar[tx+6][ty+2] = 0
		self.ar[tx+6][ty+3] = 0
		self.ar[tx+6][ty+4] = 0
		self.ar[tx+6][ty+5] = 0
		self.ar[tx+6][ty+6] = 0
		self.ar[tx+6][ty+7] = 0
		self.ar[tx+6][ty+8] = 0
		self.ar[tx+6][ty+9] = 0
		self.ar[tx+6][ty+10] = 0
		##
		self.ar[tx+6][ty+2] = 1
		self.p = (tx+6,ty+2)
		self.ar[tx+6][ty+10] = 3
		self.P = (tx+6,ty+10)

	def init_level_2(self):
		self.op_max = 3
		tx, ty = 4, 2
		self.ar[tx+6][ty+2] = 0
		self.ar[tx+6][ty+3] = 0
		self.ar[tx+5][ty+3] = 0
		self.ar[tx+5][ty+4] = 0
		self.ar[tx+4][ty+4] = 0
		self.ar[tx+4][ty+5] = 0
		self.ar[tx+3][ty+5] = 0
		self.ar[tx+3][ty+6] = 0
		self.ar[tx+2][ty+6] = 0
		##
		self.ar[tx+6][ty+2] = 1
		self.p = (tx+6,ty+2)
		self.ar[tx+2][ty+6] = 3
		self.P = (tx+2,ty+6)

	def init_level_3(self):
		self.op_max = 3
		tx, ty = 4, 2
		self.ar[tx+6][ty+2] = 0
		self.ar[tx+6][ty+3] = 0
		self.ar[tx+5][ty+3] = 0
		self.ar[tx+5][ty+4] = 0
		self.ar[tx+4][ty+4] = 0
		self.ar[tx+4][ty+5] = 0
		self.ar[tx+3][ty+5] = 0
		self.ar[tx+3][ty+6] = 0
		self.ar[tx+2][ty+6] = 0
		##
		self.ar[tx+6][ty+2] = 1
		self.p = (tx+6,ty+2)
		self.ar[tx+2][ty+6] = 3
		self.P = (tx+2,ty+6)

