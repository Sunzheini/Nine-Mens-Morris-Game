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

13. print final info
"""

# -----------------------------------------------------------------------


# 1 - matrix 7 * 7
class Game:
    FILE_PATH = ''

    def __init__(self):
        pass





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

        print(f"--Playing field {self.FIELD_SIZE}x{self.FIELD_SIZE} created--\n")

    @property
    def display_field(self):
        for i in range(len(self.matrix)):
            print(' '.join(self.matrix[i]))


game.start_logging
field = PlayingField()
field.create_field
field.display_field
game.delete_log

# each turn in a log (file handling)




# while 1:
#     pass
# 3 - which player is it

# da izpolzvam args i kwargs
# error handling
# props


# 4 - number of pieces left to put ont the board before the turn
# 5 - select place
# 6 - check if selected place is valid

# def is_outside(row, col, rows, cols):           # validaciq dali sa vytre
#     return row < 0 or col < 0 or row >= rows or col >= cols

# def accept_matrix_rows_and_columns():
#     print("Select rows and columns of the matrix, separated by ', ': ")
#     try:
#         rows, columns = [int(i) for i in input().split(', ')]
#         print(f"You have selected matrix size: {rows}, {columns}")
#
#         create_matrix_with_given_params(rows, columns)
#         print_matrix(matrix)
#
#     except ValueError:
#         print("---Input must two integers separated by ', '!---\n")
#         accept_matrix_rows_and_columns()


# 7 - check for the 3 x piece condition
# 8 -       select to remove opponent's piece
# 9 -       check if selection is valid
# 10 -      remove piece
# 11 -      print info about removal
# 12 - print final turn info


# 13. print final info


# + testing
