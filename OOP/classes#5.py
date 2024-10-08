class Employee:
  def __init__(self, firstName, lastName, pay):
    self.firstName = firstName
    self.lastName = lastName
    self.pay = pay
    self.email = firstName + '.' + lastName + '@company.com'

emp_1 = Employee('Corey', 'Schater', 50000)
emp_2 = Employee('Test', 'User', 5000)

print(emp_1)
print(emp_2)

emp_1.firstName = 'Corey'
emp_1.lastName = 'Schater'
emp_1.email = 'Corey.Schater@company.com'
emp_1.pay = 50000

emp_2.firstName = 'Test'
emp_2.lastName = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 5000

print(emp_1.email)
print(emp_2.email)
