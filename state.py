VERTICAL = False
HORIZONTAL = True

SIZE_BOARD = 6

class Block:
	"""A class to represent the blocks in the Unblock Me board."""

	def __init__(self, name, orientation, position, length):
		'''Return a new block with the given attributes.
			1. name: a string represent the name of block
			2. orientation: VERTICAL(False) or HORIZONTAL(True)
			3. position: a tuple(x,y) represent the row and column
						of the top left square of block
			4. length: integer represent the number of square
		'''
		self.name = name
		self.orientation = orientation
		self.position = position
		self.length = length

class State:
	"""A class to represent the state of the Unblock Me problem."""

	def __init__(self, block_list):
		'''Return a new state with the given attributes.
			1. block_list: a list of blocks in board
			2. board: 6x6 with block positions in it
		'''
		self.block_list = block_list
		self.board = self.make_board(block_list)

	def make_board(self, block_list):
		'''With the given blocks in list, fill the board.'''
		board = [[0 for x in range(SIZE_BOARD)] for y in range(SIZE_BOARD)]

		# Fill in the board
		for index in range(len(block_list)):
			# Fill vertical block
			if block_list[index].orientation == VERTICAL:
				for i in range(block_list[index].length):	
					board[block_list[index].position[0] + i][block_list[index].position[1]] = index + 1
			# Fill horizontal block
			else:
				for i in range(block_list[index].length):
					board[block_list[index].position[0]][block_list[index].position[1] + i] = index + 1
		return board

	def check_vertical_move(self, index):
		'''Check a block in state can move TOP, DOWN in board.
			index: index of a block in the block list
		'''
		# Get top left postion of this block
		position = self.block_list[index].position
		length = self.block_list[index].length
		up = 0
		down = 0		
		# Check how far we can move up
		row = position[0] - 1
		while row >= 0:
			if not self.board[row][position[1]]:
				up += 1
				row -= 1
			else: break
		# Check how far we can move down
		row = position[0] + length
		while row < SIZE_BOARD:
			if not self.board[row][position[1]]:
				down += 1
				row += 1
			else: break

		# Example up, down = 3 , 2:
		# So we can go up maximum 3 steps, and go down maximum 2 steps
		return up, down

	def check_horizontal_move(self, index):
		'''Check a block in state can move LEFT, RIGHT in board.
			index: index of a block in the block list
		'''
		# Get top left postion of this block
		position = self.block_list[index].position
		length = self.block_list[index].length
		left = 0
		right = 0		
		# Check how far we can go left
		column = position[1] - 1
		while column >= 0:
			if not self.board[position[0]][column]:
				left += 1
				column -= 1
			else: break
		# Check how far we can go right
		column = position[1] + length
		while column < SIZE_BOARD:
			if not self.board[position[0]][column]:
				right += 1
				column += 1
			else: break

		# Example left, right = 3 , 2:
		# So we can go left maximum 3 steps, and go right maximum 2 steps
		return left, right

	# Check 3 last column 4,5,6
	def heuristic(self):
		'''Return heuristic of this state
		'''
		point = 0
		# If there's a block at column 6 before the gate
		if self.board[2][5] != 0 and (self.board[1][5] == self.board[2][5] or self.board[3][5] == self.board[2][5]):
			point += 1
		# If there's a block at column 5 before the gate
		if self.board[2][4] != 0 and (self.board[1][4] == self.board[2][4] or self.board[3][4] == self.board[2][4]):
			point += 7
		# If there's a block at column 4 before the gate
		if self.board[2][3] != 0 and (self.board[1][3] == self.board[2][3] or self.board[3][3] == self.board[2][3]):
			point += 11
		return point

	# We need __eq__ and __hash___ to distinguish 2 instances in a set
	def __eq__(self, other):
		'''Compare two instance'''
		return self.board == other.board

	def __hash__(self):
		'''Hash its instance'''
		return hash(tuple(tuple(x) for x in self.board))

	def print_board(self):
		'''Print the board represent blocks in the board'''
		for i in range(SIZE_BOARD):
			for j in range(SIZE_BOARD):
				print "%s \t" % self.board[i][j],
			print



if __name__ == "__main__":
	pass

