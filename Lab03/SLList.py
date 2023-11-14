class SLList:     # This class represents a singly linked list
    class IntNode: # This class represents a node in the linked list.
        def __init__(self, item, next_node): # Initialize the node's item and next node references
            self.item = item  # int
            self.next = next_node  # IntNode

    def __init__(self):
        self.first = None  # initialize an empty list

    def addFirst(self, item):
        # Create a new node with the given item and make it the new first node
        self.first = self.IntNode(item, self.first)

    def insert(self, item, position):
        # Create a new node with the given item
        new_node = self.IntNode(item, None)

        # Handle the case where the list is empty or position is 0
        if position == 0 or self.first is None:
            new_node.next = self.first
            self.first = new_node
            return

        # Traverse the list to find the node before the specified position
        current = self.first
        index = 0
        while current.next is not None and index < position - 1:
            current = current.next
            index += 1

        # Update the next pointers to insert the new node
        new_node.next = current.next
        current.next = new_node

    def reverse(self):
        prev = None  # Initialize a pointer to keep track of the previous node
        current = self.first  # Start from the first node

        while current is not None:
            next_node = current.next  # Keep a reference to the next node
            current.next = prev  # Reverse the next pointer of the current node
            # Move to the next nodes
            prev = current
            current = next_node
        # Update the first reference to point to the new first node (which was originally the last node)
        self.first = prev

    def reverse_recursive(self):
        if self.first is None or self.first.next is None:
            return self.first
        def reverse_helper(current, prev):
            if current is None:
                return prev
            next_node = current.next
            current.next = prev
            return reverse_helper(next_node, current)
        # Start the recursion with the first node
        self.first = reverse_helper(self.first, None)

    
    def replicate(self):
        new_list = SLList()  # Create a new empty linked list
        current = self.first  # Traverse the original list, adding copies of each item to the new list.
        while current is not None:
            item = current.item
            # Replace the item at position with item copies of itself
            # For example, if item = 3, add 3 to the new list three times
            for i in range(item):
                new_list.addFirst(item)
            current = current.next

        return new_list  # Return the new replicated linked list

    def equals(self, anotherList):
        # Initialize two pointers to traverse the two lists.
        current_self = self.first
        current_another = anotherList.first
        
        # This while loop compares the two lists.
        while current_self is not None and current_another is not None:
            if current_self.item != current_another.item:
                return False  # Lists are not equal
            current_self = current_self.next
            current_another = current_another.next

        # If both lists reached the end together, they are equal
        return current_self is None and current_another is None

if __name__ == '__main__':
    # Test 1: Insert method
    L1 = SLList()
    L1.addFirst(15)
    L1.addFirst(10)
    L1.addFirst(5)
    L1.insert(8, 1) # insert 8 at index 1
    L1_expect = SLList()
    L1_expect.addFirst(15)
    L1_expect.addFirst(10)
    L1_expect.addFirst(8)
    L1_expect.addFirst(5)	

    if L1.equals(L1_expect):
        print("Insert method test passed")
    else:
        print("Insert method test failed")
        current = L1.first
        print("Actual list:")
        while current is not None:
            print(current.item, end=" → ")
            current = current.next
        print("\nExpected list:")
        current_expect = L1_expect.first
        while current_expect is not None:
            print(current_expect.item, end=" → ")
            current_expect = current_expect.next
    
    # Test 2: Reverse method
    L2 = SLList()
    L2.addFirst(15)
    L2.addFirst(10)
    L2.addFirst(5)
    L2.reverse()

    L2_expect = SLList()
    L2_expect.addFirst(5)
    L2_expect.addFirst(10)
    L2_expect.addFirst(15)	

    if L2.equals(L2_expect):
        print("Reverse method test passed")
    else:
        print("\nReverse method test failed")
        current = L2.first
        print("Actual list:")
        while current is not None:
            print(current.item, end=" → ")
            current = current.next
        print("\nExpected list:")
        current_expect = L2_expect.first
        while current_expect is not None:
            print(current_expect.item, end=" → ")
            current_expect = current_expect.next
    
    # Test 3: Replicate method
    L3 = SLList()
    L3.addFirst(3)
    L3.addFirst(2)
    L3.addFirst(1)
    replicated_list = L3.replicate()

    L3_expect = SLList()
    L3_expect.addFirst(1)
    L3_expect.addFirst(2)
    L3_expect.addFirst(2)
    L3_expect.addFirst(3)
    L3_expect.addFirst(3)
    L3_expect.addFirst(3)	

    if replicated_list.equals(L3_expect):
        print("Replicate method test passed")
    else:
        print("\nReplicate method test failed")
        current = replicated_list.first
        print("Actual list:")
        while current is not None:
            print(current.item, end=" → ")
            current = current.next
        print("\nExpected list:")
        current_expect = L3_expect.first
        while current_expect is not None:
            print(current_expect.item, end=" → ")
            current_expect = current_expect.next
