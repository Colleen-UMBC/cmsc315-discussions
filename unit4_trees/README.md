# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
I built multiple BSTs using the BST constructor
2. Insert multiple values.
I inserted multiple values using the insert and _insert_recursive methods
3. Demonstrate in-order traversal.
I performed in-order traversals using the inorder and _inorder_recursive methods and returning a list. 
4. Test searching.
I searched for given values using the search and _search_recursive methods and returned a boolean
5. Demonstrate edge cases.
I demonstrated what happened when I traversed and searched an empty tree, inserted only one node, and then inserted a duplicate value
6. Create a real-world BST example.
I implemented a real-world scenario where a database stores student IDs

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment
This assignment allowed me to build upon my skills in Data Structures Implementation, Algorithmic Thinking, Programming Fundamentals, Debugging and Testing, as well as Technical Evaluation and Tradeoff Analysis.
2. What challenges did you encounter, and how did you overcome them?
Just like when completing the previous discussion projects, the only challenge I faced when completing this project was translating the zybooks lesson from java to python. 
My solution was to just code in a mixture of the two languages, immediately go back over the code and rewrite it to work in python, and then run the code to see if I missed anything. 
Eventually, my goal is to just frequently code in python and java in my free time so I won’t experience that hiccup again.
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.
BSTs have a parent node and at most 2 child nodes who may be parents as well. The left  child value is less than the parent value and the right child value is greater than the parent value. 
After comparing your target value to a parent value, you then continue down the left or right subtree. This allows for faster traversal as you’re able to filter out an entire subtree each step.