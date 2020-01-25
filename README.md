# Problem Set 11.2 - Linked Lists

## Directions
Answer short response questions directly within this document. Format your responses with proper Markdown. Complete code challenges in `linkedlist.py`.

### Short Response
**1. What are the tradeoffs between linked lists and arrays?**
Answer: The tradeoffs between linked lists and arrays allow for random access, array elements are stored in a block of the computer memory. You can use index to access array elements directly and accessing arrays is fast with the constant time complexity of `0(1)`.Linked Lists supports sequential access, which means we have to traverse the entire list. To access the `nth` element of a linked list the the time complexity is `0(n).`

**2. What are the tradeoffs between singly linked lists and doubly linked lists?**
Answer: The tradeoffs between singly linked lists and doubly linked lists are travsering only one way whereas doubly linked list can traverse both ways because each node keeps an explicit reference to the node before and a reference to the node after it

**3. What are the run times for insertion, deletion, and accessing from linked lists?**
Answer: The run times for insertion and deletion is constant `0(1)` and accessing from  linked lists are linear`0(n)` because you will have to traverse the entire to access the element you are looking for.

**4. What is an abstract data type?**
Answer: An abstract data type are definitions of data and operations but do not have implementation details. For example if a user look at his Iphone he will see what his is know as a UI(User Interface) but under the hood of the Iphone, the implementation is just a bunch of class and function that makes the easier and user friendly to use.  

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

