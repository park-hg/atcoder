from collections import defaultdict
def solution(sell, buy):
  n = len(sell)
  ans = 0
  for bit in range(1<<n):
    now_have = dict()
    now_money = 0
    for i in range(n):
      if bit & (1<<i):
        s, b = sell[i], buy[i]
        if s.isalpha():
          if s in now_have:
            now_have[s] += 1
          else:
            now_have[s] = 1
        else:
          now_money += int(s)
        
        if b.isalpha():
          if b in now_have:
            now_have[b] -= 1
          else:
            now_have[b] = -1
        else:
          now_money -= int(b)

    flag = True
    for k, v in now_have.items():
      if v < 0:
        flag = False
        break
    if flag:
      ans = max(ans, now_money)
  return ans