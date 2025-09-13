# Topic Queue (FIFO) using collections.deque

from collections import deque # Import deque for efficient queue operations

#1 Create an empty queue
q = deque ()

#2 Enqueue (append to the right/back)
q.append("A")
q.append("B")
q.append("C")
print("Queue after enqueues:", q)

#3 Dequeue (popleft from the left/front)
front = q.popleft()
print("Served:", front)
print("Queue Now:", q)

#4 Peek front/back without removing
print("Front element", q[0])
print("Back element", q[-1])

#5 Tiny simulation: process the tasks in an arrival order
tasks = deque(["t1", "t2", "t3"])
while tasks:
    t = tasks.popleft()
    print("Processing", t)