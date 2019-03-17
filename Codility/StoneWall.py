""" Note
[Task description & result of this solution](https://app.codility.com/demo/results/trainingBRJED3-48C/)
My approach is simple.
If it is a height that is not in the stack called blocks, then push it.
If the current element H [i] is bigger than blocks [-1] then just push it.
However, If it is smaller then do pop until there are no elements smaller than H [i].
And count how many you pop. cnt of pop + len(blocks) can tell the answer.

As a result, It needs similar approach to the other problems in lesson 7.
But when I first encountered this problem, I could not think of a solution right away.
I took this 1 hour to make this solution,
I spent most of the time do brainstorming with self-drawing graphs and simulate the example on hand.
Writing codes was only takes 14 minutes.
So, It is important to have enough time to verify the algorithm by hand, rather than to start writing code in hurry.
"""

def solution(H):
    """Task Score: 100/100.   Detected time complexity: O(N)

    Cover "Manhattan skyline" using the minimum number of rectangles.

    :param H: An array H is contain the height of the wall of N positive integers.
               H[0] is the height of the wall's left end and
               H[N−1] is the height of the wall's right end.
               N is an integer within the range [1..100,000]
               Each element of H is an integer within the range [1..1,000,000,000].

    :return: The minimum number of blocks needed to build the wall.
    """
    cnt_block = 0
    blocks=[H[0]]
    for i in range(1,len(H)):
        if blocks[-1] != H[i]:
            while blocks and H[i] < blocks[-1]:
                blocks.pop()
                cnt_block += 1
            if not blocks or blocks[-1] < H[i]:
                blocks += [H[i]]
    return cnt_block + len(blocks)

"""
 Example test:   [8, 8, 5, 7, 9, 8, 7, 4, 8]
OK

Your test case: [100, 100, 100]
Returned value: 1

Your test case: [10, 100]
Returned value: 2

Your test case: [100, 10]
Returned value: 2

 Your test case: [100, 10, 100, 10, 100, 1000]
Returned value: 5

Your test case: [100, 10, 100, 10, 100]
Returned value: 4

Your test case: [100, 200, 100, 10, 100]
Returned value: 4
"""