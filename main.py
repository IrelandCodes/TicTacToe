import os
from helpers import draw_board, check_turn

spots = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
         6: '6', 7: '7', 8: '8', 9: '9'}

playing = True
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