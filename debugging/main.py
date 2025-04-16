class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age=age
    

    def increaseAge(self):
        self.age+= 1
    def decreaseAge(self):
        if self.age > 0:
            self.age-= 1

        
    def __str__ (self):
        return f"{self.name} is {self.age} years old."
        
    

sarper = Person("Sarper",10)
sarper.decreaseAge()
sarper.decreaseAge()
sarper.decreaseAge()
sarper.decreaseAge()
sarper.decreaseAge()
sarper.decreaseAge()
sarper.decreaseAge()



print(sarper)
