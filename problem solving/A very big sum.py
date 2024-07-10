#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    
    sum = 0 #Inisiasi Sum = 0 Untuk menampung nilai
    for i in (ar): #Perulangan terhadap "ar" ditampung pada vaiable i
        sum = sum + i #Sum menampung hasil perulangan i
    return sum #Mengembalikan nilai sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
