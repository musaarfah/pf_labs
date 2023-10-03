a=int(input('Basic Salary : '))
Medical_Allowance = a*0.1
Conveyance_Allowance=a*0.5
House_Rent= a*0.45
Gross_Salary=int((a+Medical_Allowance+Conveyance_Allowance+House_Rent))
print('Gross Salary :',Gross_Salary)
Tax=(a*0.1)
Net_Salary=int((Gross_Salary-Tax))
print('Net Salary :',Net_Salary)