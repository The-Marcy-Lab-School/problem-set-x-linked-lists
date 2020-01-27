# 1. Implement a `LinkedList` class. Be sure to implement all listed class methods in `linkedlist.py`.
class Linkedlist:
    def __init__(self):
        self.head = None
    
# 2. Given a singly linked list, write a function which takes in the first node in a singly linked list and returns a boolean indicating if the linked list contains a "cycle". A cycle is when a node's next point actually points back to a previous node in the list. This is also sometimes known as a circularly linked list.
def cycle_list(node):
    slow = head
    fast = head
    
# 3. Write a function to reverse a linked list in place. The function will take in the head of the list as input and return the new head of the list.

# 4. Merge two sorted linked lists and return it as a new list. The new list should
# be made by splicing together the nodes of the first two lists.

#   For example:
#   ```
#   Input: 1->2->4, 1->3->4
#   Output: 1->1->2->3->4->4
#   ```

# 5. Write a function that removes duplicates from a linked list and returns the list.