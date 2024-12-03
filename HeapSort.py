# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:28:41 2024

@author: Spencer Miller
"""

class HeapSort:
    # Constructor to initialize the heap
    def __init__(self, heap: list) -> None:
        self.heap = heap

    # Function to create heap subtree rooted at index i
    def create_heap(self, n: int, i: int) -> None:
        # Initialize maximum as root
        maximum = i
        
        # left = 2*i + 1
        l = 2 * i + 1
        
        # right = 2*i + 2
        r = 2 * i + 2

        # Check if left child of root exists and is greater than root
        if l < n and self.heap[i] < self.heap[l]:
            maximum = l

        # Check if right child of root exists and is greater than root
        if r < n and self.heap[maximum] < self.heap[r]:
            maximum = r

        # Change root, if needed
        if maximum != i:
            # Swap values
            self.heap[i], self.heap[maximum] = self.heap[maximum], self.heap[i]
            
            # Create max heap
            self.create_heap(n, maximum)

    # Main function to do heap sort
    def heapSort(self) -> None:
        # Get the length of the heap
        n = len(self.heap)

        # Build a maxheap
        for i in range(n, -1, -1):
            self.create_heap(n, i)

        # Extract elements one by one
        for i in range(n-1, 0, -1):
            # Swap values
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            
            # Build max heap with root element
            self.create_heap(i, 0)

    # Function to print the heap array
    def printHeap(self) -> None:
        print("Heap array: ")
        print(self.heap)

    # Function to print the sorted array
    def printSorted(self) -> None:
        print("The Sorted array is: ")
        print(self.heap)

# Driver code
# Define the heap
heap = [58, 306, 770, 12, 998, 487,
        361, 558, 874, 608, 618, 168,
        588, 187, 623, 653, 634, 973,
        8, 642, 80, 402, 352]

# Create an instance of the HeapSort class
heapSorter = HeapSort(heap)

# Print the heap array
heapSorter.printHeap()

# Call the heapSort method to sort the heap
heapSorter.heapSort()

# Print the sorted array
heapSorter.printSorted()