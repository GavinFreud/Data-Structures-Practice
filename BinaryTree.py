class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def remove(self, data):
        node, parent = self.find_node(data)
        if node is not None:
            children_pop = node.children_pop()
        if children_pop == 0
            if parent:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            else:
                self.data = None
        elif children_pop == 1:
            if node.left:
                replacement = node.left
            else:
                replacement = node.right
            if parent:
                if parent.left == node:
                    parent.left = replacement
                else:
                    parent.right = replacement
                del node
            else:
                self.left = replacement.left
                self.right = replacement.right
                self.data = replacement.data
        else:


    def children_pop(self):
        pop=0
        if self.left:
            pop += 1
        if self.right:
            pop += 1
        return pop
        

    def find_node(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.find_node(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.find_node(data, self)
        else:
            return self, parent
                






