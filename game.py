###############################
## Author: TRAN Quang Toan   ##
## Project Game of Life      ##
## Version 1                 ##
## 13 Apr 2020               ##
###############################

import pygame
from define import *
from ft_lib import *
from board import *
from operations import *

class Game():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH + SCREEN_WIDTH//2, SCREEN_HEIGHT))
		self.right_menu = pygame.Surface((SCREEN_WIDTH//2,SCREEN_HEIGHT))
		self.right_menu.fill(BLACK)
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont("comicsansms", 30)
		
		self.CodeInput()

		opt = self.Play()
		self.Game_Over(opt)

		pygame.quit()


	def CodeInput(self):
		self.board = Board(self.screen)
		self.right = RIGHT()
		self.down = DOWN()
		self.up = UP()
		self.left = LEFT()

		self.OPS = {
			"up": self.up,
			"down": self.down,
			"left": self.left,
			"right": self.right
		}

		self.code = ["down", "left", "f1"]
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
						self.board.ar[p[0]][p[1]] = -1
			
			self.screen.fill(WHITE)
			self.screen.blit(self.right_menu, (SCREEN_WIDTH, 0))
			self.board.draw2()

			pygame.display.flip()
			self.clock.tick(3)

	def Play(self):	
		
		# self.board.init_level_test()
		self.board.init_level_1()
		self.list_actions = []
		if is_in_list(self.code, "f1"):
			flag = True
		else:
			self.get_list()
			flag = False
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
						self.board.ar[p[0]][p[1]] = -1
			
			if opt:
				if flag:
					self.get_list()
				if len(self.list_actions) == 0:
					opt = False
					return -1
				else:
					op = self.list_actions.pop(0)
					self.board.p = self.OPS[op].run(self.board.ar, self.board.p)
					if self.board.p == ():
						return -1
					elif self.board.p == self.board.P:
						return 1

			self.screen.fill(WHITE)
			self.screen.blit(self.right_menu, (SCREEN_WIDTH, 0))
			self.board.draw()

			pygame.display.flip()
			self.clock.tick(3)

	def get_list(self):
		for i in range(len(self.code)):
			if self.code[i] == "f1":
				for j in [k for k in self.code[:i]]:
					self.list_actions.append(j)
			else:
				self.list_actions.append(self.code[i])

	def Game_Over(self, opt):
		if opt == -1:
			txt = "-= Never Give Up =-"
		elif opt == 1:
			txt = "-= Level Up! =-"
		else:
			txt = "-= T =-"
		txt = self.font.render(txt, True, GREEN)
		txt_center = (
            SCREEN_WIDTH + SCREEN_WIDTH//4 - txt.get_width() // 2,\
				 50 - txt.get_height() // 2
        )
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]:
						p = rev_rect(pygame.mouse.get_pos())
						self.board.ar[p[0]][p[1]] = -1
			self.screen.fill(WHITE)
			# self.right_menu.blit(txt, (SCREEN_WIDTH//4 - txt.get_width(), 50 - txt.get_height()//2))
			self.screen.blit(self.right_menu, (SCREEN_WIDTH, 0))
			self.board.draw()
			self.screen.blit(txt, txt_center)
			pygame.display.flip()
			self.clock.tick(2)


if __name__ == '__main__':
	Game()