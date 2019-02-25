import time
import tracemalloc

tracemalloc.start()
    # start_time = time.time()
'''
4
4
1 3 3 2
4
9 5 8 3
3
6 1 6
10
1 0 2 9 3 8 4 7 5 6

'''
# ----------------------------
import sys

T = int(input())

for t in range(T):
    N = int(input())
    digits = input()
    digits = [int(s) for s in digits]
    max_long = (N+1)//2
    max_score = 0

    for i in range(N-(max_long-1)):
        score = 0
        for j in range(max_long):
            score += digits[i+j]
        if score > max_score:
            max_score = score

    print("Case #{}: {}".format(t+1, max_score))
    sys.stdout.flush()



# ----------------------------


    # time taking check

    # print("--- %s seconds ---" % (time.time() - start_time))
    # sys.stdout.flush()

# check memory use
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
print("[ memort Top 10 ]")
for stat in top_stats[:10]:
    print(stat)