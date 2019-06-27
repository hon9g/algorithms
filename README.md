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
4. Language [go](#Language)
    - Choose the right language for your coding interview
    - Why I practice Python & C++
    - Python documentation
    - C++ documentation

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

<details>
<summary>resources:</summary>

- [Harvard CS50 - with korean explanation](https://www.edwith.org/cs50/lecture/22863/)
- [Harvard CS50 - Asymptotic Notation (video)](https://www.youtube.com/watch?v=iOq5kSKqeR4)
- [Big O Notations (general quick tutorial) (video)](https://www.youtube.com/watch?v=V6mKVRU1evU)
- [Big O Notation (and Omega and Theta) - best mathematical explanation (video)](https://www.youtube.com/watch?v=ei-A_wy5Yxw&index=2&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- Skiena:
    - [video](https://www.youtube.com/watch?v=gSyDMtdPNpU&index=2&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
    - [slides](http://www3.cs.stonybrook.edu/~algorith/video-lectures/2007/lecture2.pdf)
- [A Gentle Introduction to Algorithm Complexity Analysis](http://discrete.gr/complexity/)
- [Orders of Growth (video)](https://www.coursera.org/lecture/algorithmic-thinking-1/orders-of-growth-6PKkX)
- [Asymptotics (video)](https://www.coursera.org/lecture/algorithmic-thinking-1/asymptotics-bXAtM)
- [UC Berkeley Big O (video)](https://archive.org/details/ucberkeley_webcast_VIS4YDpuP98)
- [UC Berkeley Big Omega (video)](https://archive.org/details/ucberkeley_webcast_ca3e7UVmeUc)
- [Amortized Analysis (video)](https://www.youtube.com/watch?v=B3SpQZaAZP4&index=10&list=PL1BaGV1cIH4UhkL8a9bJGG356covJ76qN)
- [Illustrating "Big O" (video)](https://www.coursera.org/lecture/algorithmic-thinking-1/illustrating-big-o-YVqzv)
- TopCoder (includes recurrence relations and master theorem):
    - [Computational Complexity: Section 1](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-1/)
    - [Computational Complexity: Section 2](https://www.topcoder.com/community/competitive-programming/tutorials/computational-complexity-section-2/)
- [Cheat sheet](https://github.com/minh364/algorithms/issues/1)

</details>

## Time complexity of Python built-in Functions

### list

| operation  | example | time complexity |
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

| operation  | example | time complexity |
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

### set

| operation  | example | time complexity |
| :-------------: | :-------------: | :-------------: | 
Length        |`len(s)`       | O(1)	     |
Add           |`s.add(x)`     | O(1)	     |
Containment   |`x in/not in s`| O(1)	     | 
Remove        |`s.remove(..)`| O(1)	     | 
Discard       |`s.discard(..)`| O(1)	     | 
Pop           |`s.pop()`     | O(1)	     | 
Clear         |`s.clear()`   | O(1)	     | 
check  |`s != t` `s == t` `s <= t`     | O(len(s))     | 
check          |`s >= t`      | O(len(t))     | 
Union         |`s ∣ t`       | O(len(s)+len(t))
Intersection  |`s & t`        | O(len(s)+len(t))
Difference    |`s - t`        | O(len(s)+len(t))
Symmetric Diff|`s ^ t`        | O(len(s)+len(t))
Copy          |`s.copy()`     | O(N)	     |

### Dictionary

| operation  | example | time complexity |
| :-------------: | :-------------: | :-------------: |
Index         | `d[k]`         | O(1)	     |
Store         | `d[k] = v`     | O(1)	     |
Length        | `len(d)`       | O(1)	     |
Delete        | `del d[k]`     | O(1)	     |
get/setdefault| `d.get(k)`     | O(1)	     |
Pop           | `d.pop(k)`     | O(1)	     | 
Pop item      | `d.popitem()`  | O(1)	     | 
Clear         | `d.clear()`    | O(1)	     | 
View          | `d.keys()`     | O(1)	     | 


more: 
[python wiki-Time complexity](https://wiki.python.org/moin/TimeComplexity)
, [UCI- Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

# Sorting
<img src="https://user-images.githubusercontent.com/26381972/56885690-05734080-6aa8-11e9-9c88-118c73eb68d8.png" width="500px">

- In average, quick sort is faster than merge sort by constant time. 
- In worst case, quick sort have O(n) size of call stack, and in best O(log n) size.



| Algorithm | 
| :-------------: | 
| [Selection sort](https://github.com/minh364/algorithms/blob/master/Sorting/selectionSort.py) | 
| [Quick sort](https://github.com/minh364/algorithms/blob/master/Sorting/quickSort.py) |  
| [Merge sort](https://github.com/minh364/algorithms/blob/master/Sorting/mergeSort.py) | 
| [Counting Sort]() | `O(n+k)` | | additional `O(k)` |



# Language

Questions for choosing the right language for your coding interview
1. Are you interviewing for a language-specific job?
2. What is your best language?
3. How easy is it to solve algorithmic problems in the language?
4. Is the language easy to understand for people who don’t know it?
5. Do they use that language at the company?

<details>
<summary>Resources:</summary>

- [Choose the right language for your coding interview](https://www.byte-by-byte.com/choose-the-right-language-for-your-coding-interview/)
- [Choosing a Programming Language for Interviews](http://blog.codingforinterviews.com/best-programming-language-jobs/)
- [Programming Language Resources](https://github.com/jwasham/coding-interview-university/blob/master/programming-language-resources.md)

</details>

## Python

<details>
<summary>Python Documentations:</summary>

- [Python Official docs](https://docs.python.org/3/library/index.html)

</details>

## C++

<details>
<summary>C++ Documentations:</summary>

- [C++ Official docs](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
- [C++ documentation from devdocs.io ](https://devdocs.io/cpp/)
- [C++ docs and tutorials from cplusplus](http://www.cplusplus.com/)

</details>