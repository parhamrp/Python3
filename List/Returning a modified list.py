#  returning a list without the first and the last elements.
def modified_list(sample_list):
      del sample_list[0]
      del sample_list[-1]
      return sample_list

my_list = [1, 2, 3, 4, 5]
print (modified_list(my_list))
      
