class Node:
    def __init__(self, data):
        self.data = data
        self.nref = None
        self.pref = None


# Class to create different methods of Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Forward Traversing:
    def print_forward_traversal(self):
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            print("Forward Doubly Linked List is:")
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.nref

    # Backward Traversing:
    def print_backward_traversal(self):
        print()
        if self.head is None:
            print("Linked List is empty!")
        else:
            n = self.head
            print("Backward Doubly Linked List is:")
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.pref

    # Inserting node to empty DLL
    def insert_in_empty_DoublyLL(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")

    # Inserting node at the beginning of the DLL
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node

    # Inserting node at the end of the DLL
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    # Insert a node after a given node
    '''
    Cases:
    1) If node is inserted after the last node
    2) insert after rest of the node    
    '''
    def insert_after_given_node(self, data, x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:      # If not the last node
                    n.nref.pref = new_node
                n.nref = new_node

    # Inserting node before a given node
    '''
    Cases:
    1) Whether node is inserted before the first node
    2) before any other node
    '''
    def insert_before_given_node(self, data, x):
        if self.head is None:
            print("LL is empty!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("Given Node is not present in DLL")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = new_node
                n.pref = new_node

DLL = DoublyLinkedList()

DLL.insert_in_empty_DoublyLL(10)
DLL.insert_at_beginning(20)
DLL.insert_at_end(100)
DLL.insert_after_given_node(50,20)
DLL.insert_after_given_node(70,20)

DLL.print_forward_traversal()
DLL.print_backward_traversal()
