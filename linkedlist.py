class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(f'Node: (self.data)')
        
def print_all_node(node: Node):
    current = node
    while current:
        print(current)
        current = current.next 

# 1
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def __contain__(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
        return False 
        
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count 
        
    def __repr__(self):
        new_string = ""
        current = self.head
        new_string = str(current.data)
        current = current.next
        
        while current:
            new_string += '->'
            new_string += str(current.data)
            current = current.next
        return new_string
        
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next 
        
    def delete(self, data):
        current = self.head
        while current.next:
            if current.next.data == data:
                deleted = current.next
                current.next = current.next.next
                return deleted
        return None
    
#  2 
def is_cyclic(head: Node) -> bool:
    slow = head
    fast = head 
    while fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False 
  
#  3 
def reverse(head: Node) -> Node:
    current = head
    previous = None
    nxt = None
    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous
    
# 4
def merge(list_1, list_2):
    head = temp = Node()   
    while list_1 or list_2:
        if list_1 and (not list_2 or list_1.data <= list_2.data):
            temp.next = Node(list_1.data)
            list_1 = list_1.next
        else:
            temp.next = Node(list_2.data)
            list_2 = list_2.next
        temp = temp.next
    return head.next
        
# a = Node(1)
# b = Node(2)
# c = Node(3)
# d = Node(4)
# a.next = b
# b.next = c
# c.next = d

  
        
            
# new_list = LinkedList()
# new_list.append(2)
# new_list.append(3)
# print(new_list.head) #2
# print(new_list.next) #3
        
        
        
        