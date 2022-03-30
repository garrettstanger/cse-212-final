class BST:

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self): # Initializes empty list
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root
    def _insert(self, data, node): ## Looks where to place a node with data inside of it
        if data == node.data:
            return
        else:
            if data < node.data: # Data should be on left side
                if node.left is None: # If empty places data there
                    node.left = BST.Node(data)
                else:
                    self._insert(data, node.left)
            else: # Data should be on right side
                if node.right is None: # If empty places data there
                    node.right = BST.Node(data)
                else:
                    self._insert(data, node.right)
    def get_height(self):
        # This will get the height of the BST. An empty tree should be height 0,
        # a tree with just a root should have a height of 1. If there are more, 
        # you should call the _get_height recursively to find the height.
        if self.root is None:
            return 0
        else:
            return self.find_height(self.root)  # Start at the root

    def find_height(self, node):
        # Find the height of the BST, the height should be 1 plus the height of 
        # whichever of the right or left sub-tree is larger.
        h_l = 1
        h_r = 1
        if node.left is None and node.right is None:
            return 1
        if node.left is not None:
           h_l = 1 + self.find_height(node.left)

        if node.right is not None:
            h_r = 1 + self.find_height(node.right)
        return max(h_l, h_r)



### TESTS ###
tree = BST()
tree.insert(1)
tree.insert(5)
tree.insert(7)
tree.insert(4)
tree.insert(2)
tree.insert(3)
tree.insert(19)
print(tree.get_height()) # Should get a height of 5
tree.insert(20)
print(tree.get_height()) # Should get a height of 5
tree.insert(521)
print(tree.get_height()) # Should get a height of 6