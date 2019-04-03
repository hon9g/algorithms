import sys
from collections import deque
'''
collection module에는 deque가 구현되어있다.
append(x)
popleft()
'''
class Queue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.queue:
            return self.queue.popleft()
        return -1

    def size(self):
        return len(self.queue)

    def empty(self):
        return 1 if not self.queue else 0

    def front(self):
        return self.queue[0] if self.queue else -1

    def back(self):
        if self.queue:
            return self.queue[-1]
        return -1


if __name__ == '__main__':
    queue = Queue()
    N = int(sys.stdin.readline())
    for n in range(N):
        cmd = sys.stdin.readline().strip().split()
        if 'push' == cmd[0]:
            queue.push(cmd[1])
        elif 'pop' == cmd[0]:
            print(queue.pop())
        elif 'size' == cmd[0]:
            print(queue.size())
        elif 'empty' == cmd[0]:
            print(queue.empty())
        elif 'front' == cmd[0]:
            print(queue.front())
        elif 'back' == cmd[0]:
            print(queue.back())