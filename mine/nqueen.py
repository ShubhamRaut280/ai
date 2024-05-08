def main():
	n = int(input('Enter number of queens: '))
	board = [[0]*n for i in range(n)]
	
	if solve(board, 0, n):
		print('Solution exist.')
		for i in range(n):
			for j in range(n):
				print(board[i][j], end = ' ')
			print()
	else : 
		print('Solution does not exist!')

# [0,0,0,0]
# [0,0,0,0]
# [0,0,0,0]
# [0,0,0,0]


def solve(board, row, n):
	if row>=n: 
		return True

	for col in range(n):
		if is_safe(board, row, col, n):
			board[row][col] = 1
			if solve(board, row+1, n):
				return True
			board[row][col] = 0
	return False


def is_safe(arr, x, y, n):
	# check for same column diff row

	for row in range(x):
		if arr[row][y]==1:
			return False

	
	# check for upper left diagonal

	row = x
	col = y
	while row>=0 and col>=0:
		if arr[row][col] == 1:
			return False
		row-=1
		col-=1


	# check for upper right diagonal
	row = x
	col = y
	while row>=0 and col<n:
		if arr[row][col]==1:
			return False
		row-=1
		col+=1

	return True

main()