board=[' ']*9
def show():
 for r in range(0,9,3): print('|'.join(board[r:r+3]))
for move,mark in ((0,'X'),(4,'O'),(1,'X'),(3,'O'),(2,'X')):
 board[move]=mark; show(); print()
print('X wins')
