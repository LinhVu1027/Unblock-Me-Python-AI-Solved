from sys import argv
from time import time

from util import *
from node import *
from unblockme import *
from state import *

def get_child_node(problem, parent, action):
	cState = problem.get_result(parent.state, action)
	cParent = parent
	cAction = action
	cPathCost = parent.pathCost + problem.get_step_cost(parent.state, action)
	return Node(cState, cParent, cAction, cPathCost)

def BFS(problem):
	root = Node(problem.initial_state)
	if problem.test_goal(root.state): return root

	frontier = Queue()
	frontier.push(root)
	explored = set()

	while True:
		if frontier.isEmpty():
			print("Cannot find solution")
			return False
		node = frontier.pop()
		explored.add(node.state)
		for action in problem.get_actions(node.state):
			child = get_child_node(problem, node, action)
			if child.state not in explored:
				if problem.test_goal(child.state): return child
				frontier.push(child)

def DFS(problem):
	root = Node(problem.initial_state)
	if problem.test_goal(root.state): return root

	frontier = Stack()
	frontier.push(root)
	explored = set()

	while True:
		if frontier.isEmpty():
			print("Cannot find solution")
			return False
		node = frontier.pop()
		explored.add(node.state)
		for action in problem.get_actions(node.state):
			child = get_child_node(problem, node, action)
			if child.state not in explored:
				if problem.test_goal(child.state): return child
				frontier.push(child)

def AStar(problem):
	root = Node(problem.initial_state)
	if problem.test_goal(root.state): return root

	frontier = PriorityQueue()
	h_val = root.state.heuristic()
	g_val = root.pathCost
	f_val = h_val + g_val
	frontier.push(root, f_val)
	explored = set()

	while True:
		if frontier.isEmpty():
			print("Cannot find solution")
			return False
		node = frontier.pop()
		explored.add(node.state)
		for action in problem.get_actions(node.state):
			child = get_child_node(problem, node, action)
			if child.state not in explored:
				if problem.test_goal(child.state): return child
				h_val_child = child.state.heuristic()
				g_val_child = child.pathCost
				f_val_child = h_val + g_val
				frontier.push(child, f_val_child)

def get_solution(node):
	# Get path cost
	step = 0

	stack = Stack()
	while node.parent != None:
		stack.push((node.state, node.action))
		node = node.parent
		step += 1
	stack.push((node.state, node.action))

	while not stack.isEmpty():
		state, action = stack.pop()

		print("----------------------------------------------")
		try:
			action.print_action()
		except AttributeError:
			pass
		state.print_board()

	print("The number of movement: %d" % step)

def get_board_list(node):
	stack = Stack()
	while node.parent != None:
		stack.push(node.state.board)
		node = node.parent
	stack.push(node.state.board)

	board_list = []
	while not stack.isEmpty():
		board_list.append(stack.pop())

	return board_list

# input1 example:
# B1 vertical 0 0 3
# B2 horizontal 0 1 2
# B3 vertical 3 0 2
# B4 horizontal 4 1 2
# B5 vertical 1 3 3
# B6 horizontal 5 2 3
# B7 vertical 3 5 3
# R horizontal 2 1 2
def getStateFromInput(file_path):
	block_list = dataToBlockList(file_path)
	state = State(block_list)
	
	return state	

def dataToBlockList(file_path):
	'''Convert input datas to a list of block
	   This function will return:
	   [B1, B2, .., Bn]
	'''
	block_list = []
	with open(file_path) as f:
		# Each line is each block
		for line in f:
			# Line without ' ' '\n' at the end of the line
			pretty_line = line.rstrip()

			# Command will return a data have the format like: 
			# 	datas = ["B1", "vertical", "0", "0", "3"]
			datas = pretty_line.split(' ')

			# Set all attributes for a block:
			# name, orientation, position, length
			name = datas[0]
			if datas[1] == "vertical": orientation = VERTICAL
			else: orientation = HORIZONTAL
			position = (int(datas[2]), int(datas[3]))
			length = int(datas[4])
			block = Block(name, orientation, position, length)

			# Append a new block to the block list
			block_list.append(block)
	return block_list


if __name__ == "__main__":
	# Ex: >python search.py input1.txt
	# script = search.py
	# filename = input1.txt
	script, strategy, filename = argv

	# file is in input folder so file path:
	file_path = "input/" + filename

	# initial_state of the Unblock Me problem
	initial_state = getStateFromInput(file_path)
	#initial_state.print_board()
	#block_list = initial_state.block_list
	#test_state = State(block_list)

	# Test __eq__
	#if initial_state == test_state:
	#	print "True"

	# Test __hash__
	#c = set()
	#c.add(initial_state)
	#c.add(test_state)
	#print hash(initial_state)
	#print hash(test_state)
	#print c

	problem = UnblockMe(initial_state)

	#actions =  problem.get_actions(problem.initial_state)
	#for action in actions:
	#	print "------------------------------------------------"
	#	action.print_action()
	#	state = problem.get_result(problem.initial_state, action)
	#	state.print_board()

	start_time = time()
	if strategy.lower() == "bfs":
		result = BFS(problem)
	elif strategy.lower() == "dfs":
		result = DFS(problem)
	end_time = time()
	elapsed = end_time - start_time

	if result:
		get_solution(result)

	print("Search time: %s" % elapsed)
	print("The number of initialized node: %d" % Node.n) 



