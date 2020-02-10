# Question 1: Implement a Linked List
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return f"{self.value}"

class LinkedList():
    def __init__(self, head = None):
        self.head = head

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next_node
        return count

    def __repr__(self):
        if len(self) == 0:
            return 'This list is empty'
        if len(self) == 1:
            return f"{self.head}"
        f = ""
        current = self.head
        while current:
            f += f"{current}->"
            current = current.next_node
        return f + 'None'

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_node

    def __contains__(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next_node
        return False

    def append(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, value):
        if len(self) == 0:
            return 'Cannot delete from empty list'
        if self.head.value == value:
            self.head = self.head.next_node
            return
        d_node = Node()
        d_node.next_node = self.head
        current = d_node
        while current:
            if current.next_node.value == value:
                current.next_node = current.next_node.next_node
                return
            current = current.next_node

#Question 2: Cycle Check
def is_cyclic(head: Node) -> Node:
    fast = head
    slow = head
    while slow:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow == fast:
            return True
    return False

# Question 3: Reverse a Linked List
def reverse(head: Node) -> Node:
    current = head
    pre = None
    nxt = None
    while current:
        nxt = current.next_node
        current.next_node = pre
        pre = current
        current = nxt
    return pre

# Question 4: Merge Two Lists
def merge_two_list(l1: Node, l2: Node) -> Node:
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    d_tail = Node()
    while not (l1 is None or l2 is None):
        if l1.value < l2.value:
            current = l1
            l1 = l1.next
        else:
            current = l2
            l2 = l2.next
        d_tail.next_node = current
        d_tail = d_tail.next_node
    d_tail.next_node = l1 or l2
    return d_tail.next_node


# Question 5: Remove duplicates
def remove_dups(head: Node) -> Node:
    current = head
    while current:
        nxt = current.next_node
        if current.value == nxt.value:
            current.next_node = nxt.next_node
        current = current.next_node
    return head


# For Testing
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next_node = b
b.next_node = c
c.next_node = d
d.next_node = e
