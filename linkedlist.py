class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(f" Node: {self.data}")
    
    

node1 = Node('1st Node')
node2 = Node('2nd Node')
node1.next = node2
node2.next = Node('3rd Node')

def print_all_nodes(node: Node):
    current = node
    while current:
        print(current)
        current = current.next

#print_all_nodes(node1)

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __contains__(self,data):
        current = self.head
        while current:
            if  current.data == data:
                return True
            current = current.next
        return False
            
    def __repr__(self):
        current = self.head
        new_str = ''
        new_str += str(current.data)
        current = current.next
        while current:
            new_str += '->'
            new_str += str(current.data)
            current  = current.next
        return new_str
    
    def __iter__(self):
        current = self.head
        while current:
            if current.data % 2 == 0:
                yield current
            current = current.next
        
        
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
        
    def append(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    def delete(self,data):
        current = self.head
        if current.data == data:
            self.head = self.head.next
            return current
        while current.next:
            if current.next.data == data:
                deleted = current.next
                current.next = current.next.next
                return deleted
            current = current.next
        return None

    ######
    def isCycle(node):
    marker1 = node
    marker2 = node
    # print (node.value)
    while marker2 != None and marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode
        if marker2 == marker1:
            return True

    
    return False
    
    ######


    def reverse(node):
        current = node
        prev = None
        nextNode = None

        while current:
            nextNode = current.nextnode
            current.nextnode = prev
            prev = current
            current = nextNode
        return prev

    #####
    def merge(head1: Node, head2: Node):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
        
    tail = Node()
    while not(head1 is None or head2 is None):
        if head1.data < head2.data:
            current = head1
            head1 = head1.next
        else:
            current = head2
            head2 = head2.next
        tail.next = current
        tail = tail.next
    tail.next = head1 or head2
    return tail.next
    ######
    def remove_duplicates(head: Node)-> list:
    current = head
    prev = None
    dic = {}
    
    while current:
        if current.data in dic:
            
            prev.next = current.next
            current = None
        else:
            
            dic[current.data] = 1
            prev = current
        current = prev.next
