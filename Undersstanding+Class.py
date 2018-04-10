
# coding: utf-8

# In[1]:


#A class with no attribute and methodb
class Employee:
    pass


# In[2]:


emp1 = Employee() #Instance-1 of class "Employee"
emp2 = Employee() #Instance-2 of class "Employee"


# In[3]:


print(emp1)
print(emp2)


# In[4]:


#Giving unique attribute to each instances


# In[5]:


emp1.firstname = "Vaibhav"
emp1.lastname = "Rai"
emp1.email = "VaibhavRai@gmail.com"
emp1.sal = 400


# In[6]:


emp2.firstname = "Test"
emp2.lastname = "User"
emp2.email = "TestUser@gmail.com"
emp2.sal = 550


# In[8]:


print(emp1.firstname)
print(emp1.lastname)
print(emp1.email)
print(emp2.firstname)
print(emp2.lastname)
print(emp2.email)


# In[9]:


#The said above method is tiring, cumbersome and error prone so we create an init method to automate it


# In[14]:


class Employee1:
    def __init__(self,firstname,lastname,sal): #values of init method
        self.firstname = firstname #It is same as doing emp1.firstname = "Vaibhav"
        self.lastname = lastname #can also be self.lname = lastname
        self.sal = sal
        self.email = firstname+lastname+"@gmail.com"


# In[22]:


#firstname,lasstname,saal,email are now attribute for class Employee1
#now we can pass values for init method of Employee calss when we instatise it
#In every class, the instance is passed as first attribute for a method that why use self


# In[15]:


emp3 = Employee1("Vaibhav","Rai",400) #"emp3" is passed as self for init method of employee classs
emp4 = Employee1("Test","User",550)
print(emp3)
print(emp4)


# In[19]:


print(emp3.firstname)
print(emp3.sal)
print(emp3.email)
print(emp4.firstname)
print(emp4.sal)
print(emp4.email)


# In[20]:


print("{} {}".format(emp4.firstname,emp4.lastname)) #But again this is tedious so we will now create a method in class


# In[23]:


class Employee2:
    def __init__(self,firstname,lastname,sal): #values of init method
        self.firstname = firstname #It is same as doing emp1.firstname = "Vaibhav"
        self.lastname = lastname #can also be self.lname = lastname
        self.sal = sal
        self.email = firstname+lastname+"@gmail.com"
    def fullname(self): #a method for printing full name
        return "{} {}".format(self.firstname,self.lastname)


# In[25]:


emp5 = Employee2("Test2","User2",600)


# In[31]:


print(emp5.fullname()) #emp5 is the instance,passed as self to fullname method
print(emp5.fullname) #this will tell that fullname is a method and not return its value


# In[30]:


emp5.firstname


# In[35]:


print(emp5.fullname())
print(Employee2.fullname(emp5))# here instead of calling a method, we are calling the class and then selecting the method,
#so we need to pass self ie. emp5 manually


# In[1]:


#Class Variable are same for each instances. name,sal,email were not class variable rather instance variables


# In[8]:


class Employee3: #without class variable
    
    def __init__(self,firstname,lastname,sal): #values of init method
        self.firstname = firstname #It is same as doing emp1.firstname = "Vaibhav"
        self.lastname = lastname #can also be self.lname = lastname
        self.sal = sal
        self.email = firstname+lastname+"@gmail.com"
    def fullname(self): #a method for printing full name
        return "{} {}".format(self.firstname,self.lastname)
    def apply_raise(self):
        self.sal = int(self.sal * 1.04)
    


# In[12]:


emp6 = Employee3("Test3","User3",600)


# In[13]:


print(emp6.sal)
emp6.apply_raise() #applying salary raise method.


# In[14]:


print(emp6.sal)#raised salary but it is not useful as we can not change the raise amount of 4%, so we declare Class Variable


# In[46]:


class Employee5:
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
    
    


# In[48]:


print(Employee5.no_of_emp) #Since we do not want to change no_of_employee inherently and want to keep it global so we used
#Employee5.no_of_emp rather than self.no_of_emp


# In[49]:


emp7 = Employee5("Test4","Yuser",1000)
print(emp7.sal)


# In[50]:


print(Employee5.no_of_emp)


# In[51]:


emp8 = Employee5("Teaser","Trailer",900)


# In[52]:


print(Employee5.no_of_emp)


# In[29]:


emp7.apply_raise()
print(emp7.sal) #4% raise applied


# In[35]:


emp7.raise_amount


# In[36]:


emp8.raise_amount


# In[31]:


Employee5.raise_amount


# In[32]:


#When we call the method apply_raise() then emp7 goes as self, but method has to search raise_amount variable, so first it will
#search inside the method, if not found then it searches at class level. This is called inheritence


# In[37]:


emp7.__dict__ #all values of attributes displayed as list. Notice we do not have raise_amount


# In[39]:


Employee5.__dict__ #here we find raise_amount as 1.04


# In[41]:


#changing value of raise amount. It gets reflected at both class level and instance level
Employee5.raise_amount = 1.05
print(Employee5.raise_amount)
print(emp7.raise_amount)
print(emp8.raise_amount)


# In[42]:


#it is not always necessary to use Class variable. we can define instance variable while making an instance


# In[44]:


emp7.raise_amount = 2.00
print(Employee5.raise_amount)
print(emp7.raise_amount)#Change refleced only on this class
print(emp8.raise_amount)

print(emp7.__dict__) #now we can see raise_amount attribute in emp7 instance namespace
print(emp8.__dict__)


# In[ ]:


#While defining class if we did """self.sal = int(self.sal * Employee5.raise_amount)""" 
#instead of """self.sal = int(self.sal * self.raise_amount)""" then the method would have always looked for class variable


# In[53]:


print(Employee5.no_of_emp)

