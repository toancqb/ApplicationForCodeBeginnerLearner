
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
		if check_valid(x, y) and ar[x][y+1] == 0:
			ar[x][y+1] = ar[x][y]
			ar[x][y] = 0
		

