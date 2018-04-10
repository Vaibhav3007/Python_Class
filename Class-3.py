class Employee:
    def __init__(self,firstname,lastname,sal): #values of init method
        self.firstname = firstname #It is same as doing emp1.firstname = "Vaibhav"
        self.lastname = lastname #can also be self.lname = lastname
        self.sal = sal
        self.email = firstname+lastname+"@gmail.com"
    def fullname(self): #a method for printing full name
        return "{} {}".format(self.firstname,self.lastname)

emp1 = Employee("Test","User",600)



print(emp1.fullname()) #emp5 is the instance,passed as self to fullname method
print(emp1.fullname) #this will tell that fullname is a method and not return its value

emp1.firstname

print(emp1.fullname())
print(Employee.fullname(emp1))# here instead of calling a method, we are calling the class and then selecting the method,
#so we need to pass self i.e. emp5 manually
