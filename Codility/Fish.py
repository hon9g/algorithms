"""
[Task description & result of this solution](https://app.codility.com/demo/results/trainingYSCJNK-FHP/)
"""
def solution(A, B):
    """
    Score 100%
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
    N = len(A)
    dead = 0
    for i in range(len(B)):
        if B[i] == 1:
            downstream += [A[i]]
        else:
            while downstream != []:
                dead += 1
                if downstream[-1] > A[i]:
                    break
                else:
                    downstream.pop()
    return N-dead


"""Note
At the first attempt, I started to code 
before making sure about what the description say, like where are up and down.
I have to understand the problem clearly and then write the code.

My inattention caused to use two stacks, 
and confuse what fish is to down and to up.
"""

def solution(A, B):
    """
    Score 37%?
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
    N = len(A)
    dead = 0
    for i in range(len(B)):
        print(upstream, downstream)
        if B[i] == 0 and downstream != []:
            upstream = [A[i]] + upstream
        if B[i] == 1:
            downstream += [A[i]]
        if len(downstream) >0 and len(upstream) >0:
            if downstream[-1] < upstream[-1]:
                _ = downstream.pop()
                dead += 1
                print("downstram is smaller", _)
                if downstream == []:
                    upstream = []
            else:
                _ = upstream.pop()
                dead += 1
                print("upstram is smaller", _)
    print(upstream, downstream)
    return N-dead