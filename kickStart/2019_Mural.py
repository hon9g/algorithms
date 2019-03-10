'''
Problem

There are N number of sections.
The N number of beauty score is in the given array.
The score is already determined.
- you can choose where to start.
- next day, you should work on next section. (left or right)
- you can complete one painting, the end of the day.
- end of the day one section should be destroyed.
- Only both ends walls or connected to already broken walls are broken.
- Painted can not be broke. because It is water-proof.

4
4
1 3 3 2
4
9 5 8 3
3
6 1 6
10
1 0 2 9 3 8 4 7 5 6
'''

'''
[Mural](https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050ee2/000000000005118a)

We can observe that we will painted ceil(N/2) sections in  the end, 
all these sections would form a contiguous sub-array of the input array.
Since painting and destroying is done alternatively,
it might not be possible to paint any sub-array of our choice.

Small dataset:
An intuitive approach would rely on Dynamic Programming
and try to define a DP state that could encapsulate 
the state of the painted and the destroyed sections at any point in time.

Note that painted section is continuous, and the destroyed sections are prefixes and suffixes of the input array.
Hence, we can define f(i, j, l, r) as the maximum possible achievable score
if i and j are the lengths of the destroyed prefix and suffix, respectively;
whereas l and r denote the left and the right boundaries of painted array.

A recurrence can easily ve derived by considering at most four further possibilitys:
we have 2 ways to extend the mural 

'''
import time
import tracemalloc

# start memory taking check
tracemalloc.start()
    ## time taking should be checked inside of first loop.
    ## move below line.
    # start_time = time.time()
# ----------------------------
'''
Here are my first approach takes P(n**2).
- bacause of scored sub-array should be continuously connected.
- and score are all positive integer.
Just iterate  index 0 to N - max length of possible sub-array.
and check the sum of 0 to length of sub-array, 1 to length of sub-array +1 ... to end.
It works for small dataset, but not for large dataset.
'''
import sys

T = int(input())

for t in range(T):
    N = int(input())
    digits = input()
    digits = [int(s) for s in digits]
    max_long = (N+1)//2
    max_score = 0

    for i in range(N-(max_long-1)):
        score = 0
        for j in range(max_long):
            score += digits[i+j]
        if score > max_score:
            max_score = score

    print("Case #{}: {}".format(t+1, max_score))
    sys.stdout.flush()



# ----------------------------
    # time taking check
    # print("--- %s seconds ---" % (time.time() - start_time))
    # sys.stdout.flush()
# check memory use
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
print("[ memort Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

'''Approach for Large dataset
The solution to the Large dataset relies on an interesting observation 
that all possible contiguous subarrays of length ceil(N/2) are "paintable". 
If we can prove this fact, we can simply do an O(N) rolling window 
approach over all such subarrays and output the maximum possible sum. 

 Let's think of an intuitive way to prove this. 
 Say, if we paint the i-th section on the first day, 
 what could be the smallest possible index of the left boundary of the mural in the worst case? 
To achieve the smallest possible index, 
we will always extend the boundary on the left side; 
and in the worst case the flood can always extend the prefix, 
allowing us to paint only the indices after index ceil(i/2)(inclusive). 
And similarly, there would be an upper limit on the maximum possible index of the right boundary.
This means that given the desirable left boundary of the mural, 
we can figure out the "central point" from which we would begin painting. 
Now, irrespective of the sequence of destructions, 
we can always meet the desirable left boundary by always extending our subarray to the left 
whenever a section on the left is destroyed. 
Similar arguments can be applied to the right boundary.

'''