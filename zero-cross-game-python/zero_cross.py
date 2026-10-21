"""
Zero Cross (Tic-Tac-Toe): Player vs Computer
Player is X; computer is O. Computer uses the Minimax algorithm.
Run: python zero_cross.py
"""

HUMAN = "X"
COMPUTER = "O"
EMPTY = " "


def print_board(board):
    """Display the current 3x3 board with position numbers for empty cells."""
    cells = [str(i + 1) if value == EMPTY else value for i, value in enumerate(board)]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print()


def winner(board):
    """Return X or O if there is a winner, otherwise None."""
    lines = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    )
    for a, b, c in lines:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def minimax(board, is_maximizing, depth=0):
    """Evaluate the board recursively; quicker wins and slower losses are preferred."""
    result = winner(board)
    if result == COMPUTER:
        return 10 - depth
    if result == HUMAN:
        return depth - 10
    if EMPTY not in board:
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for index, cell in enumerate(board):
            if cell == EMPTY:
                board[index] = COMPUTER
                score = minimax(board, False, depth + 1)
                board[index] = EMPTY
                best_score = max(best_score, score)
        return best_score

    best_score = float("inf")
    for index, cell in enumerate(board):
        if cell == EMPTY:
            board[index] = HUMAN
            score = minimax(board, True, depth + 1)
            board[index] = EMPTY
            best_score = min(best_score, score)
    return best_score


def computer_move(board):
    """Choose the best available move using Minimax."""
    best_score = float("-inf")
    best_index = None
    for index, cell in enumerate(board):
        if cell == EMPTY:
            board[index] = COMPUTER
            score = minimax(board, False, 1)
            board[index] = EMPTY
            if score > best_score:
                best_score = score
                best_index = index
    return best_index


def human_move(board):
    """Read and validate a player's choice."""
    while True:
        choice = input("Choose a position (1-9): ").strip()
        if not choice.isdigit() or not 1 <= int(choice) <= 9:
            print("Please enter a number from 1 to 9.")
            continue
        index = int(choice) - 1
        if board[index] != EMPTY:
            print("That position is already occupied. Choose another.")
            continue
        return index


def play_game():
    """Play one game of Zero Cross."""
    board = [EMPTY] * 9
    print("Welcome to Zero Cross!")
    print("You are X. The computer is O.")
    print("Choose a position from 1 to 9 as shown on the board.")
    print_board(board)

    while True:
        board[human_move(board)] = HUMAN
        print_board(board)
        if winner(board) == HUMAN:
            print("Congratulations! You win!")
            break
        if EMPTY not in board:
            print("It's a draw!")
            break

        print("Computer is thinking...")
        move = computer_move(board)
        if move is not None:
            board[move] = COMPUTER
        print_board(board)
        if winner(board) == COMPUTER:
            print("Computer wins. Better luck next time!")
            break
        if EMPTY not in board:
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()
