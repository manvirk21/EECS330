class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None


class Deque:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0


    def empty(self):  # Check whether the deque is empty.
        return self.size == 0

    
    def get_size(self) -> int:  # Return total number of elements in deque.
        return self.size

    
    def push_front(self, data):  # Push an element to the front of the deque.
        new_node = Node(data)
        if self.empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1


    def push(self, data):  # Push an element at the back of the deque.
        new_node = Node(data)
        if self.empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.prev = self.back
            self.back.next = new_node
            self.back = new_node
        self.size += 1


    def pop_front(self) -> int:  # Pop an element from the front of the deque.
        if self.empty():
            raise IndexError("Deque is empty")
        data = self.front.item
        if self.size == 1:
            self.front = None
            self.back = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.size -= 1
        return data


    def pop(self) -> int:  # Pop an element from the back of the deque.
        if self.empty():
            raise IndexError("Deque is empty")
        data = self.back.item
        if self.size == 1:
            self.front = None
            self.back = None
        else:
            self.back = self.back.prev
            self.back.next = None
        self.size -= 1
        return data


    def front(self) -> int:  # Access the first element of deque.
        if self.empty():
            raise IndexError("Deque is empty")
        return self.front.item


    def back(self) -> int:  # Access the last element of deque.
        if self.empty():
            raise IndexError("Deque is empty")
        return self.back.item

def reverse_deque(deque):
    # Initialize an object for your new deque.
    reversed_deque = Deque()
    # Iterate through the input deque and add items to the reversed_deque in the reverse order.
    while not deque.empty():
        reversed_deque.push_front(deque.pop_front())
    return reversed_deque


def isPalindrome(s: str) -> bool:  # Checks whether given string is palindrome or not.
    # Initialize Deque using Deque class.
    deque = Deque()
    for char in s:
        deque.push(char)

    if deque.empty():
        print("Empty deque")
        
    while not deque.empty():
        front_char = deque.pop_front()
        if not deque.empty():
            back_char = deque.pop()
            if front_char != back_char:
                return False
    return True     


# Test cases
test1 = "racecar"
test2 = "hello"
print(isPalindrome(test1))  # True
print(isPalindrome(test2))  # False
