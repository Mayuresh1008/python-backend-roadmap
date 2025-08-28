"""
QUEUES (FIFO - First In, First Out)
What is a Queue?
- A linear data structure where the first element added(enqueued) is the first to be removed(dequeued).
- Example : Line at a ticket counter -> the person who comes first, gets served first.

Operations:
1) Enqueue -> Add element at the rear.
2) Dequeue -> Remove element from the front.
3) Peek/Front -> See the first element without removing.
4) IsEmpty -> Check if queue is empty.
"""

## Implementation Using python list
queue = []

# Enqueue
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue:", queue)

# Dequeue
print("Dequeued:", queue.pop(0))
print("Queue after dequeue:", queue)

## Implementation using collection.deque
from collections import deque

queue = deque()

# Enqueue
queue.append("A")
queue.append("B")
queue.append("C")
print("Queue:", queue)

# Dequeue
print("Dequeue:", queue.popleft())
print("Queue after dequeue:", queue)

## Implementation Using queue.Queue
from queue import Queue

q = Queue()

# Enqueue
q.put(10)
q.put(20)
q.put(30)

# Dequeue
print("Dequeued:", q.get())
print("Dequeued:", q.get())

## Priority Queue

import heapq

pq = []

heapq.heappush(pq, (2, "Write Code"))
heapq.heappush(pq, (1, "Fix Bugs"))
heapq.heappush(pq, (3, "Push to Github"))

while pq:
    print(heapq.heappop(pq))
