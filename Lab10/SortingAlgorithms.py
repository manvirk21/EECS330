from random import randint, seed
import time


class Sorting:
    def __init__(self, size):
        self.arr = []  # Initialize an empty list
        self.size = size

    def add(self, element):
        if len(self.arr) < self.size:
            self.arr.append(element)
        else:
            print("Array is already full, cannot add more elements.")

    def selection_sort(self):
        """Implements selection sort"""
        for i in range(len(self.arr)):
            min_idx = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]

    def max_heapify(self, n, i):
        """Implements Heapify for array"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.arr[left] > self.arr[largest]:
            largest = left

        if right < n and self.arr[right] > self.arr[largest]:
            largest = right

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(n, largest)

    def heap_sort(self):
        """Implements Heap sort"""
        n = len(self.arr)
        for i in range(n // 2 - 1, -1, -1):
            self.max_heapify(n, i)
        for i in range(n - 1, 0, -1):
            self.arr[0], self.arr[i] = self.arr[i], self.arr[0]
            self.max_heapify(i, 0)


    def merge_sort(self):
        """Implements Merge sort"""
        if len(self.arr) > 1:
            mid = len(self.arr) // 2
            left_half = self.arr[:mid]
            right_half = self.arr[mid:]

            # Recursive calls to merge_sort
            left_sorter = Sorting(len(left_half))
            left_sorter.arr = left_half
            left_sorter.merge_sort()

            right_sorter = Sorting(len(right_half))
            right_sorter.arr = right_half
            right_sorter.merge_sort()

            i = j = k = 0

            # Merge process
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    self.arr[k] = left_half[i]
                    i += 1
                else:
                    self.arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                self.arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                self.arr[k] = right_half[j]
                j += 1
                k += 1


    def test_sorting_time(self, sorting_method):
        sizes = [10000, 20000, 30000, 40000, 50000]
        time_taken = []
        
        for size in sizes:
            # Generate random numbers for sorting
            self.arr = [randint(0, 100000) for _ in range(size)]

            start_time = time.time()
            
            # Call the specified sorting method
            if sorting_method == 'selection':
                self.selection_sort()
            elif sorting_method == 'heap':
                self.heap_sort()
            elif sorting_method == 'merge':
                self.merge_sort()

            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Time taken for {sorting_method.capitalize()} Sort with array size {size}: {elapsed_time:.6f} seconds")

            time_taken.append(elapsed_time)
        return time_taken


    
#Test Sorted array
def is_sorted(arr):
    if arr == sorted(arr):
        print("Passed!")
    else:
        print("Failed!")

# Test each sirting technique
def test_sort_algorithms(sorting_method, set_seed=None):
    if seed != None:
        seed(set_seed)
    sorting = Sorting(10)
    # Add 10 random elements
    for _ in range(10):
        sorting.add(randint(1, 100))
    # Apply the sorting algorithm
    if sorting_method == 'selection':
        sorting.selection_sort()
        print("Selection Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'heap':
        sorting.heap_sort()
        print("Heap Sort:", is_sorted(sorting.arr))
    elif sorting_method == 'merge':
        sorting.merge_sort()
        print("Merge Sort:", is_sorted(sorting.arr))
        
#Test run time
def run_time_tests():
    seeding = 45
    array_sizes = [10000,20000,30000,40000,50000]
    methods = ['selection', 'heap', 'merge']
    print("Array Size\t\tSelection Sort\t\tHeap Sort\t\tMerge Sort")
    for size in array_sizes: 
        times = []
        for m in methods:
            sorting = Sorting(size)
            seed(seeding)
            for _ in range(size):
                sorting.add(randint(1, 50000))
            interval = sorting.test_sorting_time(m)
            times.extend(interval)
        print(f"{size}\t\t{times[0]:.6f}\t\t{times[1]:.6f}\t\t{times[2]:.6f}")
        
#test case execution
seed_num = 43   
test_sort_algorithms('selection', seed_num)
test_sort_algorithms('heap', seed_num)
test_sort_algorithms('merge', seed_num)
run_time_tests()



'''
For the runtime complexity explanation, here's a brief overview:

Selection Sort: It has a time complexity of O(n^2) in all cases. As the input size grows, the time taken increases quadratically.
This explains the significant increase in time as the array size increases.

Heap Sort: It has a time complexity of O(n log n) in all cases. Although it has a better performance than Selection Sort, it
still grows logarithmically with respect to the input size, hence showing a notable increase in time but not as drastic as
the quadratic growth of Selection Sort.

Merge Sort: It also has a time complexity of O(n log n) in all cases. Similar to Heap Sort, it grows logarithmically with
input size. Therefore, it shows an increase in time, but the growth rate is relatively stable compared to Selection Sort due
to its more efficient divide-and-conquer approach.

'''

