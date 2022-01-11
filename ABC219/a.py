import sys
sys.stdin = open('input.txt')
X = int(sys.stdin.readline())

if X < 40:
    print(40-X)
elif X < 70:
    print(70-X)
elif X < 90:
    print(90-X)
else:
    print('expert')