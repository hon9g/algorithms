class StackForInt(object):
    def __init__(self):
        self.stack = []
        self.cnt = 0

    def push(self, X):
        self.stack += [X]
        self.cnt += 1

    def pop(self):
        if not self.stack:
            return -1
        else:
            self.cnt += -1
            return self.stack.pop()

    def size(self):
        return self.cnt

    def empty(self):
        return 1 if self.size() == 0 else 0

    def top(self):
        return self.stack[-1] if self.size() != 0 else -1


if __name__ == '__main__':
    stack = StackForInt()
    N = int(input())
    for i in range(N):
        cmd = [x for x in input().split()]
        if len(cmd) == 2:
            stack.push(int(cmd[1]))
            continue
        if cmd[0] == 'top':
            print(stack.top())
        if cmd[0] == 'size':
            print(stack.size())
        if cmd[0] == 'pop':
            print(stack.pop())
        if cmd[0] == 'empty':
            print(stack.empty())
