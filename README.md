# Problem Set 11.2 - Linked Lists

## Directions
Answer short response questions directly within this document. Format your responses with proper Markdown. Complete code challenges in `linkedlist.py`.

### Short Response
**1. What are the tradeoffs between linked lists and arrays?**
  + Linked lists are accessed sequencially while arrays can be accessed randomly. Its more efficient to use arrays if you want to read data more than you want to write to memory, while linked lists make it easier to insert data but its more operations to read a given element.

**2. What are the tradeoffs between singly linked lists and doubly linked lists?**
  + Singly linked lists can only be traversed in one direction, starting with the head, while doubly linked lists can be traversed from the tail since its nodes hold a reference to the previous node. This means nodes of a doubly linked list take more space, and manipulations like insertion and deletions are more complex because of the additional reference.

**3. What are the run times for insertion, deletion, and accessing from linked lists?**
  +  Accessing an element from a linked list has a runtime complexity of O(n) while for arrays it is O(1), contant and linear runtimes respectively. Insertion and deletions, however, grow linearly (O(n)) with arrays and contant (O(1)) with linked lists.

**4. What is an abstract data type?**
  + An abstract data  type is a class of object used to store data where the precise functionality and fundamental data structures are abstracted away allowing us to design an interface to interact with it.

### Coding Challenges
1. Implement a `LinkedList` class. Be sure to implement all listed class methods in `linkedlist.py`.

2. Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle". A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.

3. Write a function to reverse a linked list in place. The function will take in the head of the list as input and return the new head of the list.

4. Merge two sorted linked lists and return it as a new list. The new list should
be made by splicing together the nodes of the first two lists.

  For example:
  ```
  Input: 1->2->4, 1->3->4
  Output: 1->1->2->3->4->4
  ```

5. Write a function that removes duplicates from a linked list and returns the list.

