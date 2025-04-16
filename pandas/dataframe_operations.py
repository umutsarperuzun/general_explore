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
q=my_new_data_frame.fillna(20)

print(q)