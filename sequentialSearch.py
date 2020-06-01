# Author: Nguyen L.
# Date:   May 7th, 2020
# Prompt: Write a program for sequential search.
# Sequential search: in computer science, linear search or sequential search is a method for finding a particular value in a list
# that checks each element in sequence until the desired element is found or the list is exhausted. The list need not be ordered.

# function for sequential search
def sequentialSearch(my_list, item):

    # essential variables
    found = False
    index = 0

    while index < len(my_list) and found != True:

        if my_list[index] == item:
            found = True
        else:
            found = False
            index += 1

    return found

my_list = [ 2, 4, 3, 6, 1, 0, 10, 15]

item_to_find = int(input("Enter item to find: "))
print(sequentialSearch(my_list, item_to_find))