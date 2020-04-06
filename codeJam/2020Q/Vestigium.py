T = int(input())

for t in range(1, T + 1):
    N = int(input())
    board = []
    for n in range(1, N + 1):
        row = input().split(' ')
        board.append([int(x) for x in row])
    k = 0
    r = 0
    c = 0
    checkCol = [{'.'} for _ in range(0, N)]
    for i in range(0, N):
        checkRow = {'.'}
        for j in range(0, N):
            if i == j:
                k += board[i][j]
            checkRow.add(board[i][j])
            checkCol[j].add(board[i][j])
            if i == N - 1 and len(checkCol[j]) != N + 1:
                c += 1
        if len(checkRow) != N + 1:
            r += 1
    print("Case #{}: {} {} {}".format(t, k, r, c))
