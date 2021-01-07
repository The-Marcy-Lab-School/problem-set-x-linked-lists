// Question 1: Implement a Linked List

class Node {
    constructor(data = null){
        this.data = data;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null
    }
    
    appendToTail(data){ // add new Node with data to tail
        let tail = this.head;
        if (!tail) {
          this.head = new Node(data);
        } else {
          while (tail.next !== null) {
            tail = tail.next;
          }
          tail.next = (new Node(data));
        }  
    }

    prependToHead(data){ // add new Node with data to head
        const newHead = new Node(data);
        const currentHead = this.head;
        this.head = newHead;
        if (currentHead) {
          this.head.next = currentHead;
        }
    }
    
    removeHead() { // removed the first Node in the LinkedList and returns its data
        const removedHead = this.head;
        if (!removedHead) {
          return;
        }
        this.head = removedHead.next;
        return removedHead.data;
    }

    contains(data){ // returns true is any Node in the LinkedList contains data, false otherwise
        let currentNode = this.head
        while(currentNode) {
            if(currentNode.data === data){
                return true
            }
            currentNode = currentNode.next
        }
        return false
    }

    length(){ //returns the length of the LinkedList as an integer value
        let currentNode = this.head
        let size = 0;
        while(currentNode) {
            size ++
            currentNode = currentNode.next
        }
        return size
    }
}

// Question 2: Cycle Check
const isCyclic = (headNode) => { //returns a boolean
    let node1 = headNode
    let node2 = headNode.next
    while(node1 && node2) {
        if(node1 === node2) {
            return true
        }
        node1 = node1.next;
        if(node2.next){
            node2 = node2.next.next;
        } else {
            return false;
        }
    }
    return false;
};

// Question 3: Reverse a Linked List
const reverse = (headNode) => { //returns the new headNode
    var node = headNode;
    var previous = null;

    while(node) {
        // save next or you lose it!!!
        var save = node.next;
        // reverse pointer
        node.next = previous;
        // increment previous to current node
        previous = node;
        // increment node to next node or null at end of list
        node = save;
    }
    return previous;   // Change the list head !!!
};

// Question 4: Merge Two Lists
const mergeLists = (head1, head2) => { //returns the headNode
    let node = head1;
    while(node) {
        if(!node.next) {
            node.next = head2;
            break;
        }
        node = node.next
    }
    return head1
};

// Question 5: Remove duplicates
const removeDuplicates = (headNode) => { //returns the headNode
    let obj = {};
    let currentNode = headNode;
    let prev = null;
    while(currentNode){
        if(currentNode.data in obj){
            prev.next = currentNode.next
        } else {
            obj[currentNode.data] = true;
        }
        prev = currentNode
        currentNode = currentNode.next
    }
    return headNode
};

module.exports = {
    Node, LinkedList, isCyclic, reverse, mergeLists, removeDuplicates
}