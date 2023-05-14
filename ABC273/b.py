import sys
sys.stdin = open('input.txt')

X, K = map(int, sys.stdin.readline().split())

for i in range(K):
    X1 = (X//10**(i+1))*10**(i+1)
    X2 = (X//10**(i+1)+1)*10**(i+1)
    print(X1, X2, X)
    if abs(X-X1) >= abs(X-X2):
        X = X2
    else:
        X = X1
print(X)