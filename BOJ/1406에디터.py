import sys

def editor(string: str, N: int) -> str:
    """ 시간단축
        알고리즘: 2개의 스택으로 구현해서, 커서를 움직이고 원소를 삽입 삭제할때 O(1)시간 걸리도록 함.
        구현:
            - input() 말고 sys.stdin.readline()
            - list 연산 append는 O(1), expend는 O(k)
        Args:
            string(str): 영어 소문자로 이루어진 길이 100,000이하의 문자열.
            N(int): 입력할 명령어 갯수. 1≤N≤500,000.
        Returns:
            str: 명령에 따라 조작을 끝낸 문자열
        """
    left, right = [x for x in string], []
    for n in range(N):
        cmd = sys.stdin.readline().split()
        if cmd[0] == 'P':
            left.append(cmd[1])
        elif cmd[0] == 'L':
            if left:
                right.append(left.pop())
        elif cmd[0] == 'B':
            if left:
                left.pop()
        elif cmd[0] == 'D':
            if right:
                left.append(right.pop())
    result = ''.join(left) + ''.join(reversed(right))
    return result

def slow_editor(string: str, N: int) -> str:
    """ 시간초과
    반복문안에 있는
    string += cmd[1] 이나 string = string[:cursor] + string[cursor+1:]
    연산이 O(n)시간 걸려서 결과적은로 O(n**2) 시간 걸린다.

    Args:
        string(str): 영어 소문자로 이루어진 길이 100,000이하의 문자열.
        N(int): 입력할 명령어 갯수. 1≤N≤500,000.
    Returns:
        srt: 명령에 따라 조작을 끝낸 문자열
    """
    cursor = len(string)
    for n in range(N):
        cmd = input().split()
        if 0 < cursor:
            if cmd[0] == 'L':
                cursor += -1
            elif cmd[0] == 'B':
                cursor += -1
                string = string[:cursor] + string[cursor+1:]
        if cmd[0] == 'D' and cursor < len(string):
                cursor += 1
        elif cmd[0] == 'P':
            if cursor == len(string)+1:
                string += cmd[1]
            else:
                string = string[:cursor] + cmd[1] + string[cursor:]
                cursor += 1
    return string



if __name__ == '__main__':
    string = sys.stdin.readline().strip()
    N = int(sys.stdin.readline())
    print(editor(string, N))

