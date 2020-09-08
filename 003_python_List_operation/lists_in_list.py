board = []
EMPTY = [1, 2]
for i in range(8):
    row = [EMPTY for i in range(8)]   #  it forms Two Dimensional array or matrix
    board.append(row)
print(board)
print("\n")

#########  other way
board = []
EMPTY = [1, 2]
board = [[EMPTY for i in range(8)] for j in range(8)]
print(board)
