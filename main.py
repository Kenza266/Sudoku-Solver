grid = [[0,0,0,0,0,0,0,2,0],
        [9,7,0,0,0,0,4,0,0],
        [0,4,0,1,0,8,0,0,0],
        [0,0,0,6,0,3,0,7,0],
        [0,0,0,4,0,0,0,8,5],
        [0,0,8,0,0,5,0,3,0],
        [0,5,0,0,0,0,2,0,0],
        [0,0,0,0,0,1,0,6,3],
        [3,0,0,7,4,0,0,9,0]]

def print_grid (grid) :
	for i in grid :
		for j in i :
			print(j,"\t", end = '')
		print ("\n", end = '')

def possible (x,y,n) : 
	for i in range(9) :
		if grid[i][y] == n or grid[x][i] == n : 
			return False
	tmp = x%3
	x0 = x - tmp
	tmp = y%3
	y0 = y - tmp
	for i in range (3) :
		for j in range (3) :
			if grid[x0+i][y0+j] == n :
				return False
	return True

def solve() :
	global grid
	for i in range(9) :
		for j in range(9) :
			if grid[i][j] == 0 :
				for x in range(1,10) : 
					if possible (i,j,x) :
						grid[i][j] = x
						solve()
						grid[i][j] = 0
				return grid 
	print ("Sudoku Solved !")
	print_grid (grid)

print("Grid :")
print_grid (grid)
solve()
