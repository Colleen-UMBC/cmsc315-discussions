"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.stack = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Push adds new item on the top of stack. Pop removes and returns the item at the top of the stack
        # This means that the last item added to the stack is also the first item removed, ie. LIFO
        self.stack.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # If a stack is empty, there is nothing to remove/pop and that could lead to an error so I chose to return ValueError
        # According to python.org, ValueError is used when "an argument has the right type but an inappropriate value"
        if self.is_empty():
            raise ValueError("Stack cannot be empty.")
        return self.stack.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        if self.is_empty():
            return "Stack is empty."
        # Peek returns the stack's top item without removing it from the stack
        # Since peek is unavailable in this library, I chose to return the last element of the list
        return self.stack[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.stack) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.queue = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Enqueue inserts items at the end of the queue. Dequeue removes items at the front of the queue
        # This means that the first item removed from the queue was the first item added, ie. FIFO
        self.queue.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # If a queue is empty, there is nothing to remove/dequeue and that could lead to an error so I chose to return ValueError
        # According to python.org, ValueError is used when "an argument has the right type but an inappropriate value"
        if self.is_empty():
            raise ValueError("Queue cannot be empty.")
        return self.queue.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # This method acts the same as peek(). It returns the item at the front of the queue without removing it
        if self.is_empty():
            return "Queue is empty."
        return self.queue[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.queue) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

# 1. Create a Stack object.
print("\n~~~~~ Creating a stack object called stackDemo ~~~~~")
stackDemo = Stack()

# 2. Add at least 4 values to the stack.
print("~~~~~ Adding Countries to Stack ~~~~~")
for countries in ["Belgium", "Chile", "Guyana", "Singapore"]:
    stackDemo.push(countries)
    print("...Added", countries)

# 4. Demonstrate LIFO behavior.
print("\n~~~~~ Demonstrating LIFO ~~~~~")
print(f"...List of Countries: (bottom) {', '.join(stackDemo.stack)} (top)")
print(f"...Removing country via. pop()")
stackDemo.pop()
print(f"...List of Countries: (bottom) {', '.join(stackDemo.stack)} (top)")


print("\n~~~~~ Edge Cases ~~~~~")

# 5. Show what happens when pop() is used on an empty stack.
print("\n~~ Show what happens when pop() is used on an empty stack")
print("...Creating an empty stack object called emptyStack")
emptyStack = Stack()
print("...pop() on an empty stack is coded to raise an error. So I'll print the error to keep the program running to the end")
if emptyStack.is_empty():
    print("...Resulting ERROR: ValueError: Stack cannot be empty")

# 6. Show what happens when peek() is used on an empty stack.
print("\n~~ Show what happens when peek() is used on an empty stack.")
print("...Calling peek() on an empty stack")
print(f"...Resulting Warning:", emptyStack.peek())

# 7. Create a stack with only one item, remove it,
#    and verify the stack is empty afterward.
print("\n~~ Create a stack with only one item, remove it")
print("...Creating a stack object called oneItemStack")
oneItemStack = Stack()
print("...Adding a continent to oneItemStack")
oneItemStack.push("Africa")
print(f"...List of continents: (bottom) {', '.join(oneItemStack.stack)} (top)")
print("...Removing continent via. pop()")
oneItemStack.pop()
print("...and verify the stack is empty afterward")
print(f"...List of continents: (bottom) {', '.join(oneItemStack.stack)} (top)")



# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

# 1. Create a Queue object.
print("\n~~~~~ Creating a queue object called queueDemo ~~~~~")
queueDemo = Queue()

# 2. Add at least 4 values to the queue.
print("~~~~~ Adding Flowers to Stack ~~~~~")
for flowers in ["Rose", "Sunflower", "Peony", "Lavender"]:
    queueDemo.enqueue(flowers)
    print("...Added", flowers)

# 4. Demonstrate FIFO behavior.
print("\n~~~~~ Demonstrating FIFO ~~~~~")
print(f"...List of Flowers: (top) {', '.join(queueDemo.queue)} (bottom)")
print(f"...Removing flower via. dequeue()")
queueDemo.dequeue()
print(f"...List of Flowers: (top) {', '.join(queueDemo.queue)} (bottom)")


print("\n~~~~~ Edge Cases ~~~~~")

# 5. Show what happens when dequeue() is used on an empty queue.
print("\n~~ Show what happens when dequeue() is used on an empty queue")
print("...Creating an empty queue object called emptyQueue")
emptyQueue = Queue()
print("...Dequeue() on an empty queue is coded to raise an error. So I'll print the error to keep the program running to the end")
if emptyQueue.is_empty():
    print("...Resulting ERROR: ValueError: Queue cannot be empty")

# 6. Show what happens when front() is used on an empty queue.
print("\n~~ Show what happens when front() is used on an empty queue.")
print("...Calling front() on an empty queue")
print(f"...Resulting Warning:", emptyQueue.front())

# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.
print("\n~~ Create a queue with only one item, remove it")
print("...Creating a queue object called oneItemQueue")
oneItemQueue = Queue()
print("...Adding a Flower to oneItemQueue")
oneItemQueue.enqueue("Hydrangea")
print(f"...List of Flowers: (top) {', '.join(queueDemo.queue)} (bottom)")
print(f"...Removing country via. dequeue()")
oneItemQueue.dequeue()
print("...and verify the queue is empty afterward")
print(f"...List of Flowers: (top) {', '.join(oneItemQueue.queue)} (bottom)")


print("\n=== Create a real-world scenario ===")
print("~~~~~ Scenario: Program tasked with keeping track of the orders in a coffee shop ~~~~~")
print("...Creating a queue object called coffeeLine")
coffeeLine = Queue()
print("...Adding orders to queue")
for orders in ["Alex: Matcha Latte", "Lexi: Chai", "Taylor: Americano"]:
    coffeeLine.enqueue(orders)
    print(f"...Adding order:", orders)
print(f"...List of orders: (top) {', '.join(coffeeLine.queue)} (bottom)")
print("...Serving next order")
coffeeLine.dequeue()
print(f"...List of orders: (top) {', '.join(coffeeLine.queue)} (bottom)")
print(f"...Next Up:", coffeeLine.front())

if __name__ == "__main__":
    main()
