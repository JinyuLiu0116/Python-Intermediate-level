class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + ' ' + lastName + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def getFullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)

    

emp_1 = Employee('Ikura', 'Lila', 100000)
emp_2 = Employee('Ayasee', 'Kula', 95000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
