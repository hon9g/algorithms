![Python Versions](https://img.shields.io/pypi/pyversions/3.svg?style=flat-square)
## INDEX
1. **Time Complexity**
    - Of **Python built in function** [go](#TimeComplexity)
    - Of **Sorting algorithms** [go](#Sorting)
2. Data Structures with Python [go](#DataStructure)
3. Solutions for programming problems
    - **Codility** [go to solutions](/Codility/README.md)
    - **Google KickStart** [go to solutions](kickStart/README.md)
    - **BOJ** :kr: [go to solutions](BOJ/README.md)

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

![image](https://user-images.githubusercontent.com/26381972/56885321-25eecb00-6aa7-11e9-8366-dc8a5bfc19d8.png)

<details>
<summary>resource:</summary>

- [ ] [Harvard CS50 - Asymptotic Notation (video)](https://www.youtube.com/watch?v=iOq5kSKqeR4)
- [ ] [Big O Notations (general quick tutorial) (video)](https://www.youtube.com/watch?v=V6mKVRU1evU)
- [ ] [Big O Notation (and Omega and Theta) - best mathematical explanation (video)](https://www.youtube.com/watch?v=ei-A_wy5Yxw&index=2&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [ ] Skiena:
    - [video](https://www.youtube.com/watch?v=gSyDMtdPNpU&index=2&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
    - [slides](http://www3.cs.stonybrook.edu/~algorith/video-lectures/2007/lecture2.pdf)
- [ ] [A Gentle Introduction to Algorithm Complexity Analysis](http://discrete.gr/complexity/)
- [ ] [Orders of Growth (video)](https://www.coursera.org/lecture/algorithmic-thinking-1/orders-of-growth-6PKkX)
- [ ] [Asymptotics (video)](https://www.coursera.org/lecture/algorithmic-thinking-1/asymptotics-bXAtM)
- [ ] [UC Berkeley Big O (video)](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
- [ ] [UC Berkeley Big Omega (video)](https://archive.org/details/ucberkeley_webcast_ca3e7UVmeUc)
- [ ] [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [ ] [Illustrating "Big O" (video)](https://www.coursera.org/lecture/algorithmic-thinking-1/illustrating-big-o-YVqzv)
- [ ] TopCoder (includes recurrence relations and master theorem):
    - [Computational Complexity: Section 1](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-1/)
    - [Computational Complexity: Section 2](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-2/)
- [ ] [Cheat sheet](https://github.com/minh364/algorithms/issues/1)

</details>

## Time complexity of Python built-in Functions

### list

| operation  | example | Big-O |
| :-------------: | :-------------: | :-------------: |
| index | `list[i]` | O(1) |
| store | `list[i] = 0` | O(1) |
| store | `list[i] = 1` | O(1) |
| get length | `len(list)` | O(1) |
| append | `list.append(x)` | O(1) |
| slice | `list[a:b]` | O(k) |
| extend | `list.extend(iterable)` `L += K` `L = L + K`| O(k)| 
| pop last one | `list.pop()` | O(1) |
| pop not last one | `list.pop(i)` | O(n) |
| remove | `list.remove(i)` | O(n) |
| construction | `list(iterable)` | O(n) |
| multiply      | `list*k` | O(n)|
| copy | `list.copy()` | O(n) |
| comparision | `list1==list2` `list1!=list2` | O(n) |
| search | `x in list` `x not in list` | O(n) |
| extreme value | `min(list)` `max(list)`| O(n)|
| reverse | `list.reverse()`  | O(n) |
| quick sort | `list.sort()` `sorted(list)`     | O(n*log n) |
| sum | `sum(list)` | O(n) |

**append vs insert vs extend** [more](https://stackabuse.com/append-vs-extend-in-python-lists/)
- If we want to add an element at the **end of a list**, we should use `append`. It is faster and direct.
- If we want to add an element **somewhere within a list**, we should use `insert`. It is the only option for this.
- If we want to **combine** the elements of another iterable to our list, then we should use `extend`. 

- `Dictionary.pop(i)` takes O(1)

### collections.deque

| operation  | example | Big-O |
| :-------------: | :-------------: | :-------------: |
|copy|`copy.copy(deque)`|O(n)|
|append|`.append(x)`|O(1)|
|append left|`.appendleft(x)`|O(1)|
|pop|`.pop()`|O(1)|
|pop left|`.popleft()`|O(1)|
|extend|`.extend(iterable)`|O(k)|
|extend|`extendleft(iterable)`|O(k)|
|rotate|`.rotate(n)`|O(k)|
|remove|`.remove(x)`|O(n)|

more: 
[python wiki-Time complexity](https://wiki.python.org/moin/TimeComplexity)
, [UCI- Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

# Sorting
![image](https://user-images.githubusercontent.com/26381972/56885690-05734080-6aa8-11e9-9c88-118c73eb68d8.png)

- code

| algorithm | worst | average | Memory |
| :-------------: | :-------------: | :-------------: | :-------------: | 
| [Selection sort](https://github.com/minh364/algorithms/blob/master/Sorting/selectionSort.py) | `O(n**2)` |  |  |
| [Quick sort](https://github.com/minh364/algorithms/blob/master/Sorting/quickSort.py) | `O(n**2)` | `O(n*log n)` | | 
| [Merge sort](https://github.com/minh364/algorithms/blob/master/Sorting/mergeSort.py) | `O(n*log n)` |  |  |
| [Counting Sort]() | `O(n+k)` | | additional `O(k)` |
- In average, quick sort is faster than merge sort by constant time. 
- In worst case, quick sort have O(n) size of call stack, and in best O(log n) size.


# DataStructure
![image](https://user-images.githubusercontent.com/26381972/56885655-ef658000-6aa7-11e9-8c9d-493fa3c93f43.png)

I summarize quick and simple Python implementation of data structures which is need during the coding tests .
I will keep updating.

## Stack
python built-in data structure `list` have methods
`append(x)` to **add** an element at the *end of a list* and
`pop()` to pop an element at the *end of a list*.

|init|push()|pop()|
|:---:|:---:|:---:|
|`stack=list()` or `stack =[]`|`stack.append(x)`|`stack.pop()`|

## Queue
python built-in data structure `collections.deque` have methods
`append(x)` to **add** an element at the *end of a list* and
`popleft()` to pop an element at the *start of a list*.

`from collections import deque`

|init|push()|pop()|
|:---:|:---:|:---:|
|`stack=deque()`|`stack.append(x)`|`stack.popleft()`|
