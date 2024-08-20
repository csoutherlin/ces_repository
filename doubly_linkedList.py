class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtFront(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def insert(self, node, data):
        if not node:
            return
        new_node = Node(data)
        new_node.next = node.next
        if node.next:
            node.next.prev = new_node
        node.next = new_node
        new_node.prev = node

    def delete_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def find_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current
            current = current.next
        return None

# Example usage:
dll = DoublyLinkedList()
dll.insertAtFront(4)
dll.insertAtFront(3)
dll.insertAtFront(2)
dll.insertAtFront(1)

# To traverse and print the nodes:
def traverse(head):
    current = head
    while current:
        print(current.data, end=" <-> ")
        current = current.next
    print("None")

traverse(dll.head)  # Output: 1 <-> 2 <-> 3 <-> 4 <-> None
