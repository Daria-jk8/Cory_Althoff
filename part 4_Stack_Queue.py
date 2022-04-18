# --> LIFO(last in first out)
# --> Stack uses 5 methods: is_empty, push, pop, peek, size

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):             # − check if stack is empty. Returns True if the stack is empty, else False.
        return self.items == []

    def push(self, item):           # − Pushing (storing) an element on the stack.
        self.items.append(item)  

    def pop(self):                  # − Removing (accessing) an element from the stack.
        return self.items.pop()     

    def peek(self):                 # − get the top data element of the stack, without removing it.
        last = len(self.items) - 1
        return self.items[last]

    def size(self):                 # - returns an integer representing the number of elements on the stack.
        return len(self.items)  

stack = Stack()
for i in  "Good day!":
    stack.push(i)

reverse = ""

for a in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)                  # !yad dooG


# --> FIFO(first in first out)
# --> Queue uses 4 methods: is_empty, enqueue, dequeue, size

class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)    

a_queue = Queue()
print(a_queue.is_empty())    # True

for i in range(5):
    a_queue.enqueue(i)

print(a_queue.size())        # 5

for i in range(5):
   print(a_queue.dequeue())  

print()

print(a_queue.size())         



