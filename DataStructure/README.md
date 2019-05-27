# DataStructure
As suggested by this repo, [Coding Interview University](https://github.com/jwasham/coding-interview-university)
.

I implemented the DataStructure in `Python`.

<img src="https://user-images.githubusercontent.com/26381972/56885655-ef658000-6aa7-11e9-8c9d-493fa3c93f43.png" width="800px">

## Arrays
- Definition of Array : An array is collection of items stored at contiguous memory locations.
- The idea is to store multiple items of the same type together.
- This makes it easier to calculate the position of each element by simply adding an offset to a base value


- Times for Common Operations

| at | Add | Remove |
| :---: | :---: |:---: |
| Beginning | O(n) | O(n) |
| End | O(1) | O(1) |
| Middle | O(n) | O(n) |

- Linear time to add/remove at an arbitrary location.
- Constant-time to add/remove at the end.
- Constant-time access to any element. _(with address)_


- Definition of Multi-dimensional Array : an array of references to arrays/


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


<details>
<summary>To-Do: Implement an automatically resizing vector.</summary>

[implementation in python](https://github.com/minh364/algorithms/blob/master/DataStructure/1_Array/1_Array.py)

reference: [MS doc: vector Class](https://docs.microsoft.com/en-us/cpp/standard-library/vector-class?view=vs-2019)
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



## Linked-Lists

<details>
<summary>Resources :</summary>

- Description:
    - [Singly Linked Lists (video)](https://www.coursera.org/learn/data-structures/lecture/kHhgK/singly-linked-lists)
    - [CS 61B - Linked Lists 1 (video)](https://archive.org/details/ucberkeley_webcast_htzJdKoEmO0)
    - [CS 61B - Linked Lists 2 (video)](https://archive.org/details/ucberkeley_webcast_-c4I3gFYe3w)
- [C Code (video)](https://www.youtube.com/watch?v=QN6FPiD0Gzo)
    - not the whole video, just portions about Node struct and memory allocation.
- Linked List vs Arrays:
    - [Core Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/rjBs9/core-linked-lists-vs-arrays)
    - [In The Real World Linked Lists Vs Arrays (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/QUaUd/in-the-real-world-lists-vs-arrays)
- [why you should avoid linked lists (video)](https://www.youtube.com/watch?v=YQs6IC-vgmo)
- Gotcha: you need pointer to pointer knowledge:
    (for when you pass a pointer to a function that may change the address where that pointer points)
    This page is just to get a grasp on ptr to ptr. I don't recommend this list traversal style. Readability and maintainability suffer due to cleverness.
    - [Pointers to Pointers](https://www.eskimo.com/~scs/cclass/int/sx8.html)
- Doubly-linked List
    - [Description (video)](https://www.coursera.org/learn/data-structures/lecture/jpGKD/doubly-linked-lists)
    - No need to implement

</details>

<details>
<summary>To-Do: Implement a</summary>

- implement (I did with tail pointer & without):
    - size() - returns number of data elements in list
    - empty() - bool returns true if empty
    - value_at(index) - returns the value of the nth item (starting at 0 for first)
    - push_front(value) - adds an item to the front of the list
    - pop_front() - remove front item and return its value
    - push_back(value) - adds an item at the end
    - pop_back() - removes end item and returns its value
    - front() - get value of front item
    - back() - get value of end item
    - insert(index, value) - insert value at index, so current item at that index is pointed to by new item at index
    - erase(index) - removes node at given index
    - value_n_from_end(n) - returns the value of the node at nth position from the end of the list
    - reverse() - reverses the list
    - remove_value(value) - removes the first item in the list with this value
 
</details>


## Stack
python built-in data structure `list` have methods
`append(x)` to **add** an element at the *end of a list* and
`pop()` to pop an element at the *end of a list*.

|init|push()|pop()|
|:---:|:---:|:---:|
|`stack=list()` or `stack =[]`|`stack.append(x)`|`stack.pop()`|


<details>
<summary>Resources :</summary>

- [Stacks (video)](https://www.coursera.org/learn/data-structures/lecture/UdKzQ/stacks)
- [Using Stacks Last-In First-Out (video)](https://archive.org/details/0102WhatYouShouldKnow/05_01-usingStacksForLast-inFirst-out.mp4)

</details>

<details>
<summary>To-Do: - Will not implement. Implementing with array is trivial. </summary>

But I did it already in Python. [(code)](BOJ\10828스택.py)
 
</details>


## Queue
python built-in data structure `collections.deque` have methods
`append(x)` to **add** an element at the *end of a list* and
`popleft()` to pop an element at the *start of a list*.

`from collections import deque`

|init|push()|pop()|
|:---:|:---:|:---:|
|`stack=deque()`|`stack.append(x)`|`stack.popleft()`|

<details>
<summary>Resources :</summary>

- [Using Queues First-In First-Out(video)](https://archive.org/details/0102WhatYouShouldKnow/05_03-usingQueuesForFirst-inFirst-out.mp4)
- [Queue (video)](https://www.coursera.org/lecture/data-structures/queues-EShpq)
- [Circular buffer/FIFO](https://en.wikipedia.org/wiki/Circular_buffer)
- [Priority Queues (video)](https://archive.org/details/0102WhatYouShouldKnow/05_04-priorityQueuesAndDeques.mp4)

</details>

<details>
<summary>To-Do: Implement Queue using linked-list, with tail pointer:</summary>
    
- enqueue(value) - adds value at position at tail
- dequeue() - returns value and removes least recently added element (front)
- empty()
 
</details>

<details>
<summary>To-Do: Implement Queue using fixed-sized array:</summary>
    
- enqueue(value) - adds item at end of available storage
- dequeue() - returns value and removes least recently added element
- empty()
- full()
 
</details>

_Cost:_
- a bad implementation using linked list where you enqueue at head and dequeue at tail would be O(n)
    because you'd need the next to last element, causing a full traversal each dequeue
- enqueue: O(1) (amortized, linked list and array [probing])
- dequeue: O(1) (linked list and array)
- empty: O(1) (linked list and array)
 

## Hash-Table

<details>
<summary>Resources :</summary>

- Videos:
    - [Hashing with Chaining (video)](https://www.youtube.com/watch?v=0M_kIqhwbFo&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=8)
    - [Table Doubling, Karp-Rabin (video)](https://www.youtube.com/watch?v=BRO7mVIFt08&index=9&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [Open Addressing, Cryptographic Hashing (video)](https://www.youtube.com/watch?v=rvdJDijO2Ro&index=10&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [PyCon 2010: The Mighty Dictionary (video)](https://www.youtube.com/watch?v=C4Kc8xzcA68)
    - [(Advanced) Randomization: Universal & Perfect Hashing (video)](https://www.youtube.com/watch?v=z0lJ2k0sl1g&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp&index=11)
    - [(Advanced) Perfect hashing (video)](https://www.youtube.com/watch?v=N0COwN14gt0&list=PL2B4EEwhKD-NbwZ4ezj7gyc_3yNrojKM9&index=4)

- Online Courses:
    - [Understanding Hash Functions (video)](https://archive.org/details/0102WhatYouShouldKnow/06_02-understandingHashFunctions.mp4)
    - [Using Hash Tables (video)](https://archive.org/details/0102WhatYouShouldKnow/06_03-usingHashTables.mp4)
    - [Supporting Hashing (video)](https://archive.org/details/0102WhatYouShouldKnow/06_04-supportingHashing.mp4)
    - [Language Support Hash Tables (video)](https://archive.org/details/0102WhatYouShouldKnow/06_05-languageSupportForHashTables.mp4)
    - [Core Hash Tables (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/m7UuP/core-hash-tables)
    - [Data Structures (video)](https://www.coursera.org/learn/data-structures/home/week/3)
    - [Phone Book Problem (video)](https://www.coursera.org/learn/data-structures/lecture/NYZZP/phone-book-problem)
    - distributed hash tables:
        - [Instant Uploads And Storage Optimization In Dropbox (video)](https://www.coursera.org/learn/data-structures/lecture/DvaIb/instant-uploads-and-storage-optimization-in-dropbox)
        - [Distributed Hash Tables (video)](https://www.coursera.org/learn/data-structures/lecture/tvH8H/distributed-hash-tables)

</details>

<details>
<summary>To-Do: Implement Hash-Table with array using linear probing: </summary>

- hash(k, m) - m is size of hash table
- add(key, value) - if key already exists, update value
- exists(key)
- get(key)
- remove(key)
 
</details>

## Trees


<details>
<summary>Resources :</summary>

- [Series: Core Trees (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/ovovP/core-trees)
- [Series: Trees (video)](https://www.coursera.org/learn/data-structures/lecture/95qda/trees)
- basic tree construction
- traversal
- manipulation algorithms
- [BFS(breadth-first search) and DFS(depth-first search) (video)](https://www.youtube.com/watch?v=uWL6FJhq5fM)
_BFS:_
- level order (BFS, using queue)
- time complexity: O(n)
- space complexity: best: O(1), worst: O(n/2)=O(n)

_DFS:_
- time complexity: O(n)
- space complexity: best: O(log n) - avg. height of tree worst: O(n)
- inorder (DFS: left, self, right)
- postorder (DFS: left, right, self)
- preorder (DFS: self, left, right)

</details>


### BST
Binary Search Tree

<details>
<summary>Resources :</summary>

 - [Binary Search Tree Review (video)](https://www.youtube.com/watch?v=x6At0nzX92o&index=1&list=PLA5Lqm4uh9Bbq-E0ZnqTIa8LRaL77ica6)
- [Series (video)](https://www.coursera.org/learn/data-structures-optimizing-performance/lecture/p82sw/core-introduction-to-binary-search-trees)
    - starts with symbol table and goes through BST applications
- [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/E7cXP/introduction)
- [MIT (video)](https://www.youtube.com/watch?v=9Jry5-82I68)
- C/C++:
    - [Binary search tree - Implementation in C/C++ (video)](https://www.youtube.com/watch?v=COZK7NATh4k&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=28)
    - [BST implementation - memory allocation in stack and heap (video)](https://www.youtube.com/watch?v=hWokyBoo0aI&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=29)
    - [Find min and max element in a binary search tree (video)](https://www.youtube.com/watch?v=Ut90klNN264&index=30&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [Find height of a binary tree (video)](https://www.youtube.com/watch?v=_pnqMz5nrRs&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=31)
    - [Binary tree traversal - breadth-first and depth-first strategies (video)](https://www.youtube.com/watch?v=9RHO6jU--GU&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=32)
    - [Binary tree: Level Order Traversal (video)](https://www.youtube.com/watch?v=86g8jAQug04&index=33&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [Binary tree traversal: Preorder, Inorder, Postorder (video)](https://www.youtube.com/watch?v=gm8DUJJhmY4&index=34&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [Check if a binary tree is binary search tree or not (video)](https://www.youtube.com/watch?v=yEwSGhSsT0U&index=35&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [Delete a node from Binary Search Tree (video)](https://www.youtube.com/watch?v=gcULXE7ViZw&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P&index=36)
    - [Inorder Successor in a binary search tree (video)](https://www.youtube.com/watch?v=5cPbNCrdotA&index=37&list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)

</details>

<details>
<summary>To-Do: Implement a Binary Search Tree</summary>

insert // insert value into tree
get_node_count // get count of values stored
print_values // prints the values in the tree, from min to max
delete_tree
is_in_tree // returns true if given value exists in the tree
get_height // returns the height in nodes (single node's height is 1)
get_min // returns the minimum value stored in the tree
get_max // returns the maximum value stored in the tree
is_binary_search_tree
delete_value
get_successor // returns next-highest value in tree after given value, -1 if none
 
</details>

### Heap//Priority-Queue//Binary-Heap
visualized as a tree, but is usually linear in storage (array, linked list)

<details>
<summary>Resources :</summary>

- [Heap](https://en.wikipedia.org/wiki/Heap_(data_structure))
- [Introduction (video)](https://www.coursera.org/learn/data-structures/lecture/2OpTs/introduction)
- [Naive Implementations (video)](https://www.coursera.org/learn/data-structures/lecture/z3l9N/naive-implementations)
- [Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/GRV2q/binary-trees)
- [Tree Height Remark (video)](https://www.coursera.org/learn/data-structures/supplement/S5xxz/tree-height-remark)
- [Basic Operations (video)](https://www.coursera.org/learn/data-structures/lecture/0g1dl/basic-operations)
- [Complete Binary Trees (video)](https://www.coursera.org/learn/data-structures/lecture/gl5Ni/complete-binary-trees)
- [Pseudocode (video)](https://www.coursera.org/learn/data-structures/lecture/HxQo9/pseudocode)
- [Heap Sort - jumps to start (video)](https://youtu.be/odNJmw5TOEE?list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&t=3291)
- [Heap Sort (video)](https://www.coursera.org/learn/data-structures/lecture/hSzMO/heap-sort)
- [Building a heap (video)](https://www.coursera.org/learn/data-structures/lecture/dwrOS/building-a-heap)
- [MIT: Heaps and Heap Sort (video)](https://www.youtube.com/watch?v=B7hVxCmfPtM&index=4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
- [CS 61B Lecture 24: Priority Queues (video)](https://archive.org/details/ucberkeley_webcast_yIUFT6AKBGE)
- [Linear Time BuildHeap (max-heap)](https://www.youtube.com/watch?v=MiyLo8adrWw)

</details>

<details>
<summary>To-Do: Implement a max-heap:</summary>

- insert
- sift_up - needed for insert
- get_max - returns the max item, without removing it
- get_size() - return number of elements stored
- is_empty() - returns true if heap contains no elements
- extract_max - returns the max item, removing it
- sift_down - needed for extract_max
- remove(i) - removes item at index x
- heapify - create a heap from an array of elements, needed for heap_sort
- heap_sort() - take an unsorted array and turn it into a sorted array in-place using a max heap
    - note: using a min heap instead would save operations, but double the space needed (cannot do in-place).
 
</details>

## Graphs

<details>
<summary>To-Do: Go for sorting algorithms </summary>

Before start to dig in graphs
 
</details>

<details>
<summary>Resources :</summary>

- Notes:
    - There are 4 basic ways to represent a graph in memory:
        - objects and pointers
        - adjacency matrix
        - adjacency list
        - adjacency map
    - Familiarize yourself with each representation and its pros & cons
    - BFS and DFS - know their computational complexity, their tradeoffs, and how to implement them in real code
    - When asked a question, look for a graph-based solution first, then move on if none.

- MIT(videos):
    - [Breadth-First Search](https://www.youtube.com/watch?v=s-CYnVz-uh4&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=13)
    - [Depth-First Search](https://www.youtube.com/watch?v=AfSk24UTFS8&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=14)

- Skiena Lectures - great intro:
    - [CSE373 2012 - Lecture 11 - Graph Data Structures (video)](https://www.youtube.com/watch?v=OiXxhDrFruw&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=11)
    - [CSE373 2012 - Lecture 12 - Breadth-First Search (video)](https://www.youtube.com/watch?v=g5vF8jscteo&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=12)
    - [CSE373 2012 - Lecture 13 - Graph Algorithms (video)](https://www.youtube.com/watch?v=S23W6eTcqdY&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b&index=13)
    - [CSE373 2012 - Lecture 14 - Graph Algorithms (con't) (video)](https://www.youtube.com/watch?v=WitPBKGV0HY&index=14&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
    - [CSE373 2012 - Lecture 15 - Graph Algorithms (con't 2) (video)](https://www.youtube.com/watch?v=ia1L30l7OIg&index=15&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)
    - [CSE373 2012 - Lecture 16 - Graph Algorithms (con't 3) (video)](https://www.youtube.com/watch?v=jgDOQq6iWy8&index=16&list=PLOtl7M3yp-DV69F32zdK7YJcNXpTunF2b)

- Graphs (review and more):

    - [6.006 Single-Source Shortest Paths Problem (video)](https://www.youtube.com/watch?v=Aa2sqUhIn-E&index=15&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [6.006 Dijkstra (video)](https://www.youtube.com/watch?v=2E7MmKv0Y24&index=16&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [6.006 Bellman-Ford (video)](https://www.youtube.com/watch?v=ozsuci5pIso&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=17)
    - [6.006 Speeding Up Dijkstra (video)](https://www.youtube.com/watch?v=CHvQ3q_gJ7E&list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb&index=18)
    - [Aduni: Graph Algorithms I - Topological Sorting, Minimum Spanning Trees, Prim's Algorithm -  Lecture 6 (video)]( https://www.youtube.com/watch?v=i_AQT_XfvD8&index=6&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm)
    - [Aduni: Graph Algorithms II - DFS, BFS, Kruskal's Algorithm, Union Find Data Structure - Lecture 7 (video)]( https://www.youtube.com/watch?v=ufj5_bppBsA&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=7)
    - [Aduni: Graph Algorithms III: Shortest Path - Lecture 8 (video)](https://www.youtube.com/watch?v=DiedsPsMKXc&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=8)
    - [Aduni: Graph Alg. IV: Intro to geometric algorithms - Lecture 9 (video)](https://www.youtube.com/watch?v=XIAQRlNkJAw&list=PLFDnELG9dpVxQCxuD-9BSy2E7BWY3t5Sm&index=9)
    - [CS 61B 2014 (starting at 58:09) (video)](https://youtu.be/dgjX4HdMI-Q?list=PL-XXv-cvA_iAlnI-BQr9hjqADPBtujFJd&t=3489)~~
    - [CS 61B 2014: Weighted graphs (video)](https://archive.org/details/ucberkeley_webcast_zFbq8vOZ_0k)
    - [Greedy Algorithms: Minimum Spanning Tree (video)](https://www.youtube.com/watch?v=tKwnms5iRBU&index=16&list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - [Strongly Connected Components Kosaraju's Algorithm Graph Algorithm (video)](https://www.youtube.com/watch?v=RpgcYiky7uw)

- Full Coursera Course:
    - [ ] [Algorithms on Graphs (video)](https://www.coursera.org/learn/algorithms-on-graphs/home/welcome)

</details>

<details>
<summary>To-Do: Implement </summary>

- I'll implement:
    - DFS with adjacency list (recursive)
    - DFS with adjacency list (iterative with stack)
    - DFS with adjacency matrix (recursive)
    - DFS with adjacency matrix (iterative with stack)
    - BFS with adjacency list
    - BFS with adjacency matrix
    - single-source shortest path (Dijkstra)
    - minimum spanning tree
    - DFS-based algorithms (see Aduni videos above):
        - check for cycle (needed for topological sort, since we'll check for cycle before starting)
        - topological sort
        - count connected components in a graph
        - list strongly connected components
        - check for bipartite graph
 
</details>