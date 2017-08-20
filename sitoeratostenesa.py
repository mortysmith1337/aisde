#!/usr/bin/env python3
import sys
import math
def eratosthenes(n):
    A = []
    for i in range(2, n+1):
        A.append(True)
    g = int(math.sqrt(n))
    for i in range(2, g+1):
        if(A[i]):
            for j in range(i*i, len(A), i):
                #print("test")
                A[j] = False
    for i in range(2, len(A)):
        if(A[i]==True):
            print(i)


eratosthenes(int(sys.argv[1]))
