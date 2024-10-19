class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.email = firstName + '.' + lastName + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def getFullName(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        firstName, lastName, pay = emp_str.split('-')
        return cls(firstName, lastName, pay)
        
emp_1 = Employee('Ikura', 'Lila', 100000)
emp_2 = Employee('Ayasee', 'Kula', 95000)

Employee.set_raise_amount(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.set_raise_amount(1.06)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('#####################################')

emp_string_1 = 'John-Doe-70000'
emp_string_2 = 'Steve-Smith-30000'
emp_string_3 = 'Jane-Doe-90000'


firstName, lastName, pay = emp_string_1.split('-')
new_emp_1 = Employee(firstName, lastName, pay)

print(new_emp_1.email)
print(new_emp_1.pay)

new_emp_2 = Employee.from_string(emp_string_2)

print(new_emp_2.email)
print(new_emp_2.pay)
