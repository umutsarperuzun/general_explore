import pandas as pd
import numpy as np


salary_dict = { "Name" : ["A","B","C"],"Programming Language" : ["Python" ,"Java" ,"Swift"],"Salary":[100,90,80]}

my_frame =pd.DataFrame(salary_dict,index=[1,2,3])

salary_dict2 = { "Name" : ["G","H","R"],"Programming Language" : ["Python","Java" ,"Swift"],"Salary":[170,160,150]}

my_frame2 = pd.DataFrame(salary_dict2,index=[4,5,6])

salary_dict3 = {"Name" : ["D","E","F"],"Programming Language" : ["Python","Java" ,"Swift"],"Salary":[70,60,50]}

my_frame3 = pd.DataFrame(salary_dict3,index=[7,8,9])



#CONCATENATION

# x = pd.concat([my_frame,my_frame2,my_frame3])

# print(x)



#MERGE

# y=pd.merge(my_frame,my_frame2,on="Programming Language")

# print(y)

#UNIQUE
new_salary_frame = pd.DataFrame({"Name":["Ali","Sarper","Semra","Berkin"],"Salary" : [10,20,30,40] ,"Age" : [30,40,50,60]})

# z=new_salary_frame["Name"].nunique()

# print(z)


#USING FUNCTION IN DATAFRAMES
def grossToNet(salary):
    return salary *0.65


e = new_salary_frame["Salary"].apply(grossToNet)

print(e)














