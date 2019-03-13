## INDEX
1. [**Time Complexity**](#TimeComplexity)
2. [**Sorting algorithms**](#Sorting)
3. [**Codility Lessons & Solution for each quizzes**](#Codility)
4. [**Solution for Google KickStart**](#KickStart)

### To-do
- consider various task cases
- get to know Time complexity of Python built in function

# TimeComplexity

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
| sum | `sum(l)` | O(n) |

- `Dictionary.pop(i)` takes O(1)

more: 
[python wiki-Time complexity](https://wiki.python.org/moin/TimeComplexity)
, [UCI- Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

# Sorting
| algorithm | worst | average | Memory |
| :-------------: | :-------------: | :-------------: | :-------------: | 
| [Selection sort](https://github.com/minh364/algorithms/blob/master/Sorting/selectionSort.py) | `O(n**2)` |  |  |
| [Quick sort](https://github.com/minh364/algorithms/blob/master/Sorting/quickSort.py) | `O(n**2)` | `O(n*log n)` | | 
| [Merge sort](https://github.com/minh364/algorithms/blob/master/Sorting/mergeSort.py) | `O(n*log n)` |  |  |
| [Counting Sort]() | `O(n+k)` | | additional `O(k)` |
- In average, quick sort is faster than merge sort by constant time. 
- In worst case, quick sort have O(n) size of call stack, and in best O(log n) size.

# Codility
1. [Iterations](https://app.codility.com/programmers/lessons/1-iterations/)
2. [Arrays](https://app.codility.com/programmers/lessons/2-arrays/)
3. [Time Complexity](https://app.codility.com/programmers/lessons/3-time_complexity/)
    - [FlogJump](https://github.com/minh364/algorithms/blob/master/Codility/FlogJump.py)
    - [PermMissingElement](https://github.com/minh364/algorithms/blob/master/Codility/PermMissingElem.py)
    - [TapeEquilibrium](https://github.com/minh364/algorithms/blob/master/Codility/TapeEquilibrium.py)
4. [Counting Elements](https://app.codility.com/programmers/lessons/4-counting_elements/)
    - [FrogRiverOne](https://github.com/minh364/algorithms/blob/master/Codility/FrogRiverOne.py)
    - [Missing Integer](https://github.com/minh364/algorithms/blob/master/Codility/MissingInteger.py)
    - [Max Counters](https://github.com/minh364/algorithms/blob/master/Codility/MaxCounters.py)
5. [Prefix Sums](https://app.codility.com/programmers/lessons/5-prefix_sums/)
    - [PassingCars](https://github.com/minh364/algorithms/blob/master/Codility/PassingCars.py)
    - [GenomicRangeQuery](https://github.com/minh364/algorithms/blob/master/Codility/GenomicRangeQuery.py)
    - [MinAvgTwoSlice](https://github.com/minh364/algorithms/blob/master/Codility/MinAvgTwoSlice.py)
    - [CountDiv](https://github.com/minh364/algorithms/blob/master/Codility/CountDiv.py)
6. [Sorting](https://app.codility.com/programmers/lessons/6-sorting/)
    - [Distinct](https://github.com/minh364/algorithms/blob/master/Codility/Distinct.py)
    - [MaxProductOfThree](https://github.com/minh364/algorithms/blob/master/Codility/MaxProductOfThree.py)
    - [Triangle](https://github.com/minh364/algorithms/blob/master/Codility/Triangle.py)
    - [NumberOfDiscIntersections](/NumberOfDiscIntersections.py)
7. [Stacks and Queues](https://app.codility.com/programmers/lessons/7-stacks_and_queues/)
    - [Fish](https://github.com/minh364/algorithms/blob/master/Codility/Fish.py)
    - [Brackets](https://github.com/minh364/algorithms/blob/master/Codility/Brackets.py)
8. [Leader](https://app.codility.com/programmers/lessons/8-leader/)
    - [Dominator](https://github.com/minh364/algorithms/blob/master/Codility/Dominator.py)
    - [EquiLeader](https://github.com/minh364/algorithms/blob/master/Codility/EquiLeader.py)
9. [Max slice problem](https://app.codility.com/programmers/lessons/9-maximum_slice_problem/)
    - [MaxProfit](https://github.com/minh364/algorithms/blob/master/Codility/MaxProfit.py)
    - [MaxSliceSum](https://github.com/minh364/algorithms/blob/master/Codility/MaxSliceSum.py)
    - [MaxDoubleSliceSum](https://github.com/minh364/algorithms/blob/master/Codility/MaxDoubleSliceSum.py)
10. [Prime and composite numbers](https://app.codility.com/programmers/lessons/10-prime_and_composite_numbers/)
11. [Sieve of Eratosthenes](https://app.codility.com/programmers/lessons/11-sieve_of_eratosthenes/)
12. [Euclidean algorithm](https://app.codility.com/programmers/lessons/12-euclidean_algorithm/)
13. [Fibonacci numbers](https://app.codility.com/programmers/lessons/13-fibonacci_numbers/)
14. [Binary search algorithm](https://app.codility.com/programmers/lessons/14-binary_search_algorithm/)
15. [Caterpillar method](https://app.codility.com/programmers/lessons/15-caterpillar_method/)
16. [Greedy algorithms](https://app.codility.com/programmers/lessons/16-greedy_algorithms/)
17. [Dynamic programming](https://app.codility.com/programmers/lessons/17-dynamic_programming/)

# KickStart
- 2019
    - Practice round
        - [Number Guessing](https://github.com/minh364/algorithms/blob/master/kickStart/)
        - [Mural](https://github.com/minh364/algorithms/blob/master/kickStart/)
