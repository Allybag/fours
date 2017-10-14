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

	@classmethod
	def playMove(cls, square):
		cls.state[square] = 1 if cls.firstToPlay else cls.n + 1
		cls.nextTurn()
		print(cls.state, "\n First Player to Play: {}".format(cls.firstToPlay))


	@classmethod
	def nextTurn(cls):
		cls.firstToPlay = not cls.firstToPlay

	@classmethod
	def undo(cls):
		cls.moveList.pop()

