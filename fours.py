import tkinter as tk
import board
from core import State

def main():
	root = tk.Tk()
	root.title("Fours")

	n = State.n
	size = State.winSize / n
	squares = [(rank, col) for rank in range(n) for col in range(n)]

	for (rank, col) in squares:

		square = board.Square((rank, col), master=root, size=size)
		square.grid(row=rank, column=col)

	root.mainloop()

if __name__ == '__main__':
	main()
