# DataStructure
<img src="https://user-images.githubusercontent.com/26381972/56885655-ef658000-6aa7-11e9-8c9d-493fa3c93f43.png" width="800px">

I summarize quick and simple Python implementation of data structures which is need during the coding tests .

## Array
- Definition of Array : An array is a collection of items stored at contiguous memory locations.
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

<details>
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