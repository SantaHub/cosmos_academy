#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMinimumOperations' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING binaryStr as parameter.
#

def getMinimumOperations(binaryStr):
    operations = 0
    # print("binary ", binaryStr)
    for i in range(0, len(binaryStr)):
        sub_str = binaryStr[i:i+2]
        # print("sub Str ", sub_str)
        if sub_str == "10" or sub_str == "1" :
            operations +=2;
            binaryStr = binaryStr.replace(sub_str, "00", 1)
        elif sub_str == "11":
            operations +=1
            binaryStr = binaryStr.replace(sub_str, "00", 1)

        print(binaryStr)

    return operations

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    binaryStr = input()

    result = getMinimumOperations(binaryStr)

    fptr.write(str(result) + '\n')

    fptr.close()
