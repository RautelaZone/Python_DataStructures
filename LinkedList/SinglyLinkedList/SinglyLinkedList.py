class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:

    # Empty List
    def __init__(self):
        self.head = None

    # For printing elements of Linked List
    def printLinkedList(self):
        if self.head is None:
            print("Linked List is Empty!")
            return
        else:
            n = self.head
            while n is not None:
                print(n.data, "--->", end=" ")
                n = n.ref

    # Adding element at the beginning
    def add_element_at_beginning(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node



LL = LinkedList()
LL.add_element_at_beginning(50)
LL.printLinkedList()
