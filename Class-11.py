#Inheritance
#Modifying inherited class by extra attributes from parent class
#Adding a new inheritence

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
    raise_amount = 1.10

    def __init__(self,firstname,lastname,sal,language): #We created a new attribute i.e programming language
        super().__init__(firstname,lastname,sal) #This tells python that following attributes will be handled by the parent class
        #Employee.__init__(self,firstname,lastname,sal) this way is better when we have multiple classes
        self.language = language


class Manager(Employee): #This is for creating list of employees under a manager

    def __init__(self,firstname,lastname,sal,employees = None):
        super().__init__(firstname,lastname,sal)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print("-->",emp.fullname())



emp1 = Employee("Vaibhav","Rai",5000) #this is instance for Employee Class
dev1 = Developer("Test","Developer",6000,"Pyhton")#now here we need to specify  another attribute language

mgr1 = Manager("Dell","Inspiron",70000,[dev1]) #We can pass list of employees under mgr1 as we can also leave it blank
print(mgr1.fullname())
mgr1.print_emps() #Viewing employees under mgr1
print()
mgr1.add_emp(emp1) #Adding new employee under mgr1
mgr1.print_emps()
print()
mgr1.remove_emp(emp1) #Removing an employee from mgr list
mgr1.print_emps()



