# # Ascending soprt for a list.
# def list_element_swap_asc(sample_list):
      
#     my_list = sample_list[:]
  
#     length = 0
#     for element in my_list:
#         length = length + 1
#     unSorted = True
#     while unSorted:
#         unSorted = False
#         for item in range(0, length-1):
#             if my_list[item] < my_list[item + 1]:
#                 temp_variable = my_list[item]
#                 my_list[item] = my_list[item + 1]
#                 my_list[item + 1] = temp_variable
#                 unSorted = True
#     return my_list  
# one_list = [1, 3, 5, 6 ,7 ,78, 34, 2121]
# list_element_swap_asc(one_list)
# print (one_list)


################### Sample Solution ###################
def _merge_and_sort_sample_(a, b):
    a.extend(b)
    # Create a new list
    new_list = []
    # Loop until a becomes empty
    while a:
        # set an arbitrary element as the minimum
        # in this case we chose the first index
        maximum = a[0]
        # loop through the list and
        # find the element that is smallest
        for element in a:
            if element > maximum:
                maximum = element
        # append the smallest element to the new list
        new_list.append(maximum)
        # now remove that smallest element from the original list
        a.remove(maximum)
    # Ultimately a will become empty
    # and the loop will end
    # now return the new list
    return new_list


list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10]
#and now I just found the best way to use or recall a function:D
print(_merge_and_sort_sample_(list1, list2))    
