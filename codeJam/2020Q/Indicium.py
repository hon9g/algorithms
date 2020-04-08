def getBoardK(N, K):
    board = [[x for x in range(1, N + 1)]]
    while board[0][0] != K // N:
        board[0].append(board[0].pop(0))
    for i in range(N - 1):
        row = [board[i][N - 1]]
        for j in range(N - 1):
            row.append(board[i][j])
        board.append(row)
    for i in range(N):
        print(" ".join([str(x) for x in board[i]]))
    
def getBoard(line):
    
    isSloved = [False]
    board = []
    rows = []
    cols = []
    
    for i in range(N):
        board.append([])
        rows.append(set())
        rows[i].add(line[i])
        for j in range(N):
            if i == j:
                board[i].append(line[i])
                cols.append(set())
                cols[i].add(line[i])
            else:
                board[i].append(0)
    
    def isAvailable(r, c, v):
        if v in rows[r] or v in cols[c]:
            return False
        return True
    
    def place(r, c, v):
        board[r][c] = v
        rows[r].add(v)
        cols[c].add(v)
    
    def remove(r, c, v):
        board[r][c] = 0
        rows[r].remove(v)
        cols[c].remove(v)
    
    def go(r, c):
        print(board)
        if isSloved[0]:
            return
        elif r + 1 == N and c + 1 == N:
            isSloved[0] = True
            return
        else:
            if c + 1 == N and r < N:
                return backtrack(r + 1, 0)
            if r < N:
                return backtrack(r, c + 1)
    
    def backtrack(r, c):
        if board[r][c] == 0:
            for x in range(1, N + 1):
                if isAvailable(r, c, x):
                    place(r, c, x)
                    go(r, c)
                    if not isSloved[0]:
                        remove(r, c, x)
        else:
            go(r, c)
    
    backtrack(0, 0)
    return [isSloved[0], board]
    

    
def find(n, k, nums):
    if len(nums) == n:
        return getBoard(nums) if sum(nums) == k else [False, []]
    for x in range(1, n + 1):
        nums.append(x)
        res = find(n, k, nums)
        if res[0]:
            return res 
        nums.pop()
    return [False, []]

T = int(input())

for t in range(1, T + 1):
    N, K = [int(x) for x in input().split(' ')]
    if K < N or N * N < K:
        print("Case #{}: IMPOSSIBLE".format(t))
        continue
    res = find(N, K, [])
    if res[0]:
        print("Case #{}: POSSIBLE".format(t))
        for i in range(N):
            print(" ".join([str(x) for x in res[1][i]]))
    else:
        print("Case #{}: IMPOSSIBLE".format(t))
        
        