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

- `Dictionary.pop(i)` takes O(1)

[more](https://wiki.python.org/moin/TimeComplexity)

# codility lessons
- Iterations
- Arrays
- Time Complexity
    - [TapeEquilibrium](https://github.com/minh364/algorithms/blob/master/TapeEquilibrium.py)
- Counting Elements
    - [Missing Integer](https://github.com/minh364/algorithms/blob/master/MissingInteger.py)
    - [Max Counters](https://github.com/minh364/algorithms/blob/master/MaxCounters.py)
- Prefix Sums
    - [Passing Cars](https://github.com/minh364/algorithms/blob/master/PassingCars.py)
- Sorting
- Stacks and Queues
- Leader
- Max slice problem
- Prime and composite numbers
- Sieve of Eratosthenes
- Euclidean algorithm
- Fibonacci numbers
- Binary search algorithm
- Caterpillar method
- Greedy algorithms
- Dynamic programming

# Sort algorithms
| algorithm | worst | average | 
| :-------------: | :-------------: | :-------------: | 
| [Selection sort](https://github.com/minh364/algorithms/blob/master/selectionSort.py) | O(n^2) | 
| [Quick sort](https://github.com/minh364/algorithms/blob/master/quickSort.py) | O(n^2) | O(n*log n) | 
| [Merge sort]() | O(n*log n) | 

- In average, quick sort is faster than merge sort by constant time. 
- In worst case, quick sort have O(n) size of call stack, and in best O(log n) size.
