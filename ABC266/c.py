import math
import sys
sys.stdin = open('input.txt')
def get_angle(a, b, c):
   angle = -math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))

   return angle + 360 if angle < 0 else angle

def solve(points):
    n = len(points)
    for i in range(len(points)):
      p1 = points[i-2]
      p2 = points[i-1]
      p3 = points[i]
      if get_angle(p1, p2, p3) > 180:
        print('No')
        return
    print('Yes')
    return

points = []
for _ in range(4):
  a, b = map(int, sys.stdin.readline().split())
  points.append((a, b))
solve(points)