# 1. 
class Node:
    def __init__ (self, data = None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(f"{self.data}")
        
class Linkedlist:
    def __init__(self):
        self.head = None
    
# 2. 
def cycle_list(head):
    slow = head
    fast = head
    while fast.next:
        slow = slow.next
        fast = fast.next.next
        if fast is None:
            return False
        if slow == fast:
            return True
    return False
    
# a = Node(1)  
# b = Node(2)
# c = Node(3)
# d = Node(4)

# a.next = b
# b.next = c  
# c.next = d
# d.next = a

# print(cycle_list(a))
        
# 3.
def reverse(head):
    curr = head
    prev = None
    nxt = None
    while curr:
        nxt = curr.next
        prev = curr
        curr = nxt
        
    return prev
    
# a = Node(1)  
# b = Node(2)
# c = Node(3)
# d = Node(4)

# a.next = b
# b.next = c
# c.next = d

# print(reverse(a)==d)
        

# 4. 
def merge(head1, head2):
    curr = head1
    alt = head2
    temp = None
    
    while curr:
        if curr.next.data > alt.data:
            temp = curr.next
            curr.next = alt
            curr = alt.next
            alt = temp
           
        else: 
            curr = curr.next
        return curr

# a = Node(1)
# b = Node(2)
# c = Node (4)

# d = Node(1)
# e = Node(3)
# f = Node(4)

# a.next = b
# b.next = c
# d.next = e
# e.next = f

# print(merge(a, d))
# print(a)
# print(a.next)
# print(a.next.next)
# print(a.next.next.next.next)


# 5. 
def removeDups(head):
    curr = head
    el = []
    prev = None
    while curr:
        if curr.data not in el:
            el.append(curr.data)
            prev = curr
            curr = curr.next
        else:
            prev.next = curr.next
            curr = curr.next
        return curr
        
a = Node(1)
b = Node(2)
c = Node(2)

print(removeDups(a))
print(a)
print(b)
print(c)