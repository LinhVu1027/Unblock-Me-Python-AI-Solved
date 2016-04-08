from state import *
from action import *

class UnblockMe:
	def __init__(self, initial_state):
		self.initial_state = initial_state

	def get_actions(self, state):
		'''Return a list of Action objects that are the successors
			of current state 
		'''
		actionList = []
		# Go through all the blocks in the block list
		for index in range(len(state.block_list)):
			# For each block, fill all valid movement to action list
			block = state.block_list[index]
			if block.orientation == VERTICAL:
				up, down = state.check_vertical_move(index)
				# add move up actions to list
				# Example: up = 3, add up(1), up(2), up(3)
				while up > 0:
					action = Action(index, UP, up)
					actionList.append(action)
					up -= 1
				# add move down actions to list
				# Example: down = 3, add down(1), down(2), down(3)
				while down > 0:
					action = Action(index, DOWN, down)
					actionList.append(action)
					down -= 1
			elif block.orientation == HORIZONTAL:
				left, right = state.check_horizontal_move(index)
				# add move left actions to list
				# Example: left = 3, add left(1), left(2), left(3)
				while left > 0:
					action = Action(index, LEFT, left)
					actionList.append(action)
					left -= 1
				# add move right actions to list
				# Example: right = 3, add right(1), right(2), right(3)
				while right > 0:
					action = Action(index, RIGHT, right)
					actionList.append(action)
					right -= 1

		return actionList


	def get_result(self, state, action):
		'''Return a new state through parent state and its action'''
		# Get all attributes of a block
		block_name = state.block_list[action.index].name
		block_orientation = state.block_list[action.index].orientation
		block_length = state.block_list[action.index].length

		# Set top left position of a new block
		row = int()
		column = int()
		if action.direction == UP:
			row = state.block_list[action.index].position[0] - action.move
			column = state.block_list[action.index].position[1]
		elif action.direction == DOWN:
			row = state.block_list[action.index].position[0] + action.move
			column = state.block_list[action.index].position[1]
		elif action.direction == LEFT:
			row = state.block_list[action.index].position[0]
			column = state.block_list[action.index].position[1] - action.move
		elif action.direction == RIGHT:
			row = state.block_list[action.index].position[0]
			column = state.block_list[action.index].position[1] + action.move
		block_position = (row, column)

		# Initialize a new block
		new_block = Block(block_name, block_orientation, block_position, block_length)

		# Initialize a new block list for a state
		new_block_list = state.block_list[:action.index] + [new_block] + state.block_list[action.index + 1:]

		# Return a new state with 1 block is changed
		return State(new_block_list)

	def get_step_cost(self, state, action):
		return action.move

	def test_goal(self, state):
		'''Check this state is a goal state
			A goal state is a state that its block named "R" or its last block
			has block"s tail at (2, 5)
			Example: block has postion: (2, 3), orientation: horizontal, length: 3
			So it's tail has position at (2,5)
		'''
		# Default row_tail = 2 and orientation = horizontal
		target_block = state.block_list[-1]
		column_tail = target_block.position[1] + target_block.length - 1
		return column_tail == 5


if __name__ == "__main__":
	pass
