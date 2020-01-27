# Problem Set 11.2 - Linked Lists

## Directions
Answer short response questions directly within this document. Format your responses with proper Markdown. Complete code challenges in `linkedlist.py`.

### Short Response
**1. What are the tradeoffs between linked lists and arrays?**
  Arrays:
  Random Access => runs in constant time when searching for an element in it
  Inserting Node => runs in linear time, has to shift all elements in memory and/or move memory location is there is no more space
  Deleting Node => runs in linear time, shift all elements leaving an empty space in memory that can't be used by another object except the array
  
  LinkedList:
  Sequential Access => runs in linear time, has to go through every element in order to find element being searched for
  Inserting Element => runs in constant time, only redirects the reference to the new node
  Deleting Node => runs in contant time, reirects reference to the next node 

**2. What are the tradeoffs between singly linked lists and doubly linked lists?**
SinglyLinkedList:
  * contain a head that is a reference to the first node
  * sequentially accesses the node starting from the head 
  * the last node in the list doesn't have any reference unless its cycled list
  
DoublyLinkedList:
  * contains a header that is a reference to the first node and the next node references the first one
  * sequentially accesses a node starting from the header or the trailer (last node)
  * the last node references the previous node 
**3. What are the run times for insertion, deletion, and accessing from linked lists?**
Insertion: O(1) 
Deletion: O(1)
Access: O(n)
**4. What is an abstract data type?**
An abstract data type is when specific operations are kept "hidden" from user but are still being taken place 

### Coding Challenges

