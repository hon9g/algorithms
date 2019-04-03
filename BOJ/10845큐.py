import sys
from collections import deque
'''
collection module에는 deque가 구현되어있다.
append(x)
popleft()
'''
queue = deque()
N = int(sys.stdin.readline())
for n in range(N):
    cmd = sys.stdin.readline().strip().split()
    if 'push' == cmd[0]:
        queue.append(cmd[1])
    elif 'pop' == cmd[0]:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif 'size' == cmd[0]:
        print(len(queue))
    elif 'empty' == cmd[0]:
        if queue:
            print(0)
        else:
            print(1)
    elif 'front' == cmd[0]:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif 'back' == cmd[0]:
        if queue:
            print(queue[-1])
        else:
            print(-1)