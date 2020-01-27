# Problem Set 11.2 - Linked Lists

## Directions
Answer short response questions directly within this document. Format your responses with proper Markdown. Complete code challenges in `linkedlist.py`.

### Short Response
**1. What are the tradeoffs between linked lists and arrays?**
- Arrays store elements one after the other, this can be great if you want to look up an element quickly. Arrays have fast reads but slow insterts.
- Linked lists are a collection of nodes. Linked lists store data where ever space is available and store the address of the next element in every node. Linked lists have sequential access, which means to access a specific node you must travel through all nodes. Linked lists have fast insterts but slow reads. 

**2. What are the tradeoffs between singly linked lists and doubly linked lists?**
- Nodes in doubly linked lists point to the next and previous node in the list, which  allow elements two way traversal. However, doubly linked lists occupy more memory than singly as it has 3 fields.

- Singly linked lists have one  pointer to the next node in the list, which means it allows only in one way traversal. Singly linked lists occupy less memory as it has only 2 fields.

**3. What are the run times for insertion, deletion, and accessing from linked lists?**
- Doubly linked lists allow a variety of O(1) time update opperations, insertions, and deletions.
- For Singly linked lists the time complexity of insertion and deletion is O(n).

**4. What is an abstract data type?**
- An abstract datatype is defined by a set of values and set of operations, but the operations are hidden from the user. 

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

