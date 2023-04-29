class employee:   #class
    def __init__(self,first,last): #self is an instance of a class self=emp_1 or self=emp_2
        self.first=first
        self.last=last
    def generateEmail(self):
        return f"{self.first}.{self.last}@company.com"
    def fullName(self):
        return("{} {}".format(self.first,self.last))
    


'''both are the instances of the same class '''
emp_1=employee("test1","user1") #instance of a class 
emp_2=employee("test2","user2") #2nd instance of the same class



emp_1.last="user1"
emp_1.email=emp_1.first+"."+emp_1.last+"@company.com"


emp_2.first="test2"
emp_2.last="user2"
emp_2.email=emp_1.first+"."+emp_2.last+"@company.com"

print(emp_2.generateEmail())
print(emp_1.fullName())

print(emp_1.first)
print(emp_2.last)

