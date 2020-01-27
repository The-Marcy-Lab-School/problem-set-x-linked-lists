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

def is_cyclic(head: Node) -> bool:
        slow = head
        fast = head
        while fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
            
        return False   

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
    

def merge_lists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    # create dummy node to avoid additional checks in loop
    tail = temp = Node() 
    while not (head1 is None or head2 is None):
        if head1.data < head2.data:
            # remember current low-node
            current = head1
            # follow ->next
            head1 = head1.next
        else:
            # remember current low-node
            current = head2
            # follow ->next
            head2 = head2.next

        # only mutate the node AFTER we have followed ->next
        temp.next = current          
        # and make sure we also advance the temp
        temp = temp.next

    temp.next = head1 or head2

    # return tail of dummy node
    return tail.next

def merge( h1, h2): 
    if (h1 == None): 
        return h2 
    if (h2 == None): 
        return h1 
  
    if (h1.data < h2.data): 
        h1.next = merge(h1.next, h2) 
        return h1 
      
    else: 
        h2.next = merge(h1, h2.next) 
        return h2
        
def remove_duplicates(head):
    current = head
    prev = None
    dic = {}
    while current:
        if current.data in dic:
            # Remove node
            prev.next = current.next
            current = None
        else:
            # Did not see element yet.
            dic[current.data] = 1
            prev = current
        current = prev.next    
