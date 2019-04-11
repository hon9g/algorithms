import re

def solution(S):
    """
    Args:
        S(str): 길이 100 이하의 문자열 영어 소문자, 대문자, 숫자, 공백으로 이루어져있다.
    Returns:
        int: 문자열에 대한 소문자 갯수,
        int: 대문자 갯수,
        int: 숫자 갯수,
        int: 공백의 개수.
    """
    p_lower = re.compile('[a-z]')
    p_upper = re.compile('[A-Z]')
    p_nums = re.compile('[0-9]')
    p_space = re.compile('[\s]')
    return len(p_lower.findall(S)), len(p_upper.findall(S)), len(p_nums.findall(S)), len(p_space.findall(S))


def test():
    """
    >>> solution('This is String')
    (10, 2, 0, 2)
    >>> solution('SPACE    1    SPACE')
    (0, 10, 1, 8)
    >>> solution(' S a M p L e I n P u T     ')
    (5, 6, 0, 16)
    >>> solution('0L1A2S3T4L5I6N7E8')
    (0, 8, 9, 0)
    """
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    # test()
    while 1:
        try:
            S = input()
            result = ' '.join(str(s) for s in solution(S))
            print(result)
        except EOFError:
            break

    """
    `EOFError`:
            Raised when the input() function hits an end-of-file condition (EOF) without reading any data. 
            (N.B.: the io.IOBase.read() and io.IOBase.readline() methods return an empty string when they hit EOF.)
            
    `input`:
             Python 3 input() presents a console prompt to the user and awaits user input, 
             which is then converted to a string and returned as the result of the input() function invocation.
             
             However, Python 2 had a slightly different behavior for input(), 
             as it still prompts the user, but the input the user provides is parsed as Python code and is evaluated as such. 
             To process user input using the Python 3 behavior, 
             
             Python 2 also included the raw_input() function, 
             which behaves the same as the Python 3 input() function.
    
    resource:
    [1](https://airbrake.io/blog/python-exception-handling/eoferror)
    [2](https://docs.python.org/3.7/library/exceptions.html)
    """