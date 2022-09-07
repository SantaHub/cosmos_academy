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
    for i in range(after_rows):
        for j in range(after_columns):
            after[i][j] = subtract_any_before(after, i, j)

    # print(after)
    return after


def subtract_any_before(after, num_row, num_col):
    current = after[num_row][num_col]
    # print("Current Before", current)
    for i in range(num_row + 1):
        for j in range(num_col + 1):
            if (i == num_row and j == num_col):
                continue
            # print("Afte rvalue", after[i][j])
            current -= after[i][j]

    # print("Current after ", current )
    return current


def create_after(before):
    row = len(before)
    col = len(before[0])
    after_matrix = [[0] * col] * row
    for i in range(row):
        for j in range(col):
            after_matrix[i][j] = matrix_sum_until(before, i, j)
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
    before = [[1, 2], [3, 4]]
    after = [[1, 3], [4, 10]]
    print("Created After", create_after(before))

    print("After", after)

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
