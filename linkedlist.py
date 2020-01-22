class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextnode = None
        

def singly_linked_list(node):
    first = node
    second = node
    
    while second != None and second.nextnode != None:
        first = first.nextnode
        second = second.nextnode.nextnode
        
        if second == first:
            return True
    return False
    
def reverse(head):
    current = head 
    before = None
    nextnode = None
  
    while current:
        nextnode = current.nextnode
        current.nextnode = before
        
        before = current
        current = nextnode
    return before

def merge():
    new_list = []