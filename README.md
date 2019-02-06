### To-do
- consider various task cases
- get to know Time complexity of Python built in function

# Time Complexity

**Expected time complexity** to perform the operation on the `data limit N` within the `time limit of 1 to 10 seconds` is as follows.

|Limit of Data Size | Expected Time Complexity |
| :-------------: | :-------------: |
| N <= 1,000,000 | `O(N)` or `O( n *log(n))`|
| N <= 10,000 | `O(N**2)`|
| N <= 500 |`O(N**3)`|

## Time complexity of Python built-in Functions

- List

| operation  | example | Big-O |
| :-------------: | :-------------: | :-------------: |
| index | `A[i]` | O(1) |
| store | `A[i] = 0` | O(1) |
| store | `A[i] = 1` | O(1) |
| get length | `len(A)` | O(1) |
| append | `A.append(1)` | O(1) |
| slice | `A[a:b]` | O(k) |
| pop last one | `A.pop()` | O(1) |
| pop not last one | `A.pop(i)` | O(n) |
| remove | `A.remove(i)` | O(n) |
| construction | `list(A)` | O(n) |
| multiply      | `A*k` | O(n)|
| copy | `A.copy()` | O(n) |
| comparision | `a==b` `a!=b` | O(n) |
| search | `x in A` `x not in A` | O(n) |
| extreme value | `min(l)` `max(l)`| O(n)|
| reverse | `A.reverse()`  | O(n) |
| quick sort | `A.sort()` `sorted(A)`     | O(n*log n) |
| min&max | `min(s)`, `max(s)`| O(n) |

- `Dictionary.pop(i)` takes O(1)

more: 
[python wiki-Time complexity](https://wiki.python.org/moin/TimeComplexity)
, [UCI- Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

# Codility Lessons & My solution for each quizzes.
1. [Iterations](https://app.codility.com/programmers/lessons/1-iterations/)
2. [Arrays](https://app.codility.com/programmers/lessons/2-arrays/)
3. [Time Complexity](https://app.codility.com/programmers/lessons/3-time_complexity/)
    - [TapeEquilibrium](https://github.com/minh364/algorithms/blob/master/Codility/TapeEquilibrium.py)
4. [Counting Elements](https://app.codility.com/programmers/lessons/4-counting_elements/)
    - [Missing Integer](https://github.com/minh364/algorithms/blob/master/Codility/MissingInteger.py)
    - [Max Counters](https://github.com/minh364/algorithms/blob/master/Codility/MaxCounters.py)
5. [Prefix Sums](https://app.codility.com/programmers/lessons/5-prefix_sums/)
    - [Passing Cars](https://github.com/minh364/algorithms/blob/master/Codility/PassingCars.py)
    - [Genomic Range Query](https://github.com/minh364/algorithms/blob/master/Codility/GenomicRangeQuery.py)
    - [MinAvgTwoSlice](https://github.com/minh364/algorithms/blob/master/Codility/MinAvgTwoSlice.py)
    - [CountDiv](https://github.com/minh364/algorithms/blob/master/Codility///CountDiv.py)
6. [Sorting](https://app.codility.com/programmers/lessons/6-sorting/)
    - [Distinct](https://github.com/minh364/algorithms/blob/master/Codility//Distinct.py)
    - [MaxProductOfThree](https://github.com/minh364/algorithms/blob/master/Codility/MaxProductOfThree.py)
    - [Triangle](https://github.com/minh364/algorithms/blob/master/Codility//Triangle.py)
    - [NumberOfDiscIntersections](/NumberOfDiscIntersections.py)

7. [Stacks and Queues](https://app.codility.com/programmers/lessons/7-stacks_and_queues/)
    - [Brackets](https://github.com/minh364/algorithms/blob/master/Codility///Brackets.py)
8. Leader
9. Max slice problem
10. Prime and composite numbers
11. Sieve of Eratosthenes
12. Euclidean algorithm
13. Fibonacci numbers
14. Binary search algorithm
15. Caterpillar method
16. Greedy algorithms
17. Dynamic programming

# Sort algorithms
| algorithm | worst | average | Memory |
| :-------------: | :-------------: | :-------------: | :-------------: | 
| [Selection sort](https://github.com/minh364/algorithms/blob/master/Sorting/selectionSort.py) | `O(n**2)` |  |  |
| [Quick sort](https://github.com/minh364/algorithms/blob/master/Sorting/quickSort.py) | `O(n**2)` | `O(n*log n)` | | 
| [Merge sort](https://github.com/minh364/algorithms/blob/master/Sorting/mergeSort.py) | `O(n*log n)` |  |  |
| [Counting Sort]() | `O(n+k)` | | additional `O(k)` |
- In average, quick sort is faster than merge sort by constant time. 
- In worst case, quick sort have O(n) size of call stack, and in best O(log n) size.
