class Employee:
  def __init__(self, firstName, lastName, pay):
    self.firstName = firstName
    self.lastName = lastName
    self.pay = pay
    self.email = fristName + '.' + lastName + '@company.com'

  def getFullNmae(self):
    return '{} {}'.format(self.firstName, self.lastName)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 5000)
