class PayrollDeduction: #Write a class 
    
    def __init__(self, descript, date, charge, eID): #attributes 
        self.__descript = descript
        self.__date = date
        self.__charge = charge
        self.__eID = eID
        
    #accessor method for description
    def get_descript(self):
        return self.__descript
    
    #accessor method for date
    def get_date(self):
        return self.__date
    
    #accessor method for charge amount
    def get_charge(self):
        return self.__charge
    
    #accessor method for employee ID number
    def getEmployeeID(self):
        return self.__eID