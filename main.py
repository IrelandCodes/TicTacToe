import os
from helpers import draw_board, check_turn, check_for_win

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
complete = False
turn = 0
previous_turn = -1

while playing:
    # Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # Let the player know if invalid turn
    if previous_turn == turn:
        print("Sorry, it looks like you have selected in invalid spot, but you can go ahead and select another.")
    previous_turn = turn
    print("Player " + str((turn % 2) +1) + "'s turn: Pick your spot or press q to quit")
    # Get input from player
    choice = input()
    if choice == 'q':
        playing = False
    # Check if player has given a number from 1 - 9
    elif str.isdigit(choice) and int(choice) in spots:
        # Checks if spot has been taken previously
        if not spots[int(choice)] in {'X', 'O'}:
            # If all valid, updates the board
            turn += 1
            spots[int(choice)] = check_turn(turn)
    
    # Check if game has ended (with someone winning or a tie)
    if check_for_win(spots):
        playing = False
        complete = True
    if turn > 8: 
        playing = False

# Draw board for a last time to show result
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

# Print Game Outcome
if complete == True:
    if check_turn(turn) == 'X':
        print('Congratulations Player 1, you went first and you finished first as well! Player 1 Wins!')
    else:
        print('Congratulations Player 2, you were the underdog here but you managed to win! Player 2 Wins!')
else:
    # Tied game
    print("Sorry, you both played well, but not well enough. No Winner :(")

print("Thank you for playing!")
    