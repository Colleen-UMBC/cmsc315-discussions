"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None


    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Nodes that are smaller than the current node becomes the current node's left child
        # Nodes that are larger than the current node becomes the current node's right child

        # - Use the recursive helper method.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # - Create a new node when a position is found.
        if node is None:
            return Node(value)
        # If duplicate value, return node
        if value == node.value:
            return node
        else:
            # - Insert smaller values into the left subtree.
            if value < node.value:
                node.left = self._insert_recursive(node.left, value)
            # - Insert larger values into the right subtree.
            else:
                node.right = self._insert_recursive(node.right, value)
        return node


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # The worst case for searching in BST is O((log2 N) + 1)
        # The worst case for searching linear is O(N)
        # That means that BST has a faster speed since log2 N is significantly smaller than N
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # - Return False if not found.
        if node is None:
            return False
        # - Return True if found.
        if value == node.value:
            return True
        else:
            if value < node.value:
                return self._search_recursive(node.left, value)
            else:
                return self._search_recursive(node.right, value)


    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        valueList = []
        self._inorder_recursive(self.root, valueList)
        return valueList

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # left child value < parent value < right child value
        # So by traversing in this order, the values are appended in ascending order
        if node is None:
            return
        # - Visit the left subtree
        self._inorder_recursive(node.left, values)
        # - Visit the current node.
        values.append(node.value)
        # - Visit the right subtree.
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # 1. Create a BST object.
    print("...Creating a BST object")
    sampleBST = BST()

    # 2. Insert at least 7 values.
    # 3. Include values that go into both left and right subtrees.
    numbersList = [10, 30, 40, 50, 60, 70, 90]
    for number in numbersList:
        sampleBST.insert(number)
        print("...Inserted", number, "into the BST")

    # 4. Display the values inserted = Done in next section

    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.
    # left child value < parent value < right child value
    # That means that when searching at each step you are able to cancel out an entire subtree

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # 1. Perform an in-order traversal.
    print("...Performing in-order traversal")
    traversalList = sampleBST.inorder()

    # 2. Display the traversal results.
    print(f"...BST: {traversalList}")

    # 3. Use comments to explain why the traversal produces sorted output in a BST.
    # left child value < parent value < right child value
    # So by traversing in this order, the values are appended in ascending order

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # 1. Search for at least two values that exist.
    # Calls search function for each value which then returns a boolean
    print("...Searching for values that exist in the BST")
    print("...Searching for 30", sampleBST.search(30))
    print("...Searching for 50", sampleBST.search(50))

    # 2. Search for at least two values that do not exist.
    # Calls search function for each value which then returns a boolean
    print("...Searching for values that do not exist in the BST")
    print("...Searching for 80", sampleBST.search(80))
    print("...Searching for 100", sampleBST.search(100))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # - Traverse an empty tree
    print("...Creating an empty BST")
    edgeCaseBST = BST()
    print("...Performing in-order traversal")
    edgeCaseBSTList = edgeCaseBST.inorder()
    print(f"...BST: {edgeCaseBSTList}")

    # - Search an empty tree
    print("...Searching for 15", edgeCaseBST.search(15))

    # - Create a tree with only one node
    print("...Inserted 25 into the BST")
    edgeCaseBST.insert(25)
    edgeCaseBSTList = edgeCaseBST.inorder()
    print(f"...BST: {edgeCaseBSTList}")

    # - Insert duplicate values
    print("...Attempted to insert 25 into the BST again")
    edgeCaseBST.insert(25)
    edgeCaseBSTList = edgeCaseBST.inorder()
    print(f"...BST: {edgeCaseBSTList}")


    # ===============================
    # REAL-WORLD EXAMPLE
    # ===============================
    print("\n=== REAL-WORLD BST EXAMPLE ===")
    print("Scenario: A database stores student IDs")
    # Based on "Database Indexing (BST Concept)" in the Learning Resources tab

    print("...Creating BST")
    realWorldBST = BST()
    studentIDs = [4390, 9540, 8937, 9386, 3847, 3957, 4679]
    for ID in studentIDs:
        realWorldBST.insert(ID)
        print("...Inserted student ID:", ID, "into the BST")
    IDTraversalList = realWorldBST.inorder()
    print(f"...BST: {IDTraversalList}")

    print("...Confirming student IDs that exist in the BST")
    print("...Searching for 8937", realWorldBST.search(8937))
    print("...Confirming student IDs that do not exist in the BST")
    print("...Searching for 1001", realWorldBST.search(1001))


if __name__ == "__main__":
    main()