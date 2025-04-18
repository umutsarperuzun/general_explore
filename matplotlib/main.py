import numpy as np
import matplotlib.pyplot as plt


age_list =[20,25,30,35,40,45,50,60,70,80]

weight_list = [70,55,105,110,92,86,97,108,110,72]

age_list_numpy = np.array(age_list)
weight_list_numpy = np.array(weight_list)


#Line graph
# plt.plot(age_list,weight_list,"r")
# plt.xlabel("Age")
# plt.ylabel("Weight")
# plt.title("Age-Weight Graph")

# plt.show()



my_numpy1=np.linspace(0,15,20)

my_numpy2=my_numpy1 **3

#Point graph
# plt.scatter(my_numpy1,my_numpy2, color="r")
# plt.xlabel("number1")
# plt.ylabel("number2")
# plt.title("Number Comparison Graph")
# plt.show()


# plt.subplot(1,2,1) #1 row,2 column ,1.graph
# plt.plot(my_numpy1,my_numpy2,"r--")
# plt.subplot(1,2,2)
# plt.plot(my_numpy2,my_numpy1,"g*")
# plt.show()



#FIGURE
# my_figure=plt.figure()
# my_axes = my_figure.add_axes([0.1,0.1,0.5,0.5])
# my_axes.plot(my_numpy1,my_numpy2,"g*")
# my_axes.set_xlabel("X Data")
# my_axes.set_ylabel("Y Data")


my_figure2=plt.figure()

my_axes3 = my_figure2.add_axes([0.1,0.1,0.9,0.9])
my_axes3.plot(my_numpy1,my_numpy2,"r-*")
my_axes3.set_xlabel("X Data Large")
my_axes3.set_ylabel("Y Data Large")
my_axes3.set_title("Large Graph")

my_axes2 = my_figure2.add_axes([0.2,0.4,0.4,0.5])
my_axes2.plot(my_numpy1,my_numpy2,"g*")
my_axes2.set_xlabel("X Data Small")
my_axes2.set_ylabel("Y Data Small")
my_axes2.set_title("Small Graph")
plt.show()


# (my_fig,my_axe) = plt.subplots()
# my_numpy3 = np.linspace(0,15,20)
# my_numpy4 = my_numpy3 **2
# my_axe.plot(my_numpy3,my_numpy4,color="#CD621D",alpha=1)#alpha using for opacity
# my_axe.plot(my_numpy4,my_numpy3,color="#B81DCD",alpha=0.5)


# (new_fig,new_axe) = plt.subplots()
# new_axe.plot(my_numpy1,my_numpy1+3,color="#B81DCD",linewidth=1.0) #linewidth for set to width level
# new_axe.plot(my_numpy1,my_numpy1+2,color="#CD621D",linewidth=1.0,linestyle="-.") #set to line types
# new_axe.plot(my_numpy1,my_numpy1+4,color="black",linewidth=1.0,linestyle="-.",marker="+") # showing data with marks


#Histogram
new_numpy = np.random.randint(0,100,40)
plt.hist(new_numpy)

plt.show()


#Save to the graphs
my_figure2.savefig("myfig.png",dpi=200)







