def solution(S):
    """
    Args:
        S(string):  알파벳 소문자로 이루어진 단어.
                    단어의 길이이는 100을 넘지 않는다.
    Return:
        string: 공백으로 구분한 각 알파벳 갯수
    """
    cnt = [0] * 26
    for s in S:
        cnt[ord(s) - ord('a')] += 1
    return cnt

def test():
    """
    >>> solution('baekjoon')
    [1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    import sys
    S = sys.stdin.readline().strip()
    result = ' '.join(str(s) for s in solution(S))
    print(result)
    # test()