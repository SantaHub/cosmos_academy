#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findBeforeMatrix' fgpunction below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY after as parameter.
#

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


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    after = []
    after_rows = int(input().strip())
    after_columns = int(input().strip())
    for _ in range(after_rows):
        after.append(list(map(int, input().rstrip().split())))

    result = findBeforeMatrix(after)


    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
