"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Ensure that the index isn't a negative value or larger than the list + 1
    if 0 <= index < len(lst) + 1:
        # Inserts the value at the index using the python list method insert()
        # After insertion, the list is rearranged and the elements after that index point are shifted one index to the right
        # As such, an insertion at the very end is the fastest, at the very front is the slowest, and in the middle is average.
        # Specifically, insertion at the front and middle are O(n) and insertion at the end is O(1)
        lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Ensure that the index isn't a negative value or larger than the length of the list
    # Index validation ensuring that the index is in bounds we prevent errors and missing data
    if 0 <= index < len(lst):
        # Removes the value at the index using the python list method pop()
        # Safe deletion ensures that the data is deleted and cannot be accidentally or purposefully accessed again
        return lst.pop(index)
    # Returns None if the index is invalid
    return None


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Ensure that the index isn't a negative value or larger than the length of the list
    # Conducts a linear search that searches through array elements until finding the key (3.6.3 zyBooks)
    # Searching sequentially means the data doesn't need to be sorted and data types do not need to be assumed (CertBolt)
    for index in range(0, len(lst)):
        # If valid index and values match, return the index
        if lst[index] == value:
            return index
    # Returns -1 is the value is not found
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # 1. Create a list containing several values.
    print("...Creating list")
    testList = ["Apple", "Banana", "Cherry", "Date", "Eggplant", "Fig"]

    # 2. Display the original list.
    print(f"...List: {', '.join(testList)}")

    # 3. Test insertion at:
    #    - the beginning
    print("...Inserting Grape at the beginning of the list")
    insert_at(testList, 0, "Grape")
    print(f"...List: {', '.join(testList)}")

    #    - the middle
    print("...Inserting Honeysuckle at the middle of the list")
    insert_at(testList, 3, "Honeysuckle")
    print(f"...List: {', '.join(testList)}")

    #    - the end
    print("...Inserting Imbe at the end of the list")
    insert_at(testList, 8, "Imbe")
    print(f"...List: {', '.join(testList)}")



    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    print(f"...List: {', '.join(testList)}")

    # 1. Delete an item from:
    #    - the beginning
    print("...Deleting item from the beginning of the list")
    print(f"...Deleted {delete_at(testList, 0)}")
    print(f"...List: {', '.join(testList)}")

    #    - the middle
    print("...Deleting item from the middle of the list")
    print(f"...Deleted {delete_at(testList, 3)}")
    print(f"...List: {', '.join(testList)}")

    #    - the end
    print("...Deleting item from the end of the list")
    print(f"...Deleted {delete_at(testList, 6)}")
    print(f"...List: {', '.join(testList)}")



    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    print(f"...List: {', '.join(testList)}")

    # 1. Search for a value that exists.
    print("...Searching for Honeysuckle in list")
    print(f"...Found Honeysuckle in list at index {search_value(testList, "Honeysuckle")}")
    print(f"...List: {', '.join(testList)}")

    # 2. Search for a value that does not exist.
    print("...Searching for Rose in list")
    print(f"...Error {search_value(testList, "Rose")} : Rose does not exist in list")
    print(f"...List: {', '.join(testList)}")



# ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    print(f"...List: {', '.join(testList)}")

    # - Delete using an invalid index
    print("...Deleting item at index 10")
    print(f"...Deleted {delete_at(testList, 10)}")
    print(f"...List: {', '.join(testList)}")

    # - Search for a missing value
    print("...Searching for Lily in list")
    print(f"...Error {search_value(testList, "Lily")} : Lily does not exist in list")
    print(f"...List: {', '.join(testList)}")


    print("...Creating an empty list")
    emptyList = []
    print(f"...List: {', '.join(emptyList)}")


    # - Delete from an empty list
    print("...Deleting from an empty list")
    print(f"...Deleted {delete_at(emptyList, 0)}")
    print(f"...List: {', '.join(emptyList)}")

    # - Insert into an empty list
    print("...Inserting item into the empty list")
    insert_at(emptyList, 0, "Tulip")
    print(f"...List: {', '.join(emptyList)}")



# ===============================
# REAL WORLD SCENARIO
# ===============================
#
# 5. Create a real-world scenario.
#
    print("\n=== REAL WORLD SCENARIO ===")
    print("TODO: Create a real-world scenario.")

    print("Scenario: Contact List")
    print("...Creating new empty contact list")
    contactList = []
    print(f"...Contact List: {', '.join(testList)}")

    # Adding contacts
    print("...Adding Mom")
    insert_at(contactList, 0, "Mom")
    print(f"...Contact List: {', '.join(contactList)}")
    print("...Adding Dad")
    insert_at(contactList, 1, "Dad")
    print(f"...Contact List: {', '.join(contactList)}")
    print("...Adding Alex")
    insert_at(contactList, 2, "Alex")
    print(f"...Contact List: {', '.join(contactList)}")
    print("...Adding Sam")
    insert_at(contactList, 3, "Sam")
    print(f"...Contact List: {', '.join(contactList)}")

    # Searching for contacts
    print("...Searching for Alex in contact list")
    index = search_value(contactList, "Alex")
    print(f"...Alex found at index {index}")

    # Deleting contacts
    print("...Deleting Alex")
    print(f"...Deleted {delete_at(contactList, index)}")
    print(f"...Contact List: {', '.join(contactList)}")



if __name__ == "__main__":
    main()