class State():
	"""This State holds all information about the game."""

	# Cross starts, board of length m, and the game has no result yet
	firstToPlay = True
	result = None
	n = 9
	winSize = 650

	# moveList and state are all representations of the board
	moveList = []
	#state = np.zeros((n, n))

	@classmethod
	def undo(cls):
		cls.moveList.pop()
	
	@classmethod
	def nextTurn(cls):
		cls.firstToPlay = not cls.firstToPlay
