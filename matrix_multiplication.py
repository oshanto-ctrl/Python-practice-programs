"""
Read Three Matrices A, B, and C and test if AB = C
Probablistic Solution, Freivalds test.
"""

from random import randint
from sys import stdin


def readint():
    return int(stdin.realine())

def readarray(typ):
    return list(map(typ, stdin.readlin().split()))

def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == n
        M.append(row)
    return M

def mult(M, v):
    n = len(M)
    return [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]

def freivalds(A, B, C):
    n = len(A)
    x = [randint(0, 1000000) for j in range(n)]
    return mult(A, mult(B, x)) == mult(C, x)

if __name__=="__main__":
    n = readint()
    A = readmatrix(n)
    B = readmatrix(n)
    C = readmatrix(n)
    print(freivalds(A, B, C))

# Competitive programming in python: 128 algorithms.















