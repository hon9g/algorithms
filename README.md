## INDEX
1. **Time Complexity**
    - Of **Python built in function** [go](#TimeComplexity)
    - Of **Sorting algorithms** [go](#Sorting)
2. Solutions for programming problems
    - **Codility** [solutions](/Codility/README.md)
    - **Google KickStart** [solutions](kickStart/README.md)
    - **BOJ** :kr: [solutions](BOJ/README.md)

### To-Do
- Consider various task cases
- Get to know Time complexity of Python built in function

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
| extend | `A.extend(K)` `A += K` `A = A + K`| O(k)| 
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

- If we want to add an element at the **end of a list**, we should use `append`. It is faster and direct.
- If we want to add an element **somewhere within a list**, we should use `insert`. It is the only option for this.
- If we want to **combine** the elements of another iterable to our list, then we should use `extend`.


- `Dictionary.pop(i)` takes O(1)

more: 
[python wiki-Time complexity](https://wiki.python.org/moin/TimeComplexity)
, [UCI- Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)
[append vs insert vs extend](https://stackabuse.com/append-vs-extend-in-python-lists/)

# Sorting
| algorithm | worst | average | Memory |
| :-------------: | :-------------: | :-------------: | :-------------: | 
| [Selection sort](https://github.com/minh364/algorithms/blob/master/Sorting/selectionSort.py) | `O(n**2)` |  |  |
| [Quick sort](https://github.com/minh364/algorithms/blob/master/Sorting/quickSort.py) | `O(n**2)` | `O(n*log n)` | | 
| [Merge sort](https://github.com/minh364/algorithms/blob/master/Sorting/mergeSort.py) | `O(n*log n)` |  |  |
| [Counting Sort]() | `O(n+k)` | | additional `O(k)` |
- In average, quick sort is faster than merge sort by constant time. 
- In worst case, quick sort have O(n) size of call stack, and in best O(log n) size.

