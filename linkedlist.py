#Question 1
class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        
#Question 2
def has_cycle(head):
    mark_one = head
    mark_two = head
    
    while mark_one !=  None and mark_two != None:
        mark_one = mark_one.next_node
        mark_two = mark_two.next_node.next_node
        if mark_two == mark_one:
            return True
    return False
    
#Question 3
def reverse_list(head):
    current = head 
    prev_node = None
    next_node = None
    
    while current:
        next_node = current.next_node
        current.next_node = prev_node
        prev_node = current
        current = next_node
    return prev_node


#Question 4
def merge_list(list_one, list_two):
    new_head = None
    current = list_one
    nxt = list_two
    if list_one.value >= list_two.value:
        new_head = list_one
    else:
        new_head = list_two
    
    while nxt:
        
        if current.next_node is None:
            current.next_node = nxt
            
        if current.next_node.value <= nxt.value:
            current = current.next_node
        else:
            hold = current.next_node
            current.next_node = nxt 
            nxt = hold
    return new_head
        
#Question 5

def remove_repeats(head):
    repeat_count = {}
    current = head
    
    while current.next_node:
        if current.next_node.value not in repeat_count:
            repeat_count['current.next_node.value'] = 1
        else:
            repeat_count['current.next_node.value'] += 1
            
    while current.next_node: 
        if repeat_count['current.next_node.value'] > 1:
            repeat_count['current.next_node.value'] -= 1
            current.next_node = current.next_node.next_node

    




    

