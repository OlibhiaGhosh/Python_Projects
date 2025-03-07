def display_board(testboard):
    print(" | " + testboard[1] + " | " + testboard[2] + " | " + testboard[3] + " | ")
    print(" |-" + "-" + "-|-" + "-" + "-|-" + "-" + "-|")
    print(" | " + testboard[4] + " | " + testboard[5] + " | " + testboard[6] + " | ")
    print(" |-" + "-" + "-|-" + "-" + "-|-" + "-" + "-|")
    print(" | " + testboard[7] + " | " + testboard[8] + " | " + testboard[9] + " | ")

def initial_board_display():
    testboard = ["#" , "1", "2", "3", "4", "5", "6", "7", "8","9" ]
    display_board(testboard)

def players_choice():
    availacle_choice = ['X' , 'O']
    marker = ""
    while marker not in availacle_choice:
        marker = input("Enter Player1's choice (X or O): ")
        if marker not in availacle_choice:
            print("Invalid choice!")
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)
def validate_index(index):
    if index not in ["1", "2", "3", "4", "5", "6", "7", "8","9"]:
        return False
    else:
        return True
def input_index (player, index):
    while (not validate_index(index)):
        index = input("Player" + str(player) + ": Where will you want to enter (1-9)? ")
        if (not validate_index(index)):
            print("Enter a valid index!")
    return int(index)
def allocate_choice(player, testboard, player1, player2):
    index = input_index(player, "")
    while testboard[index] in ['X' , 'O']:
        print ("Already taken. Enter another one!")
        index = input_index(player, "")
        if testboard[index] not in ['X' , 'O']:
            break  
    if player==1:
        testboard[index] = player1
    else:
        testboard[index] = player2

def result(testboard, player1):
    row = [1, 4, 7]
    col = [1, 2, 3]
    for i in row:
        if (testboard[i], testboard[i+1], testboard[i+2]) in [('X', 'X', 'X'),('O', 'O', 'O')]:
            symbol = testboard[i]
            winner = ""
            if symbol == player1:
                winner = "Player1"
            else:
                winner = "Player2"
            print("Congratulations! "+winner + " won the match")
            return True
    for j in col:
        if (testboard[j], testboard[j+3], testboard[j+6]) in [('X', 'X', 'X'),('O', 'O', 'O')]:
            symbol = testboard[j]
            winner = ""
            if symbol == player1:
                winner = "Player1"
            else:
                winner = "Player2"
            print("Congratulations! "+winner + " won the match")
            return True
    if (testboard[1], testboard[5], testboard[9]) in [('X', 'X', 'X'),('O', 'O', 'O')]:
        symbol = testboard[1]
        winner = ""
        if symbol == player1:
            winner = "Player1"
        else:
            winner = "Player2"
        print("Congratulations! "+winner + " won the match")
        return True
    elif (testboard[3], testboard[5], testboard[7]) in [('X', 'X', 'X'),('O', 'O', 'O')]:
        symbol = testboard[3]
        winner = ""
        if symbol == player1:
            winner = "Player1"
        else:
            winner = "Player2"
        print("Congratulations! "+winner + " won the match")
        return True
    else:
        return False

def main():
    print ("Welcome to the Tic Tac Toe game :)")
    print("\n")
    print ("Here's your initial tic tac toe board with numbers in every boxes you want to address with: ")
    print("\n")
    initial_board_display()
    testboard = ["#" , " ", " ", " ", " ", " ", " ", " ", " "," " ]
    print("\n")
    print("Now its time to make symbol choice!")
    print("\n")
    player1 , player2 = players_choice()
    print("Player1 will be playing with "+ player1)
    print("Player2 will be playing with "+ player2)
    print("\n")
    start = ""
    while start not in ['Y', 'N']:
        start = input("Are you sure to start the Game (Y/N)? ")
        if start not in ['Y', 'N']:
            print("Enter a valid option!")
    if start == 'N':
        print("Bye! Do come again :)")
        return
    print("\n")
    count = 1
    while count < 10:
        for i in [1, 2]:
            # game_result = result(testboard, player1)
            # if (game_result):
            #     return
            if count <10:
                allocate_choice(i, testboard, player1, player2)
                display_board(testboard)
                if (result(testboard, player1)):
                    return
                count += 1
            elif count >9:
                print("It's a tie! Well played")
                return
            else:
                return
    else:
        if count>9:
            print("It's a tie! Well played")
            return   
main()