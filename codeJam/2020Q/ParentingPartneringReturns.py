def solution(sched, t):
    isC = 0
    isJ = 0
    res = []
    for i in range(N):
        if isC and isC <= sched[i][0]:
            isC = 0
        if isJ and isJ <= sched[i][0]:
            isJ = 0
        if isC == 0:
            res.append(['C', sched[i][2]])
            isC = sched[i][1]
            continue
        if isJ == 0:
            res.append(['J', sched[i][2]])
            isJ = sched[i][1]
            continue
        print("Case #{}: {}".format(t, 'IMPOSSIBLE'))
        break
    else:
        res = sorted(res, key = lambda x : x[1])
        print("Case #{}: {}".format(t, ''.join([r[0] for r in res])))

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    sched = []
    for n in range(N):
        cur = [int(x) for x in input().split(' ')]
        cur.append(n)
        sched.append(cur)
    solution(sorted(sched, key = lambda x : x[0]), t)
