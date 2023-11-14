class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
        '''Number of Nodes in the Tree'''
        self.size = 0


    def insert(self, value):
        """Insert a node with the given value into the BST."""
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            self.size += 1
        else:
            self._insert_recursive(self.root, new_node)


    def _insert_recursive(self, current_node, new_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
                self.size += 1
            else:
                self._insert_recursive(current_node.left, new_node)
        elif new_node.value >= current_node.value:
            if current_node.right is None:
                current_node.right = new_node
                self.size += 1
            else:
                self._insert_recursive(current_node.right, new_node)


    def search(self, value) -> TreeNode:
        """Search for a value in the BST and return the first corresponding TreeNode using preorder traversal."""
        return self._search_recursive(self.root, value)


    def _search_recursive(self, current_node, value):
        if current_node is None:
            return None

        if current_node.value == value:
            return current_node

        right_result = self._search_recursive(current_node.right, value)
        left_result = self._search_recursive(current_node.left, value)
        
        if left_result:
            return left_result
        if right_result:
            return right_result
        return None


    def level_order_traversal(self) -> list:
        """Perform level-order traversal of the binary search tree
        and return a list of values in the order that they were visited."""
        result = []
        queue = [self.root]

        while queue:
            current_node = queue.pop(0)  # Dequeue the first node in the queue
            if current_node is not None: 
                result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result



def main():
    # Initialize BST.
    bst = BinarySearchTree()

    # Test inserting nodes
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)

    # Test size method.
    assert bst.size == 7
    assert bst.search(1) is None

    # Test inserting additional nodes.
    bst.insert(1)
    bst.insert(6)

    assert bst.size == 9
    assert bst.search(1).value == 1

    # Finally, also test by inserting duplicate values.

    # Test level order traversal with duplicates.
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(7)
    bst.insert(9)
    bst.insert(5)
    bst.insert(7)
    bst.insert(1)
    bst.insert(6)
    bst.insert(1)
    bst.insert(6)

    # Test level order traversal.
    assert bst.level_order_traversal() == [5, 3, 8, 2, 4, 7, 9, 1, 5, 7, 1, 6, 6]

if __name__ == "__main__":
    main()
    
