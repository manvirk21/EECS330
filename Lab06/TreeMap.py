class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        """Inserts a new key-value pair into the TreeMap."""
        self.root = self._put_recursive(self.root, key, value)

    def _put_recursive(self, node, key, value):
        if node is None:
            return TreeNode(key, value)

        if key < node.key:
            node.left = self._put_recursive(node.left, key, value)
        elif key > node.key:
            node.right = self._put_recursive(node.right, key, value)
        else:
            # Update the value for an existing key
            node.value = value
        return node


    def get(self, key):
        """Retrieve the value associated with the given key."""
        node = self.search(key)
        if node is not None:
          return node.value
        else:
          return None        

    def search(self, key) -> TreeNode:
        """Searches for the given key in the BST and returns the corresponding node.

        If multiple nodes have the same value, the first node found using preorder
        traversal is returned."""
        node = self.root
        
        while node is not None:
            if key == node.key:
                return node
            elif key < node.key:
                node = node.left
            else:
                node = node.right
                
        return None



# Create a TreeMap
tree_map = TreeMap()

# Test putting and getting key-value pairs.
tree_map.put(3, "A")
tree_map.put(1, "B")
tree_map.put(2, "C")
tree_map.put(4, "D")

assert tree_map.get(2) == "C"
assert tree_map.get(1) == "B"
assert tree_map.get(4) == "D"
# Non-existent key should return None.
assert tree_map.get(5) is None
