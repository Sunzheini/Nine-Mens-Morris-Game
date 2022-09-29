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
    DEFAULT_PIECES = 6

    def __init__(self):
        self.__pieces_left = self.DEFAULT_PIECES
        self.selected_row = 0
        self.selected_column = 0
        self.possible_combos = [(0, 0), (0, 3), (0, 6),
                                (1, 1), (1, 3), (1, 5),
                                (2, 2), (2, 3), (2, 4),
                                (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6),
                                (4, 2), (4, 3), (4, 4),
                                (5, 1), (5, 3), (5, 5),
                                (6, 0), (6, 3), (6, 6),
                                ]
        self.player_1_placements = []
        self.player_2_placements = []

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

            if current_player == 1:
                if ((self.selected_row - 1, self.selected_column - 1) not in self.possible_combos) \
                        or ((self.selected_row - 1, self.selected_column - 1) in self.player_1_placements):
                    print("---Not a valid point selected!---\n")
                    self.accept_matrix_rows_and_columns()
                else:
                    self.player_1_placements.append((self.selected_row-1, self.selected_column-1))
                    print(f"You have selected: {self.selected_row}, {self.selected_column}")

            elif current_player == 2:
                if ((self.selected_row - 1, self.selected_column - 1) not in self.possible_combos) \
                        or ((self.selected_row - 1, self.selected_column - 1) in self.player_2_placements):
                    print("---Not a valid point selected!---\n")
                    self.accept_matrix_rows_and_columns()
                else:
                    self.player_2_placements.append((self.selected_row-1, self.selected_column-1))
                    print(f"You have selected: {self.selected_row}, {self.selected_column}")

        except ValueError:
            print("---Input must two integers separated by ', '!---\n")
            self.accept_matrix_rows_and_columns()

    def manage_win_condition(self):
        command = input("Do you have 3 pieces in a row - Y/N?\n")
        if command == 'Y' or command == 'y':
            command2 = input("Select opponent's piece to remove - press two integers separated by ', '. 'c' to cancel\n")
            if command2 == 'c' or command2 == 'C':
                return
            else:
                try:
                    self.selected_row, self.selected_column = [int(i) for i in command2.split(', ')]

                    if current_player == 1:
                        if (self.selected_row - 1, self.selected_column - 1) not in self.player_2_placements:
                            print("---Not a valid opponent's piece selected!---\n")
                            self.manage_win_condition()

                        else:
                            self.player_2_placements.remove((self.selected_row-1, self.selected_column-1))

                    elif current_player == 2:
                        if (self.selected_row - 1, self.selected_column - 1) not in self.player_1_placements:
                            print("---Not a valid opponent's piece selected!---\n")
                            self.manage_win_condition()

                        else:
                            self.player_1_placements.remove((self.selected_row - 1, self.selected_column - 1))

                    print(f"You have selected to remove: {self.selected_row}, {self.selected_column}")
                    return

                except ValueError:
                    print("---Input must two integers separated by ', '!---\n")
                    self.manage_win_condition()

        elif command == 'N' or command == 'n':
            return

    def display_player_placements(self):
        to_print_1 = [(x+1, y+1) for (x, y) in self.player_1_placements]
        to_print_1.sort(key=lambda i: (i[0], i[1]))
        to_print_2 = [(x+1, y+1) for (x, y) in self.player_2_placements]
        to_print_2.sort(key=lambda i: (i[0], i[1]))
        print("Player 1 positions:", end='')
        print(*to_print_1, sep=', ')
        print("Player 2 positions:", end='')
        print(*to_print_2, sep=', ')

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
    # 6 - check if selected place is valid
    new_game.accept_matrix_rows_and_columns()
    new_game.display_player_placements()

    # 7 - check for the 3 x piece condition (using input from player)
    # 8 - select to remove opponent's piece
    # 9 -  check if selection is valid
    # 10 - remove piece
    # 11 - print info about removal
    new_game.manage_win_condition()

# 12 - print final turn info
    # ok

    # 4 - number of pieces left to put ont the board before the turn
    new_game.reduce_pieces_by_1
    print(new_game)  # prints number of pieces left
    if out_of_pieces_flag:
        break

    # 13 - rotate player
    current_player = new_game.rotate_player_order(current_player)
    print(f"(Admin) Player changed to: {current_player}")
    print("-------------------------------------------\n")
    time.sleep(1)

# 14. print final info
print("(Admin) Game finished")
if len(new_game.player_1_placements) > len(new_game.player_2_placements):
    print(f"(Admin) Winner is Player 1")
elif len(new_game.player_1_placements) < len(new_game.player_2_placements):
    print(f"(Admin) Winner is Player 2")
else:
    print(f"(Admin) The game is a draw!")

# + testing
