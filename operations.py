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

	def run(self, ar, p):
		x, y = p
		if check_valid(x+1, y):
			if ar[x+1][y] == 0 or ar[x+1][y] == 3:
				ar[x+1][y] = ar[x][y]
				ar[x][y] = 0
				return (x+1,y)
		return ()

class LEFT():
	def __init__(self):
		pass

	def run(self, ar, p):
		x, y = p
		if check_valid(x-1, y):
			if ar[x-1][y] == 0 or ar[x-1][y] == 3:
				ar[x-1][y] = ar[x][y]
				ar[x][y] = 0
				return (x-1,y)
		return ()
		
class DOWN():
	def __init__(self):
		pass

	def run(self, ar, p):
		x, y = p
		if check_valid(x, y+1):
			if ar[x][y+1] == 0 or ar[x][y+1] == 3:
				ar[x][y+1] = ar[x][y]
				ar[x][y] = 0
				return (x,y+1)
		return ()

class UP():
	def __init__(self):
		pass

	def run(self, ar, p):
		x, y = p
		if check_valid(x, y-1):
			if ar[x][y-1] == 0 or ar[x][y-1] == 3:
				ar[x][y-1] = ar[x][y]
				ar[x][y] = 0
				return (x,y-1)
		return ()


