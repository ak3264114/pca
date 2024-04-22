# Tic tac toe with out computer

```python

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):

    for row in board:
        if all(cell == player for cell in row):
            return True


    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()

```

# Tic tac toe with computer

```python
import random

def print_board(board):
    # Function to print the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Function to check if a player has won the game
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def computer_move(board, player):
    # Function for the computer to make a move
    # First, check for a winning move
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player
                if check_winner(board, player):
                    return
                board[i][j] = " "

    # If no winning move, check for a blocking move (opponent's winning move)
    opponent = "O" if player == "X" else "X"
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = opponent
                if check_winner(board, opponent):
                    board[i][j] = player
                    return
                board[i][j] = " "

    # If no winning or blocking move, make a random move
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = player

def tic_tac_toe():
    # Main function to play Tic-Tac-Toe
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe against the computer!")
    print_board(board)

    while True:
        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("You win!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's move:")
        computer_move(board, "O")
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins!")
            break

        if all(all(cell != " " for cell in row) for row in board):
            print("It's a draw!")
            break

tic_tac_toe()
```

#fibonaci

```pl

fib(0, 0).
fib(1, 1).
fib(N, Result) :-
    N > 1,
    N1 is N - 1,
    N2 is N - 2,
    fib(N1, Result1),
    fib(N2, Result2),
    Result is Result1 + Result2.

```

# travelling SalesmanProblem

```python

# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

	# store all vertex apart from source vertex
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	# store minimum weight Hamiltonian Cycle
	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost)
		current_pathweight = 0

		# compute current path weight
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		# update minimum
		min_path = min(min_path, current_pathweight)

	return min_path


# Driver Code
if __name__ == "__main__":

	# matrix representation of graph
	graph = [[0, 10, 15, 20], [10, 0, 35, 25],
			[15, 35, 0, 30], [20, 25, 30, 0]]
	s = 0
	print(travellingSalesmanProblem(graph, s))

```



#DataFrame

```python

import pandas as pd

# Define your two-dimensional array
data = [[10, 20, 30, 40, 40],
        [10, 20, 30, 40, 50]]

# Create a DataFrame from the array
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# ---------------------------

data = [10, 20, 30, 40, 50]

# Create a DataFrame from the array with index and values columns named explicitly
df = pd.DataFrame({'index': range(len(data)), 'Values': data})


```

# JSON

### Read from dict
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Reading values
value_a = my_dict['a']
print(value_a)  # Output: 1


```


### GEt methood
```python 
value_b = my_dict.get('b')
print(value_b)  # Output: 2

value_d = my_dict.get('d', 'Key not found')
print(value_d)  # Output: 'Key not found'


```
### writing dict

```python

# Adding new key-value pairs
my_dict['d'] = 4
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Modifying existing value
my_dict['b'] = 20
print(my_dict)  # Output: {'a': 1, 'b': 20, 'c': 3, 'd': 4}

```

### update()
```python 
# Adding or updating multiple key-value pairs
my_dict.update({'e': 5, 'f': 6})
print(my_dict)  # Output: {'a': 1, 'b': 20, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

```

### To open a JSON file, add data to it, and then save it using Python,

```python 
import json

# Open the JSON file for reading
with open('data.json', 'r') as file:
    data = json.load(file)

# Add new data to the existing JSON object
data['new_key'] = 'new_value'

# Save the updated JSON object back to the file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

```