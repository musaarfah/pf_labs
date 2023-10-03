basic_salary=int(input('Basic Salary : '))
medical_allowance=int(basic_salary*0.1)
conveyance_allowance=int((basic_salary*0.15))
house_rent=int((basic_salary*0.45))
gross_salary= int((basic_salary+medical_allowance+conveyance_allowance+house_rent))
print('Basic Salary = ',basic_salary)
print('Medical Allowance : ',medical_allowance)
print('Conveyance Allowance : ',conveyance_allowance)
print('House Rent : ',house_rent)
print('-----------------------------')
print('Gross Salary : ',gross_salary)
annual_gross_salary=gross_salary*12
a=int(gross_salary*0.1)
b=int(gross_salary*0.15)
c=int(gross_salary*0.20)
d=int(gross_salary*0.25)
if annual_gross_salary<=200000:
    Tax=0
    print('Less Tax = ',Tax)
    print('-----------------------')
    print('Net Salary = ',gross_salary-Tax)
if annual_gross_salary>200000 and annual_gross_salary<400000:
    print('Less Tax = ',a)
    print('-----------------------')
    print('Net Salary = ',gross_salary-a)
if annual_gross_salary>400000 and annual_gross_salary<600000:
    print('Less Tax = ',b)
    print('-----------------------')
    print('Net Salary = ',gross_salary-b)
if annual_gross_salary>600000 and annual_gross_salary<800000:
    print('Less Tax = ',c)
    print('-----------------------')
    print('Net Salary = ',gross_salary-c)
if annual_gross_salary>800000:
    print('Less Tax = ',d)
    print('-----------------------')
    print('Net Salary = ',gross_salary-d)
