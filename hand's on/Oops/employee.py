import itertools
class Employee:
    counter = Empno = itertools.count(100)
    
    def __init__(self, name, sal):
        self.ename = name
        self.sal = sal
        self.Empno = next(self.counter)
    
    def create_New_Emp(self):
        ename = self.ename
        Empno = self.Empno
        sal = self.sal
        return Empno,ename,sal


    def delete_Emp(self):
        print("will be deleted")
        self.ename = ""
        self.Empno = None
        self.sal = None

    def display_emp(self):
        print("Employee Name: ", self.ename)
        print("Salary: ",self.sal)
        print("Employee no: ", self.Empno)


e1 = Employee("Sam",6000)
e2 = Employee("Ron" ,10000)
e1.create_New_Emp()
e1.display_emp()
e1.delete_Emp()
            
e2.create_New_Emp()
e1.display_emp()
e2.display_emp()
e2.delete_Emp()
                  
        
        
        
