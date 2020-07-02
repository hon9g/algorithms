import math

T = int(input())
for t in range(1, T + 1):
  N = int(input())
  arr = [int(x) for x in input().split(' ')]
  cumSum = [0]
  for i in range(0, len(arr)):
    cumSum.append(cumSum[i] + arr[i])
  res = 0
  for i in range(1, len(cumSum)):
    for j in range(0, i):
      print(i, j, cumSum[i] - cumSum[j])
      if 0 <= cumSum[i] - cumSum[j] and math.sqrt(cumSum[i] - cumSum[j]) == math.floor(math.sqrt(cumSum[i] - cumSum[j])):
        res += 1
  print("Case #{}: {}".format(t, res))
