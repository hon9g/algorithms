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

<img src="https://user-images.githubusercontent.com/26381972/56885321-25eecb00-6aa7-11e9-8366-dc8a5bfc19d8.png" width="500px">

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
<img src="https://user-images.githubusercontent.com/26381972/56885690-05734080-6aa8-11e9-9c88-118c73eb68d8.png" width="500px">


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
<img src="https://user-images.githubusercontent.com/26381972/56885655-ef658000-6aa7-11e9-8c9d-493fa3c93f43.png" width="800px">

I summarize quick and simple Python implementation of data structures which is need during the coding tests .

## Array
- Definition: 
Contiguous area of memory consisting of equal-size elements indexed by contiguous integers.

- Times for Common Operations

| at | Add | Remove
| :---: | :---: |:---: |
| Beginning | O(n) | O(n) |
| End | O(1) | O(1) |
| Middle | O(n) | O(n) |

- Constant-time access to any element. _(with address)_
- Constant-time to add/remove at the end.
- Linear time to add/remove at an arbitrary location.

<details>
<summary>Resources :</summary>

- [Arrays (video)](https://www.coursera.org/learn/data-structures/lecture/OsBSF/arrays)
- [UC Berkeley CS61B - Linear and Multi-Dim Arrays (video)](https://archive.org/details/ucberkeley_webcast_Wp8oiO_CZZE) (Start watching from 15m 32s)
- [Basic Arrays (video)](https://archive.org/details/0102WhatYouShouldKnow/02_04-basicArrays.mp4)
- [Multi-dim (video)](https://archive.org/details/0102WhatYouShouldKnow/02_05-multidimensionalArrays.mp4)
- [Dynamic Arrays (video)](https://www.coursera.org/learn/data-structures/lecture/EwbnV/dynamic-arrays)
- [Jagged Arrays (video)](https://www.youtube.com/watch?v=1jtrQqYpt7g)
- [Jagged Arrays (video)](https://archive.org/details/0102WhatYouShouldKnow/02_06-jaggedArrays.mp4)
- [Resizing arrays (video)](https://archive.org/details/0102WhatYouShouldKnow/03_01-resizableArrays.mp4)

</details>
<summary>To-Do: Implement an automatically resizing vector.</summary>

- Implement a vector (mutable array with automatic resizing):
  - Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
  - new raw data array with allocated memory
    - can allocate int array under the hood, just not use its features
    - start with 16, or if starting number is greater, use power of 2 - 16, 32, 64, 128
- methods:
  - size() - number of items
  - capacity() - number of items it can hold
  - is_empty()
  - at(index) - returns item at given index, blows up if index out of bounds
  - push(item)
  - insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
  - prepend(item) - can use insert above at index 0
  - pop() - remove from end, return value
  - delete(index) - delete item at index, shifting all trailing elements left
  - remove(item) - looks for value and removes index holding it (even if in multiple places)
  - find(item) - looks for value and returns first index with that value, -1 if not found
  - resize(new_capacity) // private function
    - when you reach capacity, resize to double the size
    - when popping an item, if size is 1/4 of capacity, resize to half
 
</details>

[](add code)

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

# Language

Questions for choosing the right language for your coding interview
1. Are you interviewing for a language-specific job?
2. What is your best language?
3. How easy is it to solve algorithmic problems in the language?
4. Is the language easy to understand for people who don’t know it?
5. Do they use that language at the company?

</details>
<summary>Resources:</summary>

- [Choose the right language for your coding interview](https://www.byte-by-byte.com/choose-the-right-language-for-your-coding-interview/)
- [Choosing a Programming Language for Interviews](http://blog.codingforinterviews.com/best-programming-language-jobs/)
- [Programming Language Resources](https://github.com/jwasham/coding-interview-university/blob/master/programming-language-resources.md)

</details>

## Python
</details>
<summary>Documentations:</summary>


</details>

## C++
<summary>Documentations:</summary>

- [C++ Official](http://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines)
- [C++ documentation from devdocs.io ](https://devdocs.io/cpp/)
- [C++ docs and tutorials from cplusplus](http://www.cplusplus.com/)

</details>