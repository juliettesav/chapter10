from EmployeeClass import Employee
from PayrollDeductionClass import PayrollDeduction

#Employee 
employee= Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)

#Payroll deductions 
d1= PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
d2= PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
d3= PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
d4= PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
d5= PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

#Print report
print()
print("*** Employee Pay ***")
print("Name:", employee.get_name())
print("ID Number:", employee.get_ID())
print("Department:", employee.get_dept())
print("Gross Pay: $", float(employee.get_salary()), sep='')
print("Net Pay: $", employee.get_salary()-d2.get_charge()-d4.get_charge()-d5.get_charge(), sep='')
print()