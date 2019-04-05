from collections import deque

class Deque():
    def __init__(self):
        self.deque = deque()

    def push_front(self, x):
        return self.deque.appendleft(x)

    def push_back(self, x):
        return self.deque.append(x)

    def pop_front(self):
        return self.deque.popleft() if self.deque else -1

    def pop_back(self):
        return self.deque.pop() if self.deque else -1

    def size(self):
        return len(self.deque)

    def empty(self):
        return 1 if not self.deque else 0

    def front(self):
        return self.deque[0] if self.deque else -1

    def back(self):
        return self.deque[-1] if self.deque else -1


if __name__ == '__main__':
    import sys
    N = int(sys.stdin.readline().strip())
    my_deque = Deque()

    for _ in range(N):
        cmd = sys.stdin.readline().strip().split()
        if 'push_front' == cmd[0]:
            my_deque.push_front(cmd[1])
        elif 'push_back' == cmd[0]:
            my_deque.push_back(cmd[1])
        elif 'pop_front' == cmd[0]:
            print(my_deque.pop_front())
        elif 'pop_back' == cmd[0]:
            print(my_deque.pop_back())
        elif 'size' == cmd[0]:
            print(my_deque.size())
        elif 'empty' == cmd[0]:
            print(my_deque.empty())
        elif 'front' == cmd[0]:
            print(my_deque.front())
        elif 'back' == cmd[0]:
            print(my_deque.back())

