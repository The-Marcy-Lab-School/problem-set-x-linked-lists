class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(f'Node: (self.data)')
        
node1 = Node('1st Node')
node2 = Node('2nd Node')
node1.next = node2
node2.next = Node('3rd Node')
front = node1

def print_all_node(node: Node):
    current = node
    while current:
        print(current)
        current = current.next 

print(node1)
print(node1.next)
print(node1.next.next)

class LinkedList:
    def __init__(self):
        pass
    def __append__(self, data):
        se = Node(data)
        node.next = self.head
        self.head = node
        
        
        
        
        
        