# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
I coded and implemented insert_at(). I then called the method to test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
I coded and implemented delete_at(). I then called the method to test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
I coded and implemented search_value(). I then called the method to test for existing and missing values. 
4. Demonstrate edge cases.
I tested delete using an invalid index, search for a missing value, insert into an empty list, and delete from an empty list.
5. Create a real-world scenario.
My real-world scenario was updating a contact list. I added, searched for, and deleted contacts. 

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
By completing this assignment, I was able to build on my skills in Programming Languages, Algorithms and Data Structures.
This allowed me to further build on my skills in Data Structures Implementation, Algorithmic Thinking, Technical Evaluation and Tradeoff Analysis, Programming Fundamentals, Debugging and Testing.
2. What challenges did you encounter, and how did you overcome them?
This was the first time I completed the discussion project before completing the lab. 
So I’m a bit worried that I missed a few small things that would have been made extremely obvious in the lab. 
Like calling an error instead of a message, for example. I went over the project instructions, my code, my comments, and my notes for hours until I felt confident I didn’t miss anything.
3. How do list operations impact performance in real-world applications?
When altering a list, insertion/deletion at the front and middle are O(n) and insertion/deletion at the end is O(1). 
When working with extremely large data – eg social media friends list – this means that list operations significantly hinder speed. 