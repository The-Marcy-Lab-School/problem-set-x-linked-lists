# Problem Set: Linked Lists

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

Complete code challenges in `linkedList.js`.

Use Test Driven Development to guide you. For JavaScript, run `npm install` to download dependencies. Run `npm test` to run tests locally. Ensure all tests are passing before submitting this problem set.


### Short Response
**1. What are the tradeoffs between linked lists and arrays?**

**2. What are the tradeoffs between singly linked lists and doubly linked lists?**

**3. What is the run times for insertion at the head of a singly linked lists? What about deletion from the tail? What about searching and accessing some value from the singly linked list?**

**4. What is an abstract data type?**

### Coding Challenges
1. Implement a `Node` class and `LinkedList` class. 

2. Given a the head node of a singly linked list, write a function which returns a boolean indicating if the linked list contains a "cycle". A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.

3. Write a function to reverse a linked list in place. The function will take in the head node of the list as an input and return the new head node of the list.

4. Merge two **sorted** linked lists and return it as **a new sorted list**. The new list should be made by splicing together the nodes of the first two lists. 

  For example:
  ```
  Input: 1->2->4, 1->3->4
  Output: 1->1->2->3->4->4
  ```

5. Write a function that removes duplicates from a linked list and returns the head node of the list.
