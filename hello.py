import subprocess as sp

# Board Setup

"""

The variable "user_board" represents the coordinates where the user has already fired in an array.
Every coordinate where the user fires will be changed from 0 to 1.
Every missed shot will appear as an "X" while all accurate shots will appear as an "!".

The variable "enemy_board" represents the coordinates where the enemy ships are located.

"""

user_board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

enemy_board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 0],
    [0, 3, 3, 3, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 4, 4, 0],
    [0, 0, 0, 0, 0, 4, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Display Function

"""

Idea for board design:

---------------------
 | O O O O O O O O |
 | O O O O O O O O |
 | O O O O O O O O |
 | O O O O O O O O |
 | O O O O O O O O |
 | O O O O O O O O |
 | O O O O O O O O |
 | O O O O O O O O |
---------------------

You can change this however you want.

"""

all_hit_points = [
    [2, 1], [2, 2],
    [2, 5], [3, 5],
    [4, 2], [4, 3], [4, 4],
    [6, 5], [6, 6], [6, 7], [7, 6], [7, 7]
]

def display_board(board):
    global all_hit_points
    print("---------------------")
    r = 0; c = 0
    for row in board:
        r += 1; c = 0
        accumulator = " | "
        for element in row:
            c += 1
            if element == 0: accumulator += "O "
            elif [r, c] in all_hit_points: accumulator += "! "
            else: accumulator += "X "
        print(accumulator + "| ")
    print("---------------------")

# Game Logic

message_carry = ""
game_over = False

def check_ship(points):
    ship_destroyed = True
    for point in points:
        if user_board[point[0] - 1][point[1] - 1] == 0:
            ship_destroyed = False
    return ship_destroyed

def game():
    global message_carry
    global game_over
    s1_destroyed = False
    s2_destroyed = False
    s3_destroyed = False
    s4_destroyed = False
    while not game_over:
        print("   Current Board   ")
        display_board(user_board)
        print(message_carry)
        message_carry = ""
        x = int(input("Which row would you like to fire at (1 to 8)? "))
        y = int(input("Which column would you like to fire at (1 to 8)? "))
        user_board[x - 1][y - 1] = 1
        if enemy_board[x - 1][y - 1] != 0: message_carry += "Ship hit!\n"
        s1 = check_ship([[2, 1], [2, 2]])
        s2 = check_ship([[2, 5], [3, 5]])
        s3 = check_ship([[4, 2], [4, 3], [4, 4]])
        s4 = check_ship([[6, 5], [6, 6], [6, 7], [7, 6], [7, 7]])
        if not s1_destroyed and s1: message_carry += "Ship 1 Destroyed!\n"
        elif not s2_destroyed and s2: message_carry += "Ship 2 Destroyed!\n"
        elif not s3_destroyed and s3: message_carry += "Ship 3 Destroyed!\n"
        elif not s4_destroyed and s4: message_carry += "Ship 4 Destroyed!\n"
        if s1 and s2 and s3 and s4: game_over = True
        s1_destroyed = s1; s2_destroyed = s2; s3_destroyed = s3; s4_destroyed = s4
        sp.call("clear", shell=True)
    print("   Current Board   ")
    display_board(user_board)
    print("All ships destroyed!\nGame over!")
    replay = input("Would you like to play again (y/n)? ")
    if replay.lower() == "y" or replay.lower() == "yes": game()

if __name__ == "__main__":
    game()
