import pandas as pd
import numpy as np

#series
my_dict = {"Osimhen":26,"Icardi" : 31 , "Davinson" : 26 , "Torreira" : 28}

my_series = pd.Series(my_dict)

# print(my_series)
#Also we can merge it with using Series
age_list = [26,31,26,28]

name_list = ["Osimhen" , "Icardi" , "Davinson" , "Torreira"]


my_series_merged = pd.Series(age_list,name_list)

# print(my_series_merged)


#with numpy

new_numpy_array = np.array([10,20,30,40])
 
x=pd.Series(new_numpy_array)

# print(x)



my_series_2 = pd.Series(data=new_numpy_array,index=name_list)

my_series_2["Osimhen"] = 60


# print(my_series_2)






#DATAFRAMESSS


