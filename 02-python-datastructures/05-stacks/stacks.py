"""
STACKS (LIFO - Last in, First Out)
What is Stack?
- a linear data structure where the last element added (pushed) is the first to be removed (popped)
- Example : Stack of books - you can add/remove from the top.
Operations:
1) Push -> Add an element to the top.
2) Pop -> Remove the top element
3) Peek/Top -> See the top element without removing.
4) isEmpty -> Check if stack is empty.
"""

## Implementation Using Python List

stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)
print("Stack:", stack)

# Pop
print("Popped:", stack.pop())
print("Stack after pop:", stack)

# Peek/Top
print("Top element:", stack[-1])

# Checking Empty
print("Is Empty?", len(stack) == 0)


## Implementation Using collection.deque
