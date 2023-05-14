import sys
sys.stdin = open('input.txt')
A = [-1]*(5*10**5)
ptr = 0
note = {}
Q = int(sys.stdin.readline())
X = []
for i in range(Q):
    query = sys.stdin.readline().split()
    if query[0] == 'ADD':
        A[ptr] = int(query[1])
        ptr += 1
    elif query[0] == 'DELETE':
        if ptr > 0:
            ptr -= 1
    elif query[0] == 'SAVE':
        note[query[1]] = ptr
    elif query[0] == 'LOAD':
        if query[1] in note:
            ptr = note[query[1]]
        else:
            ptr = 0

    if ptr > 0:
        X.append(A[ptr-1])
    else:
        X.append(-1)
    # print(i+1)
    # print(A[:(ptr+1)])
    # print(note)
    # print()
print(*X)
