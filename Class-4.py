#Class Variable are same for each instances. name,sal,email were not class variable rather instance variables

class Employee: #without class variable
    
    def __init__(self,firstname,lastname,sal): #values of init method
        self.firstname = firstname #It is same as doing emp1.firstname = "Vaibhav"
        self.lastname = lastname #can also be self.lname = lastname
        self.sal = sal
        self.email = firstname+lastname+"@gmail.com"
    def fullname(self): #a method for printing full name
        return "{} {}".format(self.firstname,self.lastname)
    def apply_raise(self):
        self.sal = int(self.sal * 1.04)
    
emp1 = Employee("Test3","User3",600)
print("Employee name-",emp1.firstname)
print("emp1oyee sal-",emp1.sal)
emp1.apply_raise() #applying salary raise method.
print("employee raised sal-",emp1.sal)#raised salary but it is not useful as we can not change the raise amount of 4%, so we declare Class Variable


print()



class Employee5: #with class variable
    raise_amount = 1.04 #Class variable
    no_of_emp = 0 #another class variable
    
    def __init__(self,firstname,lastname,sal): #values of init method
        self.firstname = firstname #It is same as doing emp1.firstname = "Vaibhav"
        self.lastname = lastname #can also be self.lname = lastname
        self.sal = sal
        self.email = firstname+lastname+"@gmail.com"
        
        Employee5.no_of_emp += 1 #every time a new emp is added, counter increasses
    
    def fullname(self): #a method for printing full name
        return "{} {}".format(self.firstname,self.lastname)
    
    def apply_raise(self):
        self.sal = int(self.sal * self.raise_amount) #Either we can give class name or self

print("No. of employee-",Employee5.no_of_emp) #Since we do not want to change no_of_employee inherently and want to keep it global so we used
#Employee5.no_of_emp rather than self.no_of_emp

emp7 = Employee5("Test4","Yuser",1000)
print("emp1oyee name & sal-",emp7.firstname,emp7.sal)
print("No. of employee",Employee5.no_of_emp)
emp8 = Employee5("Teaser","Trailer",900)
print("emp1oyee name & sal-",emp8.firstname,emp8.sal)
print("No. of employee",Employee5.no_of_emp)
print()


emp7.apply_raise()
print("employee name and raised sal-",emp7.firstname,emp7.sal) #4% raise applied
print()


print("Raise amount instance level",emp7.raise_amount)
print("Raise amount instance level",emp8.raise_amount)
print("Raise amount Class level",Employee5.raise_amount)
#When we call the method apply_raise() then emp7 goes as self, but method has to search raise_amount variable, so first it will
#search inside the method, if not found then it searches at class level. This is called inheritence
print()

print("emp7 instance namespace-",emp7.__dict__ )#all values of attributes displayed as list. Notice we do not have raise_amount
print("Employee5 class namespace-",Employee5.__dict__ )#here we find raise_amount as 1.04
print()


#changing value of raise amount. It gets reflected at both class level and instance level
Employee5.raise_amount = 1.05
print("Changing class variable at class level")
print("Raise amount class level",Employee5.raise_amount)
print("Raise amount instance level",emp7.raise_amount)
print("Raise amount instance level",emp8.raise_amount)
print()

#it is not always necessary to use Class variable. we can define instance variable while making an instance
emp7.raise_amount = 2.00
print("Changing class variable but at instance level")
print("Raise amount class level",Employee5.raise_amount)
print("Raise amount instance level",emp7.raise_amount)#Change refleced only on this class
print("Raise amount instance level",emp8.raise_amount)

print("emp7 instance namespace-",emp7.__dict__) #now we can see raise_amount attribute in emp7 instance namespace
print("emp8 instance namespace-",emp8.__dict__)

#While defining class if we did """self.sal = int(self.sal * Employee5.raise_amount)""" 
#instead of """self.sal = int(self.sal * self.raise_amount)""" then the method would have always looked for class variable
print("No. of employee-",Employee5.no_of_emp)

