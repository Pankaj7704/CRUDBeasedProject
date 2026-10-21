HUMAN = "X"
COMPUTER = "O"


def print_board(board):
    print()
    for i in range(0, 9, 3):
        print(" " + " | ".join(board[i:i + 3]))
        if i < 6:
            print("---+---+---")
    print()


def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    return None


def minimax(board, is_computer):
    winner = check_winner(board)

    if winner == COMPUTER:
        return 1
    if winner == HUMAN:
        return -1
    if " " not in board:
        return 0

    if is_computer:
        best_score = -float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = COMPUTER
                score = minimax(board, False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(9):
            if board[i] == " ":
                board[i] = HUMAN
                score = minimax(board, True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def computer_move(board):
    best_score = -float("inf")
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = COMPUTER
            score = minimax(board, False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = COMPUTER

    print("Computer has made its move!")


def play_game():
    board = [" "] * 9

    print("=" * 30)
    print("     ZERO CROSS GAME")
    print("=" * 30)
    print("You are X | Computer is O")
    print("Choose a position from 1 to 9.")

    while True:
        # Display position numbers for empty cells
        display = [
            str(i + 1) if board[i] == " " else board[i]
            for i in range(9)
        ]
        print_board(display)

        # Player's turn
        while True:
            try:
                move = int(input("Enter your position (1-9): "))

                if move < 1 or move > 9:
                    print("Please enter a number between 1 and 9.")
                elif board[move - 1] != " ":
                    print("That position is already occupied!")
                else:
                    break

            except ValueError:
                print("Invalid input! Please enter a number.")

        board[move - 1] = HUMAN

        if check_winner(board) == HUMAN:
            print_board(board)
            print("Congratulations! You win!")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break

        # Computer's turn
        computer_move(board)

        if check_winner(board) == COMPUTER:
            print_board(board)
            print("Computer wins! Better luck next time.")
            break

        if " " not in board:
            print_board(board)
            print("It's a draw!")
            break


if __name__ == "__main__":
    play_game()

