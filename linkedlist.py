class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(f"Node: {self.data}")
        

def print_all_nodes(node:Node):
    current = node
    while current:
        print(current)
        current = current.next
 
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        current = self.head
        s = ""
        s += str(current.data)
        current = current.next
        while current:
            s += '->'
            s += str(current.data)
            current = current.next
        return s
    
    def __len__(self):
        count =0
        current = self.head
        while current:
            count += 1
            current= current.next
        return count
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next
    
    def __contains__(self,data):
        current = self.head
        while current:
            if current.data == data :
                return True
            current = current.next
        return False
        
    def append(self,data):
        node = Node(data)
        
        node.next = self.head
        self.head = node
        
    def delete(self,data):
        current = self.head
        if current.data == data:
            self.head = self.head.next
            
        while current.next:
            if current.next.data == data:
                deleted = current.next
                current.next = current.next.next
                return deleted
            current = current.next
        return None
        
new_list = LinkedList()
new_list.append(2)
new_list.append(3)
new_list.append(4)
new_list.append(5)
new_list.append(6)

'''
print(3 in new_list)
print(100 not in new_list)
print(new_list)

print(new_list.head)
print(new_list.head.next)
'''


def is_cyclic(head: Node) -> bool:
        slow = head
        fast = head
        while fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False   

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
d.next = a
'''
print(is_cyclic(a))
'''

def reverse(head: Node):
    current = head
    previous = None
    nxt = None
    
    while current:
        nxt = current.next
        
        current.next = previous
        
        previous = current
        
        current = nxt
        
    return previous
    
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d

print(reverse(a) == d)