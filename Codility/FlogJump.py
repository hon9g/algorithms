'''
X  = position, a frog is currently located
Y = A frog wants to get to a position greater than or equal to Y.   (X <= Y)
D = The small frog always jumps a fixed distance.                   X, Y and D are integers within the range [1..1,000,000,000];

Goal: Count the minimal number of jumps that the small frog must perform to reach its target.
      returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:
  X = 10
  Y = 85
  D = 30

the function should return 3
'''


def solution(X, Y, D):
    # write your code in Python 3.6
    result = (Y-X)//D
    if (Y-X)%D != 0:
        result+= 1
    return result

# Time Complexity: O(1)