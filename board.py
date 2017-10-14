import tkinter as tk
from core import State

class Board(tk.Frame):

	def colourToPlay():
		if State.firstToPlay:
			return('gold')
		else:
			return('purple')


class Square(tk.Canvas):
	"""A Square is a canvas upon which coloured circles can be drawn"""

	def __init__(self, position, master=None, size=None, colour='blue'):
		super().__init__(master, width=size, height=size, bg=colour)
		self.bind("<Button-1>", self.fill)
		self.config(highlightbackground="Black")
		self.config(highlightthickness=1)

		self.size = size
		self.colour = None
		self.position = position
		self.circle = self.create_oval(0, self.size, self.size, 0, fill='#fff')
		
	def fill(self, event):
		self.itemconfig(self.circle, fill=Board.colourToPlay())
		State.nextTurn()
