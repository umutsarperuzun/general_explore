import pandas as pd
import numpy as np



my_dict = {"Ali":[40,20,np.nan],"Sarper":[20,np.nan,50],"Semra":[30,40,50]}

my_data_frame = pd.DataFrame(my_dict)

x= my_data_frame.dropna()
# print(x)

# print(my_data_frame)


my_new_dict={"Ali":[40,20,np.nan],"Sarper":[20,np.nan,50],"Semra":[30,40,50],"Berkin":[45,np.nan,np.nan]}

my_new_data_frame = pd.DataFrame(my_new_dict)

# q=my_new_data_frame.dropna(axis=1,thresh=2)

# print(q)


#filling data
# q=my_new_data_frame.fillna(20)

# print(q)





#groupby

salary_dict = {"Programming Language" : ["Python" , "Python" ,"Python" ,"Java","Java" ,"Swift"], "Name" : ["A","B","C","D","E","F"],"Salary":[100,90,80,70,60,50]}

salary_frame = pd.DataFrame(salary_dict)

group_object = salary_frame.groupby("Programming Language")

# print(group_object.count())

# print(group_object.min("Salary")) #or

# print(group_object.min(numeric_only=True))


print(group_object.describe())




# print(salary_frame)