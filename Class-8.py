#Inheritance
class Employee:
    raise_amount = 1.04 #Class variable
    no_of_emp = 0 #another class variable
    
    def __init__(self,firstname,lastname,sal): #values of init method #Regular Method
        self.firstname = firstname #It is same as doing emp1.firstname = "Vaibhav"
        self.lastname = lastname #can also be self.lname = lastname
        self.sal = sal
        self.email = firstname+lastname+"@gmail.com"
        
        Employee.no_of_emp += 1 #every time a new emp is added, counter increasses
    
    def fullname(self): #a method for printing full name #Regular Method
        return "{} {}".format(self.firstname,self.lastname)
    
    def apply_raise(self): #Regular Method
        self.sal = int(self.sal * self.raise_amount) #Either we can give class name or self

class Developer(Employee): #Inherited class. Copies all properties(attributes & methods) of Employee class
    pass


emp1 = Employee("Vaibhav","Rai",5000) #this is instance for Employee Class

dev1 = Developer("Test","User",6000)#this is an instance for Developer class. But since it is empty, so python will look for its inherited class i.e. Employee

print("emp1",emp1.email,emp1.sal)
print("dev1",dev1.email,dev1.sal)
print()

#Increasing salary for developer

print("Sal",dev1.sal)
print("Raise",Developer.raise_amount) #Inherited form Employee class
dev1.apply_raise()
print("Raised Sal",dev1.sal)


"""
To check order for Developer method, try help(Developer)

"""
