#Regular method takes instance asfirst method(self).
#To avoid this we can create a class method using a decorator

class Employee:
    raise_amount = 1.04 #Class variable
    no_of_emp = 0 #another class variable
    
    def __init__(self,firstname,lastname,sal): #values of init method
        self.firstname = firstname #It is same as doing emp1.firstname = "Vaibhav"
        self.lastname = lastname #can also be self.lname = lastname
        self.sal = sal
        self.email = firstname+lastname+"@gmail.com"
        
        Employee.no_of_emp += 1 #every time a new emp is added, counter increasses
    
    def fullname(self): #a method for printing full name
        return "{} {}".format(self.firstname,self.lastname)
    
    def apply_raise(self):
        self.sal = int(self.sal * self.raise_amount) #Either we can give class name or self
    
    @classmethod
    def set_rais_amount(cls, amount): #this is a class method. rather than instance, it takes value for class
        cls.raise_amount = amount





#Adding data

emp1 = Employee("Test1","User1",8500)
emp2 = Employee("Test2","User2",9000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print()

Employee.set_rais_amount(1.05) #cls taken as class rather than instance
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print()

emp_str_1 = "Test3-User3-1000" #another way of creating users. We can create a new class method for such kind of data
firstname,lastname,sal = emp_str_1.split("-")
new_emp_1 = Employee(firstname,lastname,sal)
print(new_emp_1.firstname)
print(new_emp_1.email)
print(new_emp_1.sal)
