# Question 1: Implement a Linked List

class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None

    def __repr__(self):
        return f"{self.value} -> {self.next}"

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        rep = "" + self.head.value
        while self.head.next:
            rep += f"-> {self.head.next.value}"
            self.head = self.head.next

    def __len__(self):
        c = 0
        while self.head:
            c += 1
            self.head = self.head.next
        return c

    def __iter__(self):
        while self.head:
            yield self.head
            self.head = self.head.next

    def __contains__(self, data):
        while self.head:
            if self.head.value == data:
                return True
            self.head = self.head.next
        return False

    def append(self, data):
        while self.head:
            self.head = self.head.next
        self.head.next = Node(data)

    def delete(self, node):
        current = self.head
        if self.__len__() == 1:
            if self.head == node:
                self.head = None
        previous = None
        while current:
            previous = current
            current = current.next
            if current == node:
                previous.next == current.next
                current.next = None

# Question 2: Cycle Check
def is_cyclic(head: Node) -> bool:
    fast = head
    slow = head
    while slow:
        slow = slow.next
        fast = fast.next.next
        if slow == next:
            return True
    return False

# Question 3: Reverse a Linked List
def reverse(head: Node) -> Node:
    current = head
    pre = None
    nxt = None
    while current:
        nxt = current.next
        current.next = pre
        pre = current
        current = nxt
    return pre

# Question 4: Merge Two Lists
def merge_two_list(l1: Node, l2: Node) -> Node:
    if l1.value < l2.value:
        head = l1
        cur = l1
        alt = l2
    else:
        head = l2
        cur = l2
        alt = l1
    nxt = cur.next
    while cur:
        if nxt.value > alt.value:
            cur.next = alt
            cur = cur.next
            alt = nxt
            nxt = cur.next
        else:
            cur = cur.next
            nxt = cur.next
    return head

# Question 5: Remove duplicates
def remove_dups(head: Node) -> Node:
    cur = head
    while cur:
        nxt = cur.next
        if cur.value == nxt.value:
            cur.next = nxt.next
        cur = cur.nxt
    return head

if __name__ == "__main__":
    list1 = LinkedList(range(0, 100, 10))
    print(list1) # testing repr
    print(50 in list1, 110 not in list1) # testing contains
    list1.delete(50) # testing delete
    print(len(list1) == 9, 50 not in list1) # testing size
