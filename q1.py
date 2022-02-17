def tiped_salary(salary):
    tip_salary = salary - salary*13/100
    return(float(tip_salary))

salary = float(input('Type your salary: '))
print(tiped_salary(salary))

def annual_salary(tip_salary):
    annual_salary = tip_salary*12
    return(annual_salary)

print(annual_salary(tiped_salary(salary)))