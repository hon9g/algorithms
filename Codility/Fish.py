def solution(A, B):
    """
    Two non-empty arrays A and B consisting of N integers.
    Arrays A and B represent N voracious fish in a river,
    ordered downstream along the flow of the river

    N is an integer within the range [1..100,000]

    :param A:
            - Array A contains the sizes of the fish.
            - Each element of array A is an integer within the range [0..1,000,000,000]
            - The elements of A are all unique and distinct.
    :param B:
            - Array B contains the directions of the fish.
            - Each element of array B is an integer that can have one of [0, 1]
            - 0 represents a fish flowing upstream.
            - 1 represents a fish flowing downstream.

    :return: The number of fish that will stay alive.

            - Two fish meet each other when B[i] = 1 and B[i+1] = 0
            - After they meet bigger fish eats smaller fish.
    """
    downstream = []
    upstream = []
    for i in range(len(B)):
        if B[i] == 1:
            downstream += [A[i]]
        else:
            upstream += [A[i]]
            if len(downstream) >0 and len(upstream) >0:
                if downstream[-1] < upstream[-1]:
                    downstream.pop()
                else:
                    upstream.pop()
    return len(downstream)+len(upstream)

