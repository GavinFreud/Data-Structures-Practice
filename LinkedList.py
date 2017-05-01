class Linked_List(object):
    size = 0  # class variable to update within the insert and remove methods

    def __init__(self, head=None):  # initializes a new Linked List, and sets the head to a Node, if provided
        self.head = head

    def insert(self, data):  # simply points the new node to head, as this is very efficient and fast. O(1) efficiency.
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node
        self.size += 1  # increments size

    def find(self, data):  # Iterates through the Linked List. O(n) efficiency.
        current = self.head
        found = False
        while current and found is False:  # loops through the data to find the requested node
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next_node()
        if current is None:  # raises a ValueError if the node is not found.
            raise ValueError("Not found in list")
        return current  # returns current if found in the previous loop

    def remove(self, data):  # Iterates through the LL, similar to the find method. O(n) efficiency.
        current = self.head
        previous = None
        found = False
        while current and found is False:  # iterates through the LL to find the requested node
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next_node()
        if current is None:  # raises a ValueError if the node is not found
            raise ValueError("That value is not in this list")
        if previous is None:  # sets head to the next node if the node requested is the head of the LL
            self.head = current.get_next_node()
        else:  # removes the node by setting the pointer of the previous node to the one following the removed node.
            previous.set_next_node(current.get_next_node())
        self.size -= 1  # decrements size

    def return_size(
            self):  # returns size. Thanks to the incrementation and decrementation of the size in the remove and insert methods, this has a O(1) efficiency.
        return self.size


class Node(object):  # node object that allows you to get the data, get the next node, and set the next node
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.nextNode = next_node

    def get_data(self):
        return self.data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_node):
        self.next_node = new_node
