import random
import numpy as np

# Function to check if there is a win in Tic-Tac-Toe
def check_win(board, user_value):
    for i in range(3):
        if np.all(board[i] == user_value) or np.all(board[:, i] == user_value):
            return True
    if np.all(np.diag(board) == user_value) or np.all(np.diag(np.fliplr(board)) == user_value):
        return True
    return False

# Function to check if there is a draw in Tic-Tac-Toe
def is_draw(board):
    return np.all(board != " ")

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Tic-Tac-Toe game function
def tic_tac_toe():
    board = np.full((3, 3), " ")
    player1 = input("Enter player1 name: ")
    player2 = input("Enter player2 name: ")
    current_player = player1
    current_value = 'x'
    
    while True:
        print(f"\n{current_player}'s turn:")
        print_board(board)
        
        while True:
            try:
                user_inp = input("Enter row (0, 1, or 2) and column (0, 1, or 2) separated by space (or type 'exit' to quit): ")
                if user_inp.lower() == 'exit':
                    print(f"{current_player} has chosen to exit the game.")
                    return
                row, col = map(int, user_inp.split())
                if row in [0, 1, 2] and col in [0, 1, 2]:
                    if board[row][col] == " ":
                        board[row][col] = current_value
                        break
                    else:
                        print("That spot is already occupied. Try again.")
                else:
                    print("Invalid input. Please enter numbers between 0 and 2.")
            except ValueError:
                print("Invalid input. Please enter valid integers for row and column, or 'exit' to quit.")

        if check_win(board, current_value):
            print_board(board)
            print(f"\n{current_player} wins!")
            break
        elif is_draw(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        if current_player == player1:
            current_player = player2
            current_value = 'o'
        else:
            current_player = player1
            current_value = 'x'

# Function to get valid user input for Rock-Paper-Scissors
def get_user_input():
    while True:
        user_inp = input("Choose from rock, paper, scissors (or type 'exit' to quit): ").lower()
        if user_inp in ['rock', 'paper', 'scissors', 'exit']:
            return user_inp
        else:
            print("Invalid input. Please choose from rock, paper, or scissors, or type 'exit' to quit.")

# Function to determine the winner of Rock-Paper-Scissors
def determine_winner(user_inp, sys_inp):
    if user_inp == sys_inp:
        return "draw"
    elif (user_inp == 'rock' and sys_inp == 'scissors') or \
         (user_inp == 'paper' and sys_inp == 'rock') or \
         (user_inp == 'scissors' and sys_inp == 'paper'):
        return "win"
    else:
        return "lose"

# Function to play a round of Rock-Paper-Scissors
def play_round():
    options = ['rock', 'paper', 'scissors']
    user_inp = get_user_input()
    if user_inp == 'exit':
        print("You have chosen to exit the game.")
        return None

    sys_inp = random.choice(options)
    result = determine_winner(user_inp, sys_inp)

    print(f"User input: {user_inp}")
    print(f"System input: {sys_inp}")

    if result == "draw":
        print("It's a draw")
    elif result == "win":
        print("You won")
    else:
        print("You lost")
    
    return result

# Rock-Paper-Scissors game function
def rock_paper_scissors():
    scores = {"wins": 0, "losses": 0, "draws": 0}
    
    while True:
        result = play_round()
        if result is None:
            break
        if result == "win":
            scores["wins"] += 1
        elif result == "lose":
            scores["losses"] += 1
        else:
            scores["draws"] += 1

        while True:
            play_again = input("Enter 'yes' to play again/'no' to end the game and view results: ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        if play_again != 'yes':
            print("Thanks for playing!")
            print("Game Summary:")
            print(f"Wins: {scores['wins']}")
            print(f"Losses: {scores['losses']}")
            print(f"Draws: {scores['draws']}")
            break

# Function to get player name for Number Guessing Game
def get_user_name():
    return input("Please enter your name: ")

# Function to select difficulty for Number Guessing Game
def select_difficulty():
    while True:
        print("\nSelect Difficulty Level:")
        print("1. Easy (1 to 10)")
        print("2. Medium (1 to 50)")
        print("3. Hard (1 to 100)")
        print("4. Custom Range")
        print("5. Exit")
        
        try:
            difficulty = int(input("Enter the number corresponding to your choice: "))
            if difficulty in [1, 2, 3, 4, 5]:
                return difficulty
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

# Function to set range for Number Guessing Game
def set_range(difficulty):
    if difficulty == 1:
        return 1, 10, 5
    elif difficulty == 2:
        return 1, 50, 7
    elif difficulty == 3:
        return 1, 100, 10
    elif difficulty == 4:
        while True:
            try:
                lower = int(input("Enter the lower bound of the range: "))
                upper = int(input("Enter the upper bound of the range: "))
                if lower < upper:
                    return lower, upper, int((upper - lower) * 0.1) + 3
                else:
                    print("The lower bound must be less than the upper bound.")
            except ValueError:
                print("Invalid input. Please enter valid integers for the range.")
    elif difficulty == 5:
        return None, None, None  # Indicate exit

# Number Guessing Game function
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    player_name = get_user_name()
    best_score = None
    scoreboard = {}

    while True:
        difficulty = select_difficulty()
        if difficulty == 5:
            print("Thanks for playing! Goodbye!")
            break
        
        lower, upper, max_guesses = set_range(difficulty)
        if lower is None:
            break
        
        ran_num = random.randint(lower, upper)
        cnt = 0

        print(f"\n{player_name}, I have selected a number between {lower} and {upper}. You have {max_guesses} guesses to find it!")

        while cnt < max_guesses:
            try:
                user_inp = input("Enter your guess (or type 'exit' to quit): ")
                if user_inp.lower() == 'exit':
                    print("You have chosen to exit the game.")
                    return
                user_inp = int(user_inp)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            cnt += 1

            if user_inp == ran_num:
                print(f"Congratulations, {player_name}! You guessed the number in {cnt} attempts.")
                if best_score is None or cnt < best_score:
                    best_score = cnt
                    print("This is your best score!")
                scoreboard[player_name] = best_score
                break
            elif user_inp < ran_num:
                print("My number is higher.")
                if ran_num - user_inp <= (upper - lower) * 0.1:
                    print("Hint: You are very close!")
            else:
                print("My number is lower.")
                if user_inp - ran_num <= (upper - lower) * 0.1:
                    print("Hint: You are very close!")

        if cnt >= max_guesses:
            print(f"Sorry, {player_name}. You've used all {max_guesses} guesses. The number was {ran_num}.")
        
        print(f"Best score so far: {best_score} attempts.")
        print("Current Scoreboard:", scoreboard)
        
        while True:
            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again in ['yes', 'no']:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if play_again != 'yes':
            print("Thanks for playing! See you next time!")
            break

# Main menu to select the game
def main_menu():
    while True:
        print("\nWelcome to the Interactive Games Menu!")
        print("1. Tic-Tac-Toe")
        print("2. Rock-Paper-Scissors")
        print("3. Number Guessing Game")
        print("4. Exit")
        choice = input("Enter the number of the game you want to play: ")

        if choice == '1':
            tic_tac_toe()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            number_guessing_game()
        elif choice == '4':
            print("Thanks for visiting! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()
