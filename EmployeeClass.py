class Employee: #Write a class named Employee
    
    def __init__(self, name, ID, dept, job, salary): #attributes 
        self.__name = name #accept argument for each attribute 
        self.__ID = ID
        self.__dept = dept
        self.__job = job
        self.__salary = salary
    
    #accessor method for name
    def get_name(self):
        return self.__name
    
    #accessor method for ID number
    def get_ID(self):
        return self.__ID
    
    #accessor method for department
    def get_dept(self):
        return self.__dept
    
    #accessor method for job title
    def get_job(self):
        return self.__job
    
    #accessor method for monthly salary
    def get_salary(self):
        return self.__salary