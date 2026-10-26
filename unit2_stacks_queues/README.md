# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
I coded and implemented __init__(self), push(), pop(), peek(), and isEmpty() for the Stack class and created multiple Stack objects.
2. Implement queue operations.
I coded and implemented __init__self(), enqueue(), dequeue(), front(), and isEmprty() for the Queue class and created multiple Queue objects
3. Demonstrate LIFO behavior.
I demonstrated LIFO behavior by repeatedly calling push() and pop() on multiple stacks and printing the results.
4. Demonstrate FIFO behavior.
I demonstrated FIFO behavior by repeatedly calling enqueue() and dequeue() on multiple queues and printing the results.
5. Create and test edge cases.
I coded for edge cases within the appropriate methods for each class. For the cases that would raise an error, I printed the error message so that the program would continue to run.
6. Create a real-world scenario.
I created a real-world scenario where a program was tasked with keeping track of the orders in a coffee shop via a queue.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
This assignment allowed me to build my Data Structures Implementation, Algorithmic Thinking, Technical Evaluation and Tradeoff Analysis skills. 
I accomplished this by coding and implementing multiple stack and queue structures, analyzing their performance based on their Big-O notation, and then selecting the appropriate structures and methods for my real-life scenario. 

2. What challenges did you encounter, and how did you overcome them?
My biggest challenge for this assignment was trying to fix my git commit errors. I reached out to the professor for help and searched the internet for solutions for the specific error messages I keep getting. 
I’m still not the most comfortable committing to github. Another struggle I faced was translating the reading lessons from java to python since I have significantly more experience with Java and haven’t used python in around 5 years. 
I solved this issue by just typing it out as I would in java and then re-writing certain parts to work in python.

3. Explain the differences between stacks and queues as this relates to real-world applications.
When using stacks, the last item added to the stack is also the first item removed, ie. LIFO. A real world example of this would be the backspace button on your internet browser. 
The stack holds the websites you’ve visited and the back space buttons returns the last site you visited. When using queues, the first item removed from the queue was also the first item added, i.e. FIFO. 
A real world example would be the printing queue on a printer. The queue holds and completes the print jobs sent over to the printer in a FIFO fashion. 
