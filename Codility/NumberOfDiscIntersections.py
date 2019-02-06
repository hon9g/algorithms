'''
평면 위에 N개의 원을 그린다.
원들은 0 to N − 1로 인덱스 매겨진다.

INPUT: array A = N non-negative integers [0..2,147,483,647,
        which represent radiuses반지름들 of the discs.
[0 >= N >= 100,000], O( n *log(n))
A[J] centered at (J,0)
반지름 = A[J]
returns the number of (unordered) pairs of intersecting discs.
return −1 if the number of intersecting pairs exceeds 10,000,000.
'''

'''
'''


def solution(A):
    endpoints = []
    for i, a in enumerate(A):
        endpoints += [(i - a, True), (i + a, False)]

    endpoints.sort(key=lambda x: (x[0], -x[1]))
    print(endpoints)

    intersections, active_discs = 0, 0

    for _, is_beginning in endpoints:
        if is_beginning:
            intersections += active_discs
            active_discs += 1
        else:
            active_discs -= 1

        if intersections > 10E6:
            return -1
    return intersections

solution([1,3,4,2,1,5,1])