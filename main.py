# Nine Men's Morris

"""
Tasks:

1. matrix 7 * 7
2. valid / invalid fields marking

while 1:
3.     which player is it
4.     number of pieces left to put ont the board before the turn
5.     select place
6.     check if selected place is valid
7.     check for the 3 x piece condition
8.         select to remove opponent's piece
9.         check if selection is valid
10.        remove piece
11.        print info about removal
12.    print final turn info
13.    rotate player

14. print final info
"""

# -----------------------------------------------------------------------


# 1 - matrix 7 * 7
import time
import os
from os.path import exists


class PlayingField:
    FIELD_SIZE = 7
    F_SYMBOL = 'O'
    H_SEP = '-'
    V_SEP = '|'

    def __init__(self):
        self.matrix = []

# 2 - valid / invalid fields marking
    @property
    def create_field(self):
        self.matrix.append([self.F_SYMBOL, self.H_SEP, self.H_SEP, self.F_SYMBOL, self.H_SEP, self.H_SEP, self.F_SYMBOL])
        self.matrix.append([self.V_SEP, self.F_SYMBOL, self.H_SEP, self.F_SYMBOL, self.H_SEP, self.F_SYMBOL, self.V_SEP])
        self.matrix.append([self.V_SEP, self.V_SEP, self.F_SYMBOL, self.F_SYMBOL, self.F_SYMBOL, self.V_SEP, self.V_SEP])
        self.matrix.append([self.F_SYMBOL, self.F_SYMBOL, self.F_SYMBOL, ' ', self.F_SYMBOL, self.F_SYMBOL, self.F_SYMBOL])
        self.matrix.append([self.V_SEP, self.V_SEP, self.F_SYMBOL, self.F_SYMBOL, self.F_SYMBOL, self.V_SEP, self.V_SEP])
        self.matrix.append([self.V_SEP, self.F_SYMBOL, self.H_SEP, self.F_SYMBOL, self.H_SEP, self.F_SYMBOL, self.V_SEP])
        self.matrix.append([self.F_SYMBOL, self.H_SEP, self.H_SEP, self.F_SYMBOL, self.H_SEP, self.H_SEP, self.F_SYMBOL])

        print(f"--(Admin) Playing field {self.FIELD_SIZE}x{self.FIELD_SIZE} created--\n")

    @property
    def display_field(self):
        for i in range(len(self.matrix)):
            print(' '.join(self.matrix[i]))
        print()


class Game:
    DEFAULT_PIECES = 9

    def __init__(self):
        self.__pieces_left = self.DEFAULT_PIECES
        self.selected_row = 0
        self.selected_column = 0

    @staticmethod
    def rotate_player_order(player):
        if player == 1:
            return 2
        return 1

    @property
    def reduce_pieces_by_1(self):
        if self.__pieces_left > 0:
            self.__pieces_left -= 1
        if self.__pieces_left == 0:
            global out_of_pieces_flag
            out_of_pieces_flag = True

    def accept_matrix_rows_and_columns(self):
        print("Select row and then column to place the piece, separated by ', ', e.g.: '3, 5': ")
        try:
            self.selected_row, self.selected_column = [int(i) for i in input().split(', ')]
            print(f"You have selected: {self.selected_row}, {self.selected_column}")

        except ValueError:
            print("---Input must two integers separated by ', '!---\n")
            self.accept_matrix_rows_and_columns()

    def check_if_out_of_bounds(self):
        pass



    # def check_if_outside(row, col, rows, cols):           # validaciq dali sa vytre
    #     return row < 0 or col < 0 or row >= rows or col >= cols

    def __str__(self):
        return f"Pieces left: {self.__pieces_left}"

# Logging
# ------------------------------------------------------------------------------------------------
# class Log:
#     FILE_PATH = './logs.txt'
#
#     def __init__(self):
#         pass
#
#     def log(self, text):
#         with open(self.FILE_PATH, 'a') as file:
#             file.write(text)
#             file.write('\n')
#
#     @property
#     def display_log_contents(self):
#         with open(self.FILE_PATH, 'r') as file:
#             print(file.read())
#
#     @property
#     def delete_log_file(self):
#         if exists('./logz.txt'):
#             os.remove('./logz.txt')


# new_log.log('1212')
# new_log.display_log_contents
# new_log.delete_log_file

# Start-up
# -------------------------------------------------------------------------------#
new_field = PlayingField()
new_field.create_field
new_field.display_field
new_game = Game()
current_player = 1
out_of_pieces_flag = False
time.sleep(2)

# later: get player names in a dictionary and print winner name at the end

# Loop
# -------------------------------------------------------------------------------#

while 1:
    # 3 - which player is it
    print(f"(Admin) Current player is: {current_player}")

    # 5 - select place
    new_game.accept_matrix_rows_and_columns()

    # 6 - check if selected place is valid
    new_game.check_if_out_of_bounds()





    # da izpolzvam args i kwargs
    # error handling
    # props

# 4 - number of pieces left to put ont the board before the turn
    new_game.reduce_pieces_by_1
    print(new_game)     # prints number of pieces left
    if out_of_pieces_flag:
        break


# 7 - check for the 3 x piece condition

# 8 -       select to remove opponent's piece

# 9 -       check if selection is valid

# 10 -      remove piece

# 11 -      print info about removal

# 12 - print final turn info

    # 13 - rotate player
    current_player = new_game.rotate_player_order(current_player)
    print(f"(Admin) Player changed to: {current_player}\n")
    time.sleep(2)

# 14. print final info
print("(Admin) Game finished")
print(f"(Admin) Winner is Player {current_player}")

# + testing
