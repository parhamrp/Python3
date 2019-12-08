# finding how much an element cam in a list.
def element_count(sample_list, element):
      count  = 0 
      list_lenght = len(sample_list)
      for item in range(0 , list_lenght):
            if element == sample_list[item]:
                  count += 1
      return count

# my_list = [1, 3, 5, 7, 9, 11, 3, 5, 3, 5, 5]
# print (element_count(my_list, 5))

      
