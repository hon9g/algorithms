"""Note
I used a simple idea that just came up after read the problem.


1. If there are '(', then do +1 to variable of count nested parentheses.
   Else if there are ')' do -1.

2. ')' should not come before '('.
   If so. ')' come when a variable of the count is still 0.
   Then return 0.
"""


def solution(S):
    """Task Score 100/100.   Detected time complexity: O(N).

    Determine whether a given string of parentheses (single type) is properly nested.

    :param S: A string S consisting of N characters.
               N is an integer within the range [0..1,000,000]

    :return: Return 1  if string n is properly nested and 0 otherwise.
    """
    nested = 0
    for i in range(len(S)):
        if S[i] == ")":
            if nested == 0:
                return 0
            else:
                nested -= 1
        if S[i] == "(":
            nested += 1
    if nested != 0:
        return 0
    return 1


"""
Example test:   '(()(())())'
OK

Example test:   '())'
OK

Your test case: [')(']
Returned value: 0

Your test case: ['()())']
Returned value: 0

Your test case: ['()((']
Returned value: 0

Your test case: ['A(']
Returned value: 0

Your test case: ['()()()']
Returned value: 1

Your test case: ['((a)aa(()))']
Returned value: 1
"""