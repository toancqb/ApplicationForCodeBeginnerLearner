

class RIGHT():
	def __init__(self):
		pass

	def run(self, ar, p):
		x, y = p
		if check_valid(x+1, y):
			if ar[x+1][y] == 0:
				ar[x+1][y] = ar[x][y]
				ar[x][y] = 0
				return (x+1,y)
			elif ar[x+1][y] == 3:
				ar[x+1][y] = ar[x][y]
				ar[x][y] = 0
				return (PX,PY)
		return ()

class LEFT():
	def __init__(self):
		pass

	def run(self, ar, p):
		x, y = p
		if check_valid(x-1, y):
			if ar[x-1][y] == 0:
				ar[x-1][y] = ar[x][y]
				ar[x][y] = 0
				return (x-1,y)
			elif ar[x-1][y] == 3:
				ar[x-1][y] = ar[x][y]
				ar[x][y] = 0
				return (PX,PY)
		return ()
		
class DOWN():
	def __init__(self):
		pass

	def run(self, ar, p):
		x, y = p
		if check_valid(x, y+1):
			if ar[x][y+1] == 0:
				ar[x][y+1] = ar[x][y]
				ar[x][y] = 0
				return (x,y+1)
			elif ar[x][y+1] == 3:
				ar[x][y+1] = ar[x][y]
				ar[x][y] = 0
				return (PX,PY)
		return ()

class UP():
	def __init__(self):
		pass

	def run(self, ar, p):
		x, y = p
		if check_valid(x, y-1):
			if ar[x][y-1] == 0:
				ar[x][y-1] = ar[x][y]
				ar[x][y] = 0
				return (x,y-1)
			elif ar[x][y-1] == 3:
				ar[x][y-1] = ar[x][y]
				ar[x][y] = 0
				return (PX,PY)
		return ()