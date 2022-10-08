"""
Write a function called chop that takes a list and modifies it, removing the first and last elements,
and returns None. Then write a function called middle that takes a list and returns a new list that
contains all but the first and last elements.
"""


def chop(a_list):
    """
    Takes a list, modifies it, removing the first and last elements, and returns None.
    Input:  a_list -- a list
    Output: None
    """
    del a_list[0]  # Removes the first element
    del a_list[-1]  # Removes the last element
    return None


def middle(a_list):
    """
    Takes a list and returns a new list that contains all but the first and last elements.
    Input: a_list -- a list
    Output: new -- new list with first and last elements removed
    """
    new = a_list[1:]  # Stores all but the first element
    del new[-1]  # Deletes the last element
    return new


list_1 = [1, 2, 3, 4, 5, 6, 7]
list_2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

chop_list = chop(list_1)
print(list_1)   # List_1 has been modified
print(chop_list)    # Prints None

middle_list = middle(list_2)
print(list_2)   # Original list is unchanged
print(middle_list)  # Prints new list
