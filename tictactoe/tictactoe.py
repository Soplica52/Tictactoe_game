"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1

    if board == initial_state():
        return X
    if count % 2 == 1:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] is not EMPTY:
        raise ValueError("Invalid action: Position already taken.")

    # Create a copy of the board
    new_board = [row[:] for row in board]

    # Get the current player
    current_player = player(board)

    # Make the move
    new_board[action[0]][action[1]] = current_player

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    Returns 'X' if X wins, 'O' if O wins, or None if there is no winner yet.
    """

    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]  # Return the winner ('X' or 'O')

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not None:
            return board[0][j]  # Return the winner ('X' or 'O')

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]  # Return the winner ('X' or 'O')

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]  # Return the winner ('X' or 'O')

    # No winner found
    return None




def terminal(board):
    """
    Returns True if the game is over (either by win or tie), False otherwise.
    """
    # Check if there is a winner
    if winner(board) is not None:
        return True

    # Check if the board is full (no empty spots)
    for row in board:
        if EMPTY in row:
            return False

    # If the board is full and there's no winner, it's a tie
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)  # Check who the winner is
    if win == X:
        return 1  # X wins
    elif win == O:
        return -1  # O wins
    else:
        return 0  # No winner (tie or ongoing game)


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    current_player = player(board)

    # Define the maximizing and minimizing functions
    if current_player == X:
        # X is the maximizing player
        _, move = max_value(board)
    else:
        # O is the minimizing player
        _, move = min_value(board)

    return move


def max_value(board):
    """
    Maximizer for X.
    """
    if terminal(board):
        return utility(board), None

    v = -math.inf
    best_action = None

    for action in actions(board):
        min_val, _ = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action

    return v, best_action


def min_value(board):
    """
    Minimizer for O.
    """
    if terminal(board):
        return utility(board), None

    v = math.inf
    best_action = None

    for action in actions(board):
        max_val, _ = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action

    return v, best_action
