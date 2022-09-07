#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findBeforeMatrix' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY after as parameter.
#

def findBeforeMatrix(after):
    # Write your code here
    after_rows = len(after)
    after_columns = len(after[0])
    before_matrix = [ [0]*after_columns for i in range(after_rows)]

    for i in range(after_rows):
        for j in range(after_columns):
            before_matrix[i][j] = subtract_any_before(after, i, j)

    # print(after)
    return before_matrix

def get_element_and_handle_negative(after, x, y):
    if x < 0 or y < 0:
        return 0
    else:
        return after[x][y]

def subtract_any_before(after, num_row, num_col):
    x = num_row
    y = num_col
    # current = after[x][y] - (after[x-1][y] + (after[x][y-1]-after[x-1][y-1]))
    # Logic is the above line, using fn to handle index limits
    subtract_by = get_element_and_handle_negative(after, x-1, y) + (get_element_and_handle_negative(after, x, y-1) -get_element_and_handle_negative(after, x-1, y-1))
    current = after[x][y] - subtract_by

    return current


def create_after(before_matrix):
    row = len(before_matrix)
    col = len(before_matrix[0])
    after_matrix = [ [0]*col for i in range(row)]
    for i in range(row):
        for j in range(col):
            after_matrix[i][j] = matrix_sum_until(before_matrix, i, j)
    return after_matrix


def matrix_sum_until(matrix, row, col):  # sums the matrix until col and row.
    s = 0
    for i in range(row + 1):
        for j in range(col + 1):
            s = s + matrix[i][j]
    return s


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # after_rows = int(input().strip())
    # after_columns = int(input().strip())
    before = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # after = [[1, 3], [4, 10]]
    after  = create_after(before)
    print("Original Matrix :", before)

    print("After Matrix ", after)

    print("Generated Before Matrix ", findBeforeMatrix(after))

    # for _ in range(after_rows):
    #     after.append(list(map(int, input().rstrip().split())))
    #
    # result = findBeforeMatrix(after)
    #
    #
    # fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n')
    #
    # fptr.close()
