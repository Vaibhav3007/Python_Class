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
    
    @classmethod #Class Method
    def set_rais_amount(cls, amount): #this is a class method. rather than instance, it takes value for class
        cls.raise_amount = amount

    @classmethod #We have defines here a constructor #Class Method
    def from_string(cls, emp_str): #cls is taken for class so it is a class method, emp_str is obtained when class metod is called
        firstname,lastname,sal = emp_str.split("-")#emp_str is split
        return cls(firstname,lastname,sal)#the three splitted values are sent to cls i.e. Employee

"""
the below code is converted to class method from_string

emp_str_1 = "Test1-User1-1000"
firstname,lastname,sal = emp_str_1.split("-")
new_emp_1 = Employee(firstname,lastname,sal)
"""

emp_str_1 = "Test1-User1-1000"
emp_str_2 = "Test1-User2-1040"

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)
