from search import *

import pygame
import random

strategy = str(raw_input('Press your strategy(dfs, bfs, astar):'))
filename = str(raw_input('Press your input.txt file(input1.txt,...):'))
file_path = "input/" + filename
initial_state = getStateFromInput(file_path)
problem = UnblockMe(initial_state)

result = False

start_time = time()
if strategy.lower() == "bfs":
	result = BFS(problem)
elif strategy.lower() == "dfs":
	result = DFS(problem)
elif strategy.lower() == "astar":
	result = AStar(problem)
end_time = time()
elapsed = end_time - start_time

get_solution(result)
board_list = get_board_list(result)
number_board = len(board_list)
index = -1

num_block = len(result.state.block_list)
color_list = [(random.randrange(255), random.randrange(255), random.randrange(255)) for x in range(num_block)]


print("Search time: %s" % elapsed)
print("The number of initialized node: %d" % Node.n)


WHITE = (255, 255, 255)
GRAY = (230, 230, 230)

WIDTH = 40
HEIGHT = 40

MARGIN = 5

pygame.init()

WINDOW_SIZE = (275, 275)
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Unblock Me")

clock = pygame.time.Clock()

done = False
while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	screen.fill(WHITE)


	if index < number_board - 1:
		index += 1

	for row in range(SIZE_BOARD):
		for column in range(SIZE_BOARD):
			color = GRAY
			if board_list[index][row][column] != 0:
				color = color_list[board_list[index][row][column] - 1]
			pygame.draw.rect(screen,
							 color,
							 [(MARGIN + WIDTH) * column + MARGIN,
							  (MARGIN + HEIGHT) * row + MARGIN,
							  WIDTH,
							  HEIGHT])

	clock.tick(1)
	pygame.display.flip()

pygame.quit()
