UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

class Action:
	def __init__(self, index, direction, move):
		'''A class to represent actions of 1 state
			1. index: index of the block moving
			2. direction: UP, DOWN, LEFT, RIGHT
			3. move: the number of moving step
		'''
		self.index = index
		self.direction = direction
		self.move = move

	def print_action(self):
		if self.direction == UP:
			direct = "up"
		elif self.direction == DOWN:
			direct = "down"
		elif self.direction == LEFT:
			direct = "left"
		elif self.direction == RIGHT:
			direct = "right"
		name = "B" + str(self.index + 1)
		print("Block '%s' moving '%s': '%d' steps" % (name, direct, self.move))	

if __name__ == "__main__":
	action = Action(0, DOWN, 3)
	action.print_action()
