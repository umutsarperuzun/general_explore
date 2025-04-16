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

my_data = np.array([[10,20,30],[40,50,60],[70,80,90],[100,110,120]])

my_names = ["Ali","Sarper","Semra","Berkin"]

my_columns = ["Jan","Feb","Mar"]

my_data_frame = pd.DataFrame(my_data,index=my_names,columns=my_columns)

# print(my_data_frame["Feb"])

feb_series = my_data_frame["Feb"]

# print(my_data_frame["Jan"].mean())

# print(my_data_frame.iloc[0])


my_data_frame["Apr"]=my_data_frame["Mar"] * 2

# print(my_data_frame["Apr"])

# print(my_data_frame["Mar"])

#Remove to data (axis 0 row axis 1 column)
y= my_data_frame.drop("Berkin",axis=0)

# print(y)

# print(my_data_frame)


#Remove to column or row permenantly
my_data_frame.drop("Apr",axis=1,inplace=True)



#Filtering
boolean_frame = my_data_frame > 30

# print(boolean_frame)


q=my_data_frame["Mar"] > 50

# print(q)


#Replace indexes

w=my_data_frame.reset_index()

# print(w)


my_data_frame["NewIndex"] = ["Al","Sarper" , " Semos" , "Niyaz"]

r=(my_data_frame.set_index("NewIndex"))

my_data_frame.drop("NewIndex",axis=1,inplace=True)

print(my_data_frame)





