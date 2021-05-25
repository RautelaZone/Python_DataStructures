# Class to create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Class to create different methods of Linked List
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
    def insert_element_at_beginning(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    # Adding element at the end
    """
    Two cases on adding element at the end
    1) If linked list is empty then the new note will be the first node, so need to handle
    2) If linked list is not empty then need to traverse to the end and write code accordingly    
    """

    def insert_element_at_end(self, data):
        new_node = Node(data)
        n = self.head
        if n is None:
            self.head = new_node  # if linked list is empty then new node will be first node of the list
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    """
    Adding element in between the elements so basically,we can
    1) add after a given element
    2) add before a given element
    """

    # Adding element after a given element
    '''
    Cases:
    1) Find x that is given node after which we need to add element
    2) given element is not in the list
    3) happy path-- add element after x
    '''

    def insert_after_given_element(self, data, x):

        n = self.head
        while n.ref is not None:
            if n.data == x:
                break
            n = n.ref
        if n.ref is None:
            print(f"Node {x} is not present in the Linked List!")
            return
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Adding element before a given element
    '''
    Cases:
    1) Linked list is empty
    2) Find x that is given node before which we need to add element, for this we need to find the previous
       node of the given node x and then its like adding element after a given node
    3) If data is being added before the first node then new node will be first node so need to 
        write code of add_at_beginning
    4) given element is not in the list
    5) happy path-- add element before x
    '''

    def insert_before_given_element(self, data, x):
        n = self.head
        if n is None:
            print("Linked List is empty!")
            return
        if n.data == x:
            # LL.add_element_at_beginning()
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        else:
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print(f"Node {x} is not present in the Linked List!")
            else:
                # LL.add_after_given_element()
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node
                
    # Inserting element on an empty Linked List
    def insert_in_empty_LL(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked List is not empty!")


LL = LinkedList()
LL.insert_in_empty_LL(50)
LL.insert_element_at_beginning(20)
LL.insert_element_at_end(100)
LL.insert_before_given_element(80,100)
LL.insert_after_given_element(50,80)
LL.printLinkedList()
