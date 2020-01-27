class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        s = ""
        current = self.head
        s += str(current.data)
        urrent = current.next
        while current:
           s += "->"
           s += str(current.data)
           current = current.next
        return s

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
        
    def __iter__(self):
        current = self.head
        while current:
            if current.data % 2 == 0:
                yield current #pass some data
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

    def delete(self, data):
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

# Question 2: Cycle Check
def is_cyclic(head: Node) -> bool:
    slow = head
    fast = head
    while fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True 
    return False

# Question 3: Reverse a Linked List
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

# Question 4: Merge Two Lists
def merge_two_list(head: Node , l1: Node, l2: Node) -> Node:
    #declare all variables 
    head = ListNode(0)
    current = head
    
    smallerNum = 0
    if current.l1 < current.l2:
        smallerNum = current.l1
        l1 = l1.next
    else:
        smallerNum = current.l2
        l2 = l2.next
    
    newNodeList = ListNode(smallerNum)
    current.next = newNodeList
    current = current.next
        
    return head.next 
        # Create linked list : 
    # 10->20->30->40->50 
    list1 = LinkedList() 
    list1.append(10) 
    list1.append(20) 
    list1.append(30) 
    list1.append(40) 
    list1.append(50) 
  
    # Create linked list 2 : 
    # 5->15->18->35->60 
    list2 = LinkedList() 
    list2.append(5) 
    list2.append(15) 
    list2.append(18) 
    list2.append(35) 
    list2.append(60) 
  
    # Create linked list 3 
    list3 = LinkedList() 
  
    list3.head = merge_two_list(list1.head, list2.head) 
  
    print(" Merged Linked List is : ", end="") 
    list3.printList() 
    
    
    
# def remove_dups(head: Node) -> Node:
    # pass

# if __name__ == "__main__":
#     list1 = SinglyLinkedList(range(0, 100, 10))
#     print(list1) # testing repr
#     print(50 in list1, 110 not in list1) # testing contains
#     list1.delete(50) # testing delete
#     print(len(list1) == 9, 50 not in list1) # testing size  
        
    