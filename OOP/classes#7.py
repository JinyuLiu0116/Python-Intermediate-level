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
