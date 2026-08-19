from collections import deque

#creating
d = deque([1,2,3,4,5])

#adding
d.append(6)
print(d)
d.appendleft(0)
print(d)
d.extend([6,7])
print(d)
d.extendleft([-1,-2])
print(d)

d.pop()
print(d)
d.popleft()
print(d)
d.remove(-1)

#rotate
d.rotate(2)
print(d)
d.rotate(-1)
print(d)


from collections import Counter

#creating
counter = Counter([1,2,3,4,5,6,7,7])
print(counter)
counter = Counter('hello world')
print(counter)
print(counter.most_common(2))

from queue import Queue, LifoQueue, PriorityQueue

# Queue (FIFO)
q = Queue()
q.put(1)
q.put(2)
print(q.get())                  # 1

# LifoQueue (LIFO - Stack)
lq = LifoQueue()
lq.put(1)
lq.put(2)
print(lq.get())                 # 2

# PriorityQueue (Minimum heap)
pq = PriorityQueue()
pq.put((2, 'medium priority'))
pq.put((1, 'high priority'))
pq.put((3, 'low priority'))
print(pq.get())                 # (1, 'high priority')