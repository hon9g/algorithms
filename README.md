![Python](https://img.shields.io/badge/Python-3.x-blue)
![JS](https://img.shields.io/badge/JavaScript-es6-orange)

## INDEX
- **Choose Language for coding interview** [:link:](#Language)
- **Consider Time Complexity** [:link:](#TimeComplexity)
- **Implement Data Structures** [:link:](#DataStructure)
- **Implement Sorting algorithms** [:link:](#Sorting)
  - Quick Sort
  - Merge Sort
  - Bubble Sort
  - Insertion Sort
  - Selection Sort
  - Counting Sort
- **Problem solving**
  - LeetCode [:link:](https://github.com/hon9g/algorithms/tree/master/LeetCode)
  - Codility [:link:](https://github.com/hon9g/algorithms/tree/master/Codility)
  - Google KickStart [:link:](https://github.com/hon9g/algorithms/tree/master/kickStart)
  - BOJ [:link:](https://github.com/hon9g/algorithms/tree/master//BOJ)
  - Programmers [:link:](https://github.com/hon9g/algorithms/tree/master/Programmers)

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

# Time complexity of Python built-in Functions

## list

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

## collections.deque

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

## set

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

## Dictionary

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

## Quick Sort

|| time complexity | space complexity |
| :-------------: | :-------------: | :-------------: |
| **average** |`O(N log N)` | 
| **worst** |`O(N^2)` | `O(log N)`

```Python
# space complexity in worst case: O(N)
def quickSort(self, nums: List[int]) -> List[int]:
    if len(nums) < 2: return nums
    pivot = nums[-1]
    lower = [ x for x in nums if x < pivot ]
    same = [ x for x in nums if x == pivot ]
    higher = [ x for x in nums if x > pivot ]
    return self.quickSort(lower)+ same + self.quickSort(higher)
```

```JavaScript
const quickSort = (nums) => {
    if (nums.length < 2) {
        return nums
    }
    const pivot = nums[0]
    const less = nums.filter(x => x < pivot)
    const greater = nums.filter(x => x > pivot)
    const same = nums.filter(x => x === pivot)
    return [...quickSort(less), ...same, ...quickSort(greater)]
}
```

## Merge Sort

|| time complexity | space complexity |
| :-------------: | :-------------: | :-------------: |
| **average** |`O(N log N)` | 
| **worst** |`O(N log N)` | `O(N)`

```Python
def mergeSort(self, nums: List[int]) -> List[int]:
    if len(nums) < 2: return nums
    mid = len(nums) // 2
    a, b = self.mergeSort(nums[:mid]), self.mergeSort(nums[mid:])
    i, j, res = 0, 0, []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    res = res + a[i:] if i < len(a) else res
    res = res + b[j:] if j < len(b) else res
    return res
```
```JavaScript
const mergeSort = (nums) => {
    if (nums.length < 2) {
        return nums
    }
    const mid = Math.floor(nums.length/2)
    const [a, b] = [mergeSort(nums.slice(0, mid)), mergeSort(nums.slice(mid))]
    const sortedNums = []
    let i = 0, j = 0
    while (i < a.length && j < b.length) {
        sortedNums.push(a[i] < b[j] ? a[i++] : b[j++])
    }
    while (i < a.length) {
        sortedNums.push(a[i++])
    }
    while (j < b.length) {
        sortedNums.push(b[j++])
    }
    return sortedNums
}
```

## Bubble Sort

| time complexity | space complexity |
| :-------------: | :-------------: |
`O(N^2)` | `O(1)`

```Python
def bubbleSort(self, nums: List[int]) -> List[int]:
        N = len(nums) - 1
        for i in range(N):
            for j in range(N - i):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]
        return nums
```

## Insertion Sort

| time complexity | space complexity |
| :-------------: | :-------------: |
`O(N^2)` | `O(1)`

```Python
def insertionSort(self, nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        curr = i
        for j in reversed(range(i)):
            if nums[j] <= nums[curr]:
                break
            nums[j], nums[curr] = nums[curr], nums[j]
            curr -= 1
    return nums
```

## Selection Sort

| time complexity | space complexity |
| :-------------: | :-------------: |
`O(N^2)` | `O(1)`

```Python
def selectionSort(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            m = i
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[m]:
                    m = j
            nums[m], nums[i] = nums[i], nums[m]
        return nums
```

## Counting Sort

| time complexity | space complexity |
| :-------------: | :-------------: |
`O(A+K)` | `O(K)`

- condition: we have to know the range of the sorted values.
1. Count the number of each unique elements in the array.
2. Iterate through the array of counters in increasing order.

```Python
def countingSort(A: List[int],k: int) -> : List[int]:
    # A is consisted with integers range 0 to k
    n = len(A)
    # We need additional memory O(k)
    count = [0] * (k+1)
    for i in range(n):
        count[A[i]] += 1
    inx = 0
    for i in range(k+1):
        for j in range(count[i]): # smaller than O(A)
            A[inx] = i
            inx += 1
    return A
```
