#A class with no attribute and methodb
class Employee:
    pass

emp1 = Employee() #Instance-1 of class "Employee"
emp2 = Employee() #Instance-2 of class "Employee"

print(emp1)
print(emp2)

#Giving unique attribute to each instances
emp1.firstname = "Vaibhav"
emp1.lastname = "Rai"
emp1.email = "VaibhavRai@gmail.com"
emp1.sal = 400

emp2.firstname = "Test"
emp2.lastname = "User"
emp2.email = "TestUser@gmail.com"
emp2.sal = 550

print(emp1.firstname)
print(emp1.lastname)
print(emp1.email)
print(emp2.firstname)
print(emp2.lastname)
print(emp2.email)

#The said above method is tiring, cumbersome and error prone,
#so we create an init method to automate it in class-2
