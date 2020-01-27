class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(f'{self.data}')

def print_all_nodes(node: Node):
    current = node
    while current:
        print(current)
        current = current.next

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        current = self.head
        new_string = f'{current} '
        while current:
            new_string += f'-> {current.next} '
            current = current.next
        return new_string

    def __len__(self):
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def __iter__(self):
        current = self.head
        while current:
            if current.data % 2 == 0:
                yield current
            current = current.next

    def __contains__(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def append(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def delete(self, node):
        current = self.head
        if current.data == node:
            self.head = self.head.next
            return current
        while current.next:
            if current.next.data == node:
                deleted = current.next
                current.next = current.next.next
                return deleted
            current = current.next
        return None

def is_cyclic(head: Node) -> bool:
    slow = head
    fast = head
    while fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def reverse(head: Node) -> Node:
    current = head
    previous = None
    nxt = None

    while current:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    return previous

def merge_two_list(l1: Node, l2: Node) -> Node:
    placeholder = Node()

    while not (l1 is None or l2 is None):
        if l1.data < l2.data:
            current = l1
            l1 = l1.next
        else:
            current = l2
            l2 = l2.next
        placeholder.next = current
        placeholder = placeholder.next
    placeholder.next = l1 or l2
    return placeholder.next


def remove_duplicates(head: Node) -> Node:
    current = second = head
    linked = []
    while current:
        while second.next:
            if second.next.data == current.data:
                linked.append(current.next)
                second.next = second.next.next
            else:
                second = second.next
        current = second = current.next
    return linked

a = Node(1)
b = Node(2)
c = Node(4)
d = Node(1)
e = Node(3)
f = Node(4)

a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

list1 = LinkedList()

list1.head = a

print(list1)

print(remove_duplicates(list1.head))