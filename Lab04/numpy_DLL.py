import numpy as np


class Deque:
    def __init__(self, capacity=10):
        self.capacity = capacity
        # Initialize front and rear pointers.
        self.front = -1
        self.back = -1
        # Initialize size of the deque.
        self.size = 0
        # Use a zero intialized NumPy array to store elements.
        self.array = np.zeros(self.capacity, dtype=object)


    def empty(self):
        """Check whether the deque is empty."""
        return self.size == 0


    def get_size(self):
        """Return total number of elements in deque."""
        return self.size


    def push_front(self, data):
        """Push an element to the front of the deque."""
        if self.size == self.capacity:
            # If the array is full, resize
            self._resize()
        if self.empty():
            self.front = 0
            self.back = 0
        else:
            self.front = (self.front - 1) % self.capacity
        self.array[self.front] = data
        self.size += 1

        
    def push(self, data):
        """Push an element at the back of the deque."""
        if self.size == self.capacity:
            # If the array is full, resize.
            self._resize()
        if self.empty():
            self.front = 0
            self.back = 0
        else:
            self.back = (self.back + 1) % self.capacity
        self.array[self.back] = data
        self.size += 1


    def pop_front(self):
        """Pop an element from the front of the deque."""
        if self.empty():
            raise IndexError("Deque is empty")
        data = self.array[self.front]
        if self.size == 1:
            self.front = -1
            self.back = -1
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return data


    def pop(self):
        """Pop an element from the back of the deque."""
        if self.empty():
            raise IndexError("Deque is empty")
        data = self.array[self.back]
        if self.size == 1:
            self.front = -1
            self.back = -1
        else:
            self.back = (self.back - 1) % self.capacity
        self.size -= 1
        return data


    def resize(self):
        """Resize the deque to double its capacity."""
        new_capacity = self.capacity * 2
        new_array = np.zeros(new_capacity, dtype=object)
        if self.front <= self.back:
            new_array[:self.size] = self.array[self.front:self.front + self.size]
        else:
            new_array[:self.capacity - self.front] = self.array[self.front:]
            new_array[self.capacity - self.front:] = self.array[:self.back + 1]
        
        self.front = 0
        self.back = self.size - 1
        self.capacity = new_capacity
        self.array = new_array


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
    # Create a second deque to store the reversed characters.
    reversed_deque = reverse_deque(deque)
    
    # Compare characters from the original and reversed deques.
    while not deque.empty():
        if deque.pop() != reversed_deque.pop():
            return False  
    return True

