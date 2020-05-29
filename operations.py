###############################
## Author: TRAN Quang Toan   ##
## Project APP_4_0_CODE      ##
## Version 1                 ##
## 13 Apr 2020               ##
###############################

from define import *
from ft_lib import *

class Operation():
	def __init__(self):
		pass

class RIGHT():
	def __init__(self):
		pass

	def run(self, ar, p, dk):
		x, y = p
		if dk == WHITE or CC[ar[x][y]] == dk:
			control = True
		else:
			control = False
		if check_valid(x+1, y) and control:
			if ar[x+1][y] != -1 or ar[x+1][y] == 3:
				#ar[x+1][y] = ar[x][y]
				#ar[x][y] = 0
				return (x+1,y)
		return ()

class LEFT():
	def __init__(self):
		pass

	def run(self, ar, p, dk):
		x, y = p
		if dk == WHITE or CC[ar[x][y]] == dk:
			control = True
		else:
			control = False

		if check_valid(x-1, y) and control:
			if ar[x-1][y] != -1 or ar[x-1][y] == 3:
				#ar[x-1][y] = ar[x][y]
				#ar[x][y] = 0
				return (x-1,y)
		return ()
		
class DOWN():
	def __init__(self):
		pass

	def run(self, ar, p, dk):
		x, y = p
		if dk == WHITE or CC[ar[x][y]] == dk:
			control = True
		else:
			control = False
		if check_valid(x, y+1) and control:
			if ar[x][y+1] != -1 or ar[x][y+1] == 3:
				#ar[x][y+1] = ar[x][y]
				#ar[x][y] = 0
				return (x,y+1)
		return ()

class UP():
	def __init__(self):
		pass

	def run(self, ar, p, dk):
		x, y = p
		if dk == WHITE or CC[ar[x][y]] == dk:
			control = True
		else:
			control = False
		if check_valid(x, y-1) and control:
			if ar[x][y-1] != -1 or ar[x][y-1] == 3:
				#ar[x][y-1] = ar[x][y]
				#ar[x][y] = 0
				return (x,y-1)
		return ()

class GO():
	def __init__(self):
		pass

	def run(self, ar, p, dk, dir): ## dir = 00/01/10/11
		if dir == "00":
			return UP().run(ar, p, dk)
		elif dir == "01":
			return RIGHT().run(ar, p, dk)
		elif dir == "10":
			return DOWN().run(ar, p, dk)
		elif dir == "11":
			return LEFT().run(ar, p, dk)

class TURN_LEFT():
	def __init__(self):
		pass

	def run(self, ar, p, dk, dir):
		x, y = p
		if dk == WHITE or CC[ar[x][y]] == dk:
			control = True
		else:
			control = False
		if control:
			if dir == "00":
				return "11"
			if dir == "01":
				return "00"
			if dir == "10":
				return "01"
			if dir == "11":
				return "10"
		return dir


class TURN_RIGHT():
	def __init__(self):
		pass

	def run(self, ar, p, dk, dir):
		x, y = p
		if dk == WHITE or CC[ar[x][y]] == dk:
			control = True
		else:
			control = False
		if control:
			if dir == "00":
				return "01"
			if dir == "01":
				return "10"
			if dir == "10":
				return "11"
			if dir == "11":
				return "00"
		return dir

