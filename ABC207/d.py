import sys
import math
from typing import Tuple


sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

S, T = [], []

for _ in range(n):
    S.append(tuple(map(int, sys.stdin.readline().split())))

for _ in range(n):
    T.append(tuple(map(int, sys.stdin.readline().split())))

def normalize(M):
    x_mean, y_mean = 0, 0
    for x, y in M:
        x_mean += x
        y_mean += y
    x_mean /= n
    y_mean /= n
    M_new = []
    for x, y in M:
        x -= x_mean
        y -= y_mean
        M_new.append((x,y))
    return M_new


def angle(M, M_new):
    A = []
    for i in range(n):
        angle = math.atan2(M_new[i][1], M_new[i][0])
        length = M_new[i][0]**2 + M_new[i][1]**2
        A.append((M[i][0], M[i][1], length, angle))
    A.sort(key = lambda x: (x[-1], x[-2]))
    return A


S = angle(S, normalize(S))
S = [(x, y) for x, y, _, _ in S]
T = angle(T, normalize(T))
T = [(x, y) for x, y, _, _ in T]


S_len, T_len = [], []

for i in range(n):
    if i < n-1:
        x, y = S[i]
        u, v = S[i+1]
        S_len.append((x-u)**2+(y-v)**2)

        a, b = T[i]
        c, d = T[i+1]
        T_len.append((a-c)**2+(b-d)**2)
    else:
        x, y = S[-1]
        u, v = S[0]
        S_len.append((x-u)**2+(y-v)**2)

        a, b = T[-1]
        c, d = T[0]
        T_len.append((a-c)**2+(b-d)**2)


def check():
    for i in range(n):
        if S_len == T_len[i:]+T_len[:i]:
            return "Yes"
    return "No"

print(check())