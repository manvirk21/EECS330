from DLL import Deque


def wordToDeque(input):
    deque = Deque()
    for char in input:
        deque.push(char)
    return deque


def testWordToDeque(test_string, test_deque):
    temp = test_deque
    for i in range(len(test_string)):
        if temp.front is None or test_string[i] != temp.front.item:
            return False
        else:
            temp.front = temp.front.next
    if temp.front is not None:
        return False
    return True

# Testing logic
test1_string = "hello"
test1_deque = wordToDeque(test1_string)
print(testWordToDeque(test1_string, test1_deque))  # Should return True


def OffByOne(char1, char2):
    # Check if the absolute difference between the ASCII values of char1 and char2 is 1.
    return abs(ord(char1) - ord(char2)) == 1

# Testing Logic
char1 = 'b'
char2 = 'a'
print(OffByOne(char1, char2))  # Should print True


def OffByN(char1, char2, N):
    # Check if the absolute difference between the ASCII values of char1 and char2 is equal to N.
    return abs(ord(char1) - ord(char2)) == N

# Testing Logic
char1 = 'b'
char2 = 'e'
N = 3
print(OffByN(char1, char2, N))  # Should print True
