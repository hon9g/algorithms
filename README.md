### To-do
- consider various task cases
- ~~get to know Time complexity of Python built in function~~

# Time complexity of Python built-in Functions

| operation  | example | Big-O |
| :-------------: | :-------------: | :-------------: |
| index | `A[i]` | O(1) |
| slice | `A[a:b]` | O(k) |
| store | `A[i] = 1` | O(1) |
| get length | `len(A)` | O(1) |
| append | `A.append(1)` | O(1) |
| pop last one | `A.pop()` | O(1) |
| pop element i | `A.pop(i)` | O(n) |
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

[more](https://wiki.python.org/moin/TimeComplexity)

# codility lessons
1. Iterations
2. Arrays
3. Time Complexity
    - [TapeEquilibrium](https://github.com/minh364/algorithms/blob/master/Codility/TapeEquilibrium.py)
4. Counting Elements
    - [Missing Integer](https://github.com/minh364/algorithms/blob/master/Codility/MissingInteger.py)
    - [Max Counters](https://github.com/minh364/algorithms/blob/master/Codility/MaxCounters.py)
5. Prefix Sums
    - [Passing Cars](https://github.com/minh364/algorithms/blob/master/Codility/PassingCars.py)
    - [Genomic Range Query](https://github.com/minh364/algorithms/blob/master/Codility/GenomicRangeQuery.py)
    - [MinAvgTwoSlice](https://github.com/minh364/algorithms/blob/master/Codility/MinAvgTwoSlice.py)
6. Sorting
7. Stacks and Queues
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
| algorithm | worst | average | 
| :-------------: | :-------------: | :-------------: | 
| [Selection sort](https://github.com/minh364/algorithms/blob/master/selectionSort.py) | O(n^2) | 
| [Quick sort](https://github.com/minh364/algorithms/blob/master/quickSort.py) | O(n^2) | O(n*log n) | 
| [Merge sort]() | O(n*log n) | 

- In average, quick sort is faster than merge sort by constant time. 
- In worst case, quick sort have O(n) size of call stack, and in best O(log n) size.
