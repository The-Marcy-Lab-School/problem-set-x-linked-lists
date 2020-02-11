# Problem Set 11.2 - Linked Lists

## Directions
Answer short response questions directly within this document. Format your responses with proper Markdown. Complete code challenges in `linkedlist.py`.

### Short Response
**1. What are the tradeoffs between linked lists and arrays?**
    While arrays allow for easy access to random items due to the addresses being known, they also cause a huge inefficency for the memory due to arrays being contiguosly and having to remain as so in the memory. While linked list allows for items to be scattered through out the memory therefore making it easier to store but difficult to retrieve a random index that is not the head. 
**2. What are the tradeoffs between singly linked lists and doubly linked lists?**
    Doubly linked list allow for there to be a reference to the previous and next node while the singly linked list only allow for reference to the next node.
**3. What are the run times for insertion, deletion, and accessing from linked lists?**
    The run times for accessing a node in the linked list is O(n) while to perform an insertion or deletion can be O(1) if the element can be accessed immediately.
**4. What is an abstract data type?**

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

