# Problem Set 11.2 - Linked Lists

## Directions
Answer short response questions directly within this document. Format your responses with proper Markdown. Complete code challenges in `linkedlist.py`.

### Short Response
**1. What are the tradeoffs between linked lists and arrays?**
  Linked lists solve the problem of adding items. They are able to store elements in memory without having to have each element be stored next to eachother, rather store elements in compartments where there is availability. This is why linked list have sequential access, the trade off being in order to find an element, each element prior to it has to be accessed in order to get the address of the target element. Arrays can cause wasted memory if there is not enough memory to store every element next to one another. However, they allow for random access memory which allow you to find a target element faster.

**2. What are the tradeoffs between singly linked lists and doubly linked lists?**
  Singly linked list occupies less memory than doubly linked lists. This is singly linked lists have only 2 fields; data field and next link field, while doubly linked lists have 3 fields; data field, next link field, and previous link field. However traversing through a singly linked list can be done using next node link only. 
**3. What are the run times for insertion, deletion, and accessing from linked lists?**
  Insertion - O(1), constant
  Deletion - O(1), constant
  Accessing - O(n), liner 
  
**4. What is an abstract data type?**
  An abstract data type is a type for objects whose valus is a set of operations. It is abstract because it gibes an implementation-independent view, which means the process provides essentials and hides details.
  
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

