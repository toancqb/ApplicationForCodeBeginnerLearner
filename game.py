###############################
## Author: TRAN Quang Toan   ##
## Project Game of Life      ##
## Version 1                 ##
## 13 Apr 2020               ##
###############################

import pygame
from define import *
from ft_lib import *

class Board():
	def __init__(self, screen):
		self.screen = screen
		self.init_arena()
		self.st = [(1,1)]

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
					pygame.draw.rect(self.screen, BLACK, (x*CELL,y*CELL, CELL, CELL))
					pygame.draw.rect(self.screen, BLUE, (x*CELL+1,y*CELL+1, CELL-2, CELL-2))

	def init_arena(self):
		self.ar = [[ 0 for i in range(PY)] for i in range(PX)]
		self.ar[1][1] = 1
		self.ar[PX-2][PY-2] = 3

	def process(self):
		#x, y = self.st.pop(len(self.st)-1)
		x, y = self.st.pop(0)
		index = [(-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1)]
		for i in index:
			nx, ny = x+i[0], y+i[1]
			if check_valid(nx, ny):
				if self.ar[nx][ny] == 0:
					self.st.append((nx,ny))
					self.ar[nx][ny] = 2
					return 0
				elif self.ar[nx][ny] == 3:
					return 1
		return 0
		
class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH + 100, SCREEN_HEIGHT))
		# self.screen.fill(GRIS_B)
		right_menu = pygame.Surface((100,SCREEN_HEIGHT))
		right_menu.fill(GRIS_B)
		self.clock = pygame.time.Clock()
		board = Board(self.screen)
		opt = False
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					if event.key == pygame.K_SPACE:
						opt = True
				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]:
						p = rev_rect(pygame.mouse.get_pos())
						board.ar[p[0]][p[1]] = -1
			self.screen.fill(WHITE)
			self.screen.blit(right_menu, (SCREEN_WIDTH, 0))
			board.draw()
			# if opt and board.process() == 1:
			# 	opt = False
			if opt:
				RIGHT().run()

			pygame.display.flip()
			self.clock.tick(20)

		pygame.quit()


if __name__ == '__main__':
	Game()