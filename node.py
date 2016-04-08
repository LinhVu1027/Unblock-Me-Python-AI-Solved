class Node:

	# The number of initialized node
	n = 0

	def __init__(self, state, parent=None, action=None, pathCost=0):
		self.state = state
		self.parent = parent
		self.action = action
		self.pathCost = pathCost

		# Increase 1 if a new node is initialized
		Node.n += 1

if __name__ == "__main__":
	node = Node((0,0))
	print(node.state)
	print(node.parent)
	print(node.action)
	print(node.pathCost)
	nodeChild = Node((2,2), node, 1)
	print(nodeChild.state)
	print(nodeChild.parent)
	print(nodeChild.action)
	print(nodeChild.pathCost)