import numpy as np

#numpy array

# my_list =[10,20,30,40]

# my_numpy_array = np.array(my_list)
# my_numpy_array[0] = 100

# print(my_numpy_array.max())
 

my_list = [[1,0,0],[1,1,1],[0,1,0]]

my_matrix_array = np.array(my_list)

# print(my_matrix_array.shape)

x=np.arange(0,10)
# print(x)


y=np.ones((10,10))
# print(y)

#numpy randint using
q=np.random.randint(0,10,2)
# print(q)


#numpy arrays methods

my_numpy_list = np.arange(0,20)

my_numpy_list[4:9:2] = -10
# print(my_numpy_list)


other_list = np.arange(0,15)

sliced_list = other_list[0:5]

sliced_list[:] = 100

# print(other_list)

# print(sliced_list)

#numpy copy method
my_numpy_list3= np.arange(0,20)

my_numpy_list3_copy = my_numpy_list3.copy()

slicing_3 = my_numpy_list3_copy[4:9]

slicing_3[:] = -100
print(slicing_3)
print(my_numpy_list3_copy)
print(my_numpy_list3)


#numpy operation with arrays
new_array = np.random.randint(0,150,25)

print(new_array)

result_array=new_array > 50

print(new_array[result_array])


last_array = np.arange(0,30)

print(last_array + last_array)