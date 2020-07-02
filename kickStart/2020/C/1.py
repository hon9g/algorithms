T = int(input())
for t in range(1, T + 1):
  N, K = [int(x) for x in input().split(' ')]
  arr = [int(x) for x in input().split(' ')]
  cur = K
  res = 0
  for x in arr:
    if cur != x:
      cur = K
    if cur == x:
      cur -= 1
    if cur == 0:
      cur = K
      res += 1
  print("Case #{}: {}".format(t, res))
