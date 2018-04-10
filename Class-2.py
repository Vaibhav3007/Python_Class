class Employee:
    def __init__(self,firstname,lastname,sal): #values of init method
        self.firstname = firstname #It is same as doing emp1.firstname = "Vaibhav"
        self.lastname = lastname #can also be self.lname = lastname
        self.sal = sal
        self.email = firstname+lastname+"@gmail.com"


#firstname,lasstname,saal,email are now attribute for class Employee1
#now we can pass values for init method of Employee calss when we instatise it
#In every class, the instance is passed as first attribute for a method that why use self

emp1 = Employee("Vaibhav","Rai",400) #"emp1" is passed as self for init method of employee classs
emp2 = Employee("Test","User",550)
print(emp1)
print(emp2)


print(emp1.firstname)
print(emp1.sal)
print(emp1.email)
print(emp2.firstname)
print(emp2.sal)
print(emp2.email)



print("{} {}".format(emp1.firstname,emp1.lastname)) #But again this is tedious so we will now create a method in class-3
print("{} {}".format(emp2.firstname,emp2.lastname))
