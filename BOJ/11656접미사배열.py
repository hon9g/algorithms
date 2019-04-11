def solution(S):
    """
    Args
        S(str): 길이 1000이하 영문 소문자로 이루어진 문자열.
    Returns:
         `list` of `str`: 사전순으로 정렬된 S의 모든 접미사.
    """
    suffix = []
    for i in range(len(S)):
        suffix.append(S[i:])
    return sorted(suffix)


if __name__ == '__main__':
    S = input()
    for s in solution(S):
        print(s)