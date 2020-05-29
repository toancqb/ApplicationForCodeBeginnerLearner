###############################
## Author: TRAN Quang Toan   ##
## Project APP_4_0_CODE      ##
## Version 1                 ##
## 13 Apr 2020               ##
###############################

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

	def draw(self, dir):
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
				# if self.ar[x][y] == 1:
				# 	pygame.draw.rect(self.screen, ORANGE, (x*CELL,y*CELL, CELL, CELL))
				# 	pygame.draw.rect(self.screen, BLACK, (x*CELL+1,y*CELL+1, CELL-2, CELL-2))
				if self.ar[x][y] == 2:
					pygame.draw.rect(self.screen, GRIS, (x*CELL,y*CELL, CELL, CELL))
					pygame.draw.rect(self.screen, RED_B, (x*CELL+1,y*CELL+1, CELL-2, CELL-2))
				# elif self.ar[x][y] == 3:
				# 	pygame.draw.rect(self.screen, BLACK, (x*CELL,y*CELL, CELL, CELL))
				# 	pygame.draw.rect(self.screen, ORANGE, (x*CELL+1,y*CELL+1, CELL-2, CELL-2))
				elif self.ar[x][y] == -1:
					pygame.draw.rect(self.screen, BLUE, (x*CELL,y*CELL, CELL, CELL))
					#pygame.draw.rect(self.screen, GRIS_B, (x*CELL+1,y*CELL+1, CELL-2, CELL-2))
		
		if self.P != ():
			pygame.draw.rect(self.screen, BLACK, (self.P[0]*CELL,self.P[1]*CELL, CELL, CELL))
			pygame.draw.rect(self.screen, ORANGE, (self.P[0]*CELL+1,self.P[1]*CELL+1, CELL-2, CELL-2))
		if self.p != ():
			# pygame.draw.rect(self.screen, ORANGE, (self.p[0]*CELL,self.p[1]*CELL, CELL, CELL))
			# pygame.draw.rect(self.screen, BLACK, (self.p[0]*CELL+1,self.p[1]*CELL+1, CELL-2, CELL-2))
			draw_player(self.screen, self.p, dir)

	def init_arena(self):
		self.ar = [[ -1 for i in range(PY)] for i in range(PX)]

	def init_level_test(self):
		self.init_arena()
		self.op_max = 2
		tx, ty = 4, 2
		self.ar[tx+6][ty+2] = 2
		self.ar[tx+6][ty+3] = 2
		self.ar[tx+6][ty+4] = 2
		self.ar[tx+6][ty+5] = 2
		self.ar[tx+6][ty+6] = 2
		self.ar[tx+6][ty+7] = 0
		self.ar[tx+6][ty+8] = 2
		self.ar[tx+6][ty+9] = 2
		self.ar[tx+6][ty+10] = 2
		##
		self.p = (tx+6, ty+2)
		self.P = (tx+6, ty+10)

	def init_level_1(self):
		self.init_arena()
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
		self.p = (tx+6, ty+2)
		self.P = (tx+6, ty+10)
		return ("10", False)

	def init_level_2(self):
		self.init_arena()
		self.op_max = 5
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
		self.p = (tx+6,ty+2)
		self.P = (tx+2,ty+6)
		return ("10", False)

	def init_level_3(self):
		self.init_arena()
		self.op_max = 6
		tx, ty = 4, 2
		self.ar[tx+1][ty+1] = 0
		self.ar[tx+1][ty+2] = 0
		self.ar[tx+1][ty+3] = 0
		self.ar[tx+2][ty+3] = 0
		self.ar[tx+2][ty+4] = 0
		self.ar[tx+3][ty+4] = 0
		self.ar[tx+3][ty+5] = 0
		self.ar[tx+3][ty+6] = 0
		self.ar[tx+4][ty+6] = 0
		self.ar[tx+4][ty+7] = 0
		self.ar[tx+5][ty+7] = 0
		self.ar[tx+5][ty+8] = 0
		self.ar[tx+5][ty+9] = 0
		self.ar[tx+6][ty+9] = 0
		self.ar[tx+6][ty+10] = 0
		self.ar[tx+7][ty+10] = 0

		##
		self.p = (tx+1,ty+1)
		self.P = (tx+7,ty+10)
		return "10"

	def init_level_4(self):
		self.init_arena()
		self.op_max = 7
		tx, ty = 4, 2
		self.ar[tx+1][ty+1] = 0
		self.ar[tx+2][ty+1] = 0
		self.ar[tx+3][ty+1] = 0
		self.ar[tx+3][ty+2] = 0
		self.ar[tx+3][ty+3] = 0
		self.ar[tx+2][ty+3] = 0
		self.ar[tx+2][ty+4] = 0
		self.ar[tx+3][ty+4] = 0
		self.ar[tx+4][ty+4] = 0
		self.ar[tx+4][ty+5] = 0
		self.ar[tx+4][ty+6] = 0
		self.ar[tx+3][ty+6] = 0
		self.ar[tx+3][ty+7] = 0
		##
		self.p = (tx+1,ty+1)
		self.P = (tx+3,ty+7)
		return "01"

	def init_level_5(self):
		self.init_arena()
		self.op_max = 7
		tx, ty = 4, 4
		self.ar[tx+1][ty+1] = 0
		self.ar[tx+2][ty+1] = 0
		self.ar[tx+1][ty+2] = 0
		self.ar[tx+2][ty+2] = 0
		self.ar[tx+1][ty+3] = 0
		self.ar[tx+2][ty+3] = 0
		self.ar[tx+3][ty+3] = 0
		self.ar[tx+4][ty+3] = 0
		self.ar[tx+3][ty+4] = 0
		self.ar[tx+4][ty+4] = 0
		self.ar[tx+3][ty+5] = 0
		self.ar[tx+4][ty+5] = 0
		##
		self.p = (tx+1,ty+1)
		self.P = (tx+4,ty+5)
		return ("10", False)

	def init_level_6(self):
		self.init_arena()
		self.op_max = 6
		tx, ty = 2, 2
		
		for x in range(PX-3):
			for y in range(PY-6):
				self.ar[tx+x][ty+y] = 0 
		##
		self.ar[tx][ty] = 0
		self.p = (tx,ty)
		self.ar[tx+PX-4][ty+PY-7] = 0
		self.P = (tx+PX-4,ty+PY-7)
		return ("10", False)

	def init_level_7(self):
		self.init_arena()
		self.op_max = 9
		tx, ty = 8, 2
		self.ar[tx+1][ty+1] = 0
		self.ar[tx+2][ty+1] = 0
		self.ar[tx+2][ty+2] = 0
		self.ar[tx+2][ty+3] = 0
		self.ar[tx+1][ty+3] = 0
		self.ar[tx+2][ty+4] = 0
		self.ar[tx+2][ty+5] = 0
		self.ar[tx+1][ty+5] = 0
		self.ar[tx+2][ty+6] = 0
		self.ar[tx+2][ty+7] = 0
		self.ar[tx][ty+1] = 0
		self.ar[tx][ty+2] = 0
		self.ar[tx][ty+3] = 0
		self.ar[tx][ty+4] = 0
		self.ar[tx][ty+5] = 0
		self.ar[tx][ty+6] = 0
		self.ar[tx][ty+7] = 0
		self.ar[tx+1][ty+7] = 0
		##
		self.p = (tx+1,ty+1)
		self.P = (tx+1,ty+7)
		return ("11", False)

	def init_level_8(self):
		self.init_arena()
		self.op_max = 3
		tx, ty = 3, 2
		self.ar[tx+5][ty+1] = 0
		self.ar[tx+5][ty+2] = 0
		self.ar[tx+5][ty+3] = 0
		self.ar[tx+5][ty+4] = 0
		self.ar[tx+5][ty+5] = 0
		self.ar[tx+5][ty+6] = 0
		self.ar[tx+5][ty+7] = 0
		self.ar[tx+5][ty+8] = 2
		self.ar[tx+6][ty+8] = 0
		self.ar[tx+7][ty+8] = 0
		##
		self.p = (tx+5,ty+1)
		self.P = (tx+7,ty+8)
		return ("10", True)
	
	def init_level_9(self):
		self.init_arena()
		self.op_max = 6
		tx, ty = 3, 2
		self.ar[tx+1][ty+1] = 0
		self.ar[tx+1][ty+2] = 0
		self.ar[tx+2][ty+2] = 0
		self.ar[tx+2][ty+3] = 0
		self.ar[tx+3][ty+3] = 0
		self.ar[tx+3][ty+4] = 0
		self.ar[tx+4][ty+4] = 0
		self.ar[tx+4][ty+5] = 0
		self.ar[tx+5][ty+5] = 0
		self.ar[tx+5][ty+6] = 0
		self.ar[tx+6][ty+6] = 0
		self.ar[tx+6][ty+7] = 2
		self.ar[tx+7][ty+7] = 0
		self.ar[tx+8][ty+7] = 0
		self.ar[tx+9][ty+7] = 0
		self.ar[tx+10][ty+7] = 0
		self.ar[tx+11][ty+7] = 0
		self.ar[tx+12][ty+7] = 0
		##
		self.p = (tx+12,ty+7)
		self.P = (tx+1,ty+1)
		return ("11", True)