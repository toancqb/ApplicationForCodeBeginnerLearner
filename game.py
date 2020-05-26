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
		self.screen = pygame.display.set_mode((SCREEN_WIDTH + SCREEN_WIDTH, SCREEN_HEIGHT))
		self.right_menu = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
		self.right_menu.fill(BLACK)
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont("comicsansms", 30)
		self.font2 = pygame.font.SysFont("comicsansms", 25)


		self.right = RIGHT()
		self.down = DOWN()
		self.up = UP()
		self.left = LEFT()

		self.OPS = {
			"UP": self.up,
			"DOWN": self.down,
			"LEFT": self.left,
			"RIGHT": self.right
		}
		self.board = Board(self.screen)
		self.group_button = []
		self.group_solution = []
		self.init_buttons()
		self.group_level = [self.board.init_level_1,self.board.init_level_2,\
			self.board.init_level_3,self.board.init_level_4,self.board.init_level_5,\
				self.board.init_level_6,self.board.init_level_7]

		level = 0
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					break
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						break
			if level == len(self.group_level):
				break
			self.group_level[level]()
			
			self.init_solution()
		
			self.CodeInput()

			opt = self.Play()
			opt2 = self.Game_Over(opt)
			if opt2 == -1:
				continue
			elif opt2 == -2:
				running = False
			level += 1

		pygame.quit()

	def init_buttons(self):
		norm = SCREEN_WIDTH+SCREEN_WIDTH//4
		self.button_up = Button((0,0,BS,BS),RED,change_color,text="UP",**BUTTON_STYLE)
		self.button_up.rect.center = (norm - BS*2,100)

		self.button_down = Button((0,0,BS,BS),RED,change_color,text="DOWN",**BUTTON_STYLE)
		self.button_down.rect.center = (norm - BS,100)

		self.button_left = Button((0,0,BS,BS),RED,change_color,text="LEFT",**BUTTON_STYLE)
		self.button_left.rect.center = (norm,100)

		self.button_right = Button((0,0,BS,BS),RED,change_color,text="RIGHT",**BUTTON_STYLE)
		self.button_right.rect.center = (norm + BS,100)

		self.button_f1 = Button((0,0,BS,BS),GREEN,change_color,text="F1",**BUTTON_STYLE)
		self.button_f1.rect.center = (norm + BS*2,100)

		self.group_button = [self.button_up,self.button_down,self.button_left,self.button_right,self.button_f1]

	def init_solution(self):
		self.group_solution = []
		norm = SCREEN_WIDTH+SCREEN_WIDTH//4
		for i in range(self.board.op_max):
			self.group_solution.append(Button((0,0,BS,BS),WHITE,None,text=None,**BUTTON_STYLE2))
			self.group_solution[-1].rect.center = (norm - BS +BS*i, 200)

	def process_buttons(self, pos):
		if self.button_up.rect.collidepoint(pos):
			self.code.append("UP")
		elif self.button_down.rect.collidepoint(pos):
			self.code.append("DOWN")
		elif self.button_left.rect.collidepoint(pos):
			self.code.append("LEFT")
		elif self.button_right.rect.collidepoint(pos):
			self.code.append("RIGHT")
		elif self.button_f1.rect.collidepoint(pos):
			self.code.append("F1")

	def load_solution(self, pos):
		
		if self.code != []:
			for i in range(len(self.code)):
				# if self.code[i] == "F1":
				# 	color = GREEN
				# else:
				# 	color = WHITE
				rect = self.group_solution[i].rect.center
				color = self.group_solution[i].color
				self.group_solution[i] = Button((0,0,BS,BS),color,None,text=self.code[i],**BUTTON_STYLE2)
				self.group_solution[i].rect.center = rect

	def CodeInput(self):

		txt = " -=Press [SPACE] to Play=-"
		txt = self.font2.render(txt, True, GREEN)
		txt_center = (
            SCREEN_WIDTH + SCREEN_WIDTH//4 - txt.get_width() // 2,\
				 300 - txt.get_height() // 2
        )

		click, c, cin = 0, 0, True
		self.code = []
		
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					if event.key == pygame.K_SPACE:
						return 1
				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]:
						for gs in self.group_solution:
							if gs.rect.collidepoint(pygame.mouse.get_pos()):
								if not gs.nc:
									gs.color = BLUE
								else:
									gs.color = WHITE
								gs.nc = 1 - gs.nc 
					if cin and pygame.mouse.get_pressed()[0]:
						pos = pygame.mouse.get_pos()
						self.process_buttons(pos)
						c += 1
						if c == self.board.op_max:
							cin = False
						self.load_solution(pos)
			
			self.render_CodeInput(txt, txt_center)

			pygame.display.flip()
			self.clock.tick(30)

	def render_CodeInput(self, txt, txt_center):
		self.screen.fill(WHITE)			
		self.screen.blit(self.right_menu, (SCREEN_WIDTH, 0))
		self.screen.blit(txt, txt_center)
		for b in self.group_button:
			b.update(self.screen)
		for b in self.group_solution:
			b.update(self.screen)
		self.board.draw()

	def render_Play(self):
		self.screen.fill(WHITE)
		self.screen.blit(self.right_menu, (SCREEN_WIDTH, 0))
		for b in self.group_button:
			b.update(self.screen)
		for b in self.group_solution:
			b.update(self.screen)
		self.board.draw()

	def Play(self):	
		#############################################
		self.list_actions = []
		if is_in_list(self.code, "F1"):
			flag = True
		else:
			self.get_list()
			flag = False
		############################################
		opt = True
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						running = False
					
			
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

			self.render_Play()

			pygame.display.flip()
			self.clock.tick(3)

	def get_list(self): ###############################
		for i in range(len(self.code)):
			if self.code[i] == "F1":
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
		txt2 = " -=Press [SPACE] to Play=-"
		txt2 = self.font2.render(txt2, True, GREEN)
		txt_center2 = (
            SCREEN_WIDTH + SCREEN_WIDTH//4 - txt.get_width() // 2,\
				 300 - txt.get_height() // 2
        )
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return -2					
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						return -2
					if event.key == pygame.K_SPACE:
						return opt
				if event.type == pygame.MOUSEBUTTONDOWN:
					if pygame.mouse.get_pressed()[0]:
						p = rev_rect(pygame.mouse.get_pos())
			self.screen.fill(WHITE)
			# self.right_menu.blit(txt, (SCREEN_WIDTH//4 - txt.get_width(), 50 - txt.get_height()//2))
			self.screen.blit(self.right_menu, (SCREEN_WIDTH, 0))
			self.board.draw()
			self.screen.blit(txt, txt_center)
			if opt == 1:
				self.screen.blit(txt2, txt_center2)
			pygame.display.flip()
			self.clock.tick(2)
		return -1


if __name__ == '__main__':
	Game()