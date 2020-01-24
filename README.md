# Problem Set 11.2 - Linked Lists

## Directions
Answer short response questions directly within this document. Format your responses with proper Markdown. Complete code challenges in `linkedlist.py`.

### Short Response
**1. What are the tradeoffs between linked lists and arrays?**
  Adding to or deleting from a linked list can be done in O(1) run time complexity, because all that is required is the reassignment of memory locations. However reading from a linked list can only be done sequentially in O(n) run time complexity. On the other hand arrays have random access capabilities, making reading them O(1) run time complexity. However it adding/deleting from an array is an O(n) runtime complexity because data in an array must be stored sequentially requring it to have said amount of space in memory. Without said space, the entire data set must be copied and moved to another location in memory where it does fit.

**2. What are the tradeoffs between singly linked lists and doubly linked lists?**
  Doubly linked lists allow backwards access from one node to the node before it. This allows a linked list to be read backwards. Singly linked lists however on have nodes to only allow forward access, you can only view the next node from your current node.

**3. What are the run times for insertion, deletion, and accessing from linked lists?**
  Insertion: O(1)
  Deletion: O(1)
  Accessing: O(n)

**4. What is an abstract data type?**
  An abstract data type can be considered a model created in reference to an existing data structure. A linked list is an example of this. Its not a built in data structure, but it can be created and does have similar features such as adding/removing data from it.

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

