import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
X = list(map(int, sys.stdin.readline().split()))
Y = list(map(int, sys.stdin.readline().split()))
edges = []

for i in range(N):
  edges.append([i+1, N+1, X[i]])
  edges.append([i+1, N+2, Y[i]])

for _ in range(M):
  a, b ,c = map(int, sys.stdin.readline().split())
  edges.append([a, b, c])

edges.sort(key=lambda x:x[-1])

def find_cost():
  def find(x):
    if x == par[x]:
      return x
    return find(par[x])

  def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
      return
    if rank[x] < rank[y]:
      par[x] = y
    else:
      if rank[x] == rank[y]:
        rank[x] += 1
      par[y] = x

  def same(x, y):
    return find(x) == find(y)


  par = [i for i in range(N+3)]
  rank = [0]*(N+3)
  vis1 = set()
  vis2 = set()
  vis3 = set()
  vis4 = set()
  ans1 = 0
  ans2 = 0
  ans3 = 0
  ans4 = 0
  for a, b, cost in edges:

    if not same(a, b):
      unite(a, b)
      if b != N+1 and b != N+2:
        vis1.add(a)
        vis2.add(a)
        vis3.add(a)
        vis4.add(a)
        vis1.add(b)
        vis2.add(b)
        vis3.add(b)
        vis4.add(b)

        ans1 += cost
        ans2 += cost
        ans3 += cost
        ans4 += cost

      elif b == N+1:
        vis1.add(a)
        vis2.add(a)
        vis1.add(b)
        vis2.add(b)


        ans1 += cost
        ans2 += cost


      elif b == N+2:
        vis1.add(a)
        vis3.add(a)
        vis1.add(b)
        vis3.add(b)

        ans1 += cost
        ans3 += cost
  
  if len(vis1) != N+2:
    ans1 = 10**18
  if len(vis2) != N+1:
    ans2 = 10**18
  if len(vis3) != N+1:
    ans3 = 10**18
  if len(vis4) != N:
    ans4 = 10**18
    
  return min(ans1, ans2, ans3, ans4)

print(find_cost())


