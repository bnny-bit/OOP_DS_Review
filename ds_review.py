# 1. Array/List: Simple list operations
print("--- 1. List (Array) Demonstration ---")
my_list = [10, 20, 30, 40]
print(f"Initial List: {my_list}")
my_list.append(50) # Add
print(f"After append: {my_list}")
my_list.insert(0, 5) # Insert at index
print(f"Element at index 2: {my_list[2]}") # Access
my_list.pop(1) # Remove by index
print(f"After pop(1): {my_list}")


# 2. Stack (LIFO: Last-In, First-Out) using a Python list
print("\n--- 2. Stack Demonstration ---")
stack = []
stack.append('A') # Push
stack.append('B') # Push
print(f"Stack after pushes: {stack}")
print(f"Peek (top element): {stack[-1]}")
print(f"Pop (removed): {stack.pop()}") # Pop
print(f"Stack after pop: {stack}")


# 3. Queue (FIFO: First-In, First-Out) using Python's deque
from collections import deque
print("\n--- 3. Queue Demonstration ---")
queue = deque()
queue.append('Task 1') # Enqueue (add to the right)
queue.append('Task 2') # Enqueue
print(f"Queue after enqueues: {queue}")
print(f"Dequeue (removed): {queue.popleft()}") # Dequeue (remove from the left)
print(f"Queue after dequeue: {queue}")


# 4. Simple Binary Search Tree (Node structure only)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

print("\n--- 4. Binary Search Tree (Node) Demonstration ---")
root = Node(50)
root.left = Node(30)
root.right = Node(70)
print(f"Root Node: {root.data}")
print(f"Left Child: {root.left.data}")
