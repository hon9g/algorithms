'''
N = 10**9
for i in range(30):
    N = (N/2)
    print(N)
'''
import sys

T = int(input())

for t in range(T):
    A, B = [int(s) for s in input().split(" ")]
    N = int(input())
    for n in range(N):
        guess = (A+B+1)//2
        print(guess) # print line of guessing to stdout
        sys.stdout.flush() # flush stdout
        # string S readline()
        S = input()
        if S == "WRONG_ANSWER":
            # print('error')
            # print('your output was{}'.format(guess))
            quit()
        elif S == 'CORRECT':
            break
        elif S == 'TOO_SMALL':
            A = guess
        elif S == 'TOO_BIG':
            B = guess-1


