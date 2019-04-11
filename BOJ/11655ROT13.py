import re
def solution(S):
    """
    Args:
        S(str): 길이 100 이하의 영어 대문자, 소문자, 공백, 숫자로 이루어진 문자열.
    Return:
        str: 문자열에 포함된 각 알파벳을 13글자씩 밀어서 만든 암호문.
    """
    result = ''
    for s in S:
        if re.match('[^a-zA-Z]', s):
            result += s
        else:
            n_char = ord(s) + 13
            if re.match('[a-z]', s):
                if 122 < n_char:
                    n_char += -26
            elif re.match('[A-Z]', s):
                if 90 < n_char:
                    n_char += -26
            result += chr(n_char)
    return result

def test():
    """
    >>> solution('Mm')
    'Zz'
    >>> solution('Nn')
    'Aa'
    >>> solution('One is 1')
    'Bar vf 1'
    >>> solution('Baekjoon Online Judge')
    'Onrxwbba Bayvar Whqtr'
    """
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    # S = input()
    # print(solution(S))
    test()