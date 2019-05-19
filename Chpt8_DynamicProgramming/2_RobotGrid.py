def robot_grid(grid):

	path = []

	if robot_path(grid, [], len(grid)-1, len(grid[0])-1, path):
		return path

	return null


def robot_path(grid, visited, r, c, path):
	if (r < 0 or c < 0) or (grid[r][c] is 1) or ([r,c] in visited):		
		return False

	if ((r is 0 and c is 0) or robot_path(grid, visited, r - 1, c, path) 
			or robot_path(grid, visited, r, c-1, path)):
		path.append([r,c])
		return True

	visited.append([r,c])		
	return False

import unittest

class TestGrid(unittest.TestCase):
	grid = [[0, 0, 1], [1, 0, 1], [1, 0, 0]]
	
	def test_robot_grid(self):
		print(robot_grid(self.grid))
		self.assertEqual(robot_grid(self.grid), [[0,0], [0,1],[1,1],[2,1],[2,2]])

if __name__=="__main__":
	unittest.main()