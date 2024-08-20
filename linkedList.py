class Node:
    def __init__(self, value): 
        self.value = value
        self.next = None
        
class LinkedList: 
    def __init__(self):
        self.head = None
    
    def append(self, value):
        node = Node(value)
        if self.head == None:
            self.head = node
            return
        last_node = self.head
        while last_node.next: 
            last_node = last_node.next
        last_node.next = node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.value == key:
            self.head = current_node.next
            current_node = None
            return
        prev_node = None
        while current_node and current_node.value != key:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None
