import numpy as np

class State():
	"""This State holds all information about the game."""

	# Cross starts, board of length m, and the game has no result yet
	firstToPlay = True
	result = None
	n = 9
	winSize = 650

	# moveList and state are all representations of the board
	moveList = []
	state = np.zeros((n, n))

	@staticmethod
	def findLongestLine(state, position):
		n = max(state.shape)
		longestLineLen = 0
		# East, South, Southeast, Southwest
		for z in [(1, 0), (0, 1), (1, 1), (1, -1)]:
			lineLen = 1
			for i in range(1, 4):
				square = tuple(map(lambda x, y: x + y, position, tuple(i * x for x in z)))
				# Check we're still on the board
				if max(square) >= n or min(square) < 0:
					break
				elif state[position] == state[square]:
					lineLen += 1
				else:
					break
			for i in range(1, 4):
				square = tuple(map(lambda x, y: x - y, position, tuple(i * x for x in z)))
				# If we've found four in a row, we're done
				if lineLen == 4:
					return lineLen
				# Check we're still on the board
				elif max(square) >= n or min(square) < 0:
					break
				elif state[position] == state[square]:
					lineLen += 1
				else:
					break

			if lineLen > longestLineLen:
				longestLineLen = lineLen

		return longestLineLen

	@classmethod
	def playMove(cls, square):
		cls.state[square] = 1 if cls.firstToPlay else cls.n + 1
		cls.firstToPlay = not cls.firstToPlay
		print("Last piece played: {}".format(square))
		print("\n Longest line through last played piece: {}".format(
			cls.findLongestLine(cls.state, square)))

