###############################
## Author: TRAN Quang Toan	##
## Project APP_4_0_CODE		##
## Version 1					  ##
## 13 Apr 2020					##
###############################

import pygame
import os.path

CELL = 30
PX = 20
PY = 15
SCREEN_WIDTH = CELL * PX
SCREEN_HEIGHT = CELL * PY
BS = 50

j00 = pygame.image.load(os.path.join("img", "jet_up.png"))
j00 = pygame.transform.scale(j00, (CELL, CELL))
j00.set_colorkey((255, 255, 255), pygame.RLEACCEL)

j01 = pygame.image.load(os.path.join("img", "jet_right.png"))
j01 = pygame.transform.scale(j01, (CELL, CELL))
j01.set_colorkey((255, 255, 255), pygame.RLEACCEL)

j10 = pygame.image.load(os.path.join("img", "jet_down.png"))
j10 = pygame.transform.scale(j10, (CELL, CELL))
j10.set_colorkey((255, 255, 255), pygame.RLEACCEL)

j11 = pygame.image.load(os.path.join("img", "jet_left.png"))
j11 = pygame.transform.scale(j11, (CELL, CELL))
j11.set_colorkey((255, 255, 255), pygame.RLEACCEL)

JET = {
	"00": j00,
	"01": j01,
	"10": j10,
	"11": j11
}

BLACK = (0, 0, 0)
ORANGE = (181, 101, 29)
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLUE = (135, 206, 250)
RED = (255, 0, 0)
RED_B = (255, 102, 102)
RED_P = (255, 51, 51)
GRIS_B = (192, 192, 192)
GRIS = (128, 128, 128)

CC = [WHITE, None, RED_B, None]

BUTTON_STYLE = {"hover_color" : BLUE,\
					 "clicked_color" : GREEN,\
					 "clicked_font_color" : BLACK,\
					 "hover_font_color" : ORANGE}

BUTTON_STYLE2 = {#"hover_color" : BLUE,\
					 "font_color" : BLACK,\
					 "clicked_color" : BLUE,\
					 "clicked_font_color" : BLACK}#,\
					 #"hover_font_color" : ORANGE}