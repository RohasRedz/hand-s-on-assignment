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



class Job:
    def __init__(self,job,losal,hisal):
        self.job = job
        self.losal = losal
        self.hisal = hisal

class Derived(Employee, Job):

    def __init__(self, name, sal,job,losal,hisal):
        Employee.__init__(self,  name, sal)
        Job.__init__(self, job,losal,hisal)
        
    
        
    def create_New_Emp(self):
        
        ename = self.ename
        
        sal = self.sal
        job = self.job
        hisal= self.hisal
        losal = self.losal
        return ename,sal,job,hisal,losal

    def bonus(self):
        bonus
        self.sal = self.sal + self.bonus

    
    def display_emp(self):
        print("Employee Name: ", self.ename)
        print("Salary: ",self.sal)
        print("Employee no: ", self.Empno)
        print("Job: ", self.job)
        print("Lowest Salary: ",self.losal)
        print("Highest Salary: ", self.hisal)
        
        


e1 = Derived("Ron",1000,"Engineer",900,10000)
e1.create_New_Emp()
e1.display_emp()

        
        
        
