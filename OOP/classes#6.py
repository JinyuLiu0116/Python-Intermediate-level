class Employee:
  raise_amount = 1.04
  def __init__(self, firstName, lastName, pay):
    self.firstName = firstName
    self.lastName = lastName
    self.pay = pay
    self.email = fristName + '.' + lastName + '@company.com'

  def getFullNmae(self):
    return '{} {}'.format(self.firstName, self.lastName)

  def apply_raise(self):
    self.pay = int(self.pay * Employee.raise_amount)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 5000)

emp_1.apply_raise()
print(emp_1.pay)
print(emp_1.__dict__) #check all elements
