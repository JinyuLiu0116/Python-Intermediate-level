credit_number="1234-5678-9012-3456"

print(credit_number[0])
print(f"The first four digits of the number: {credit_number[0:4]}")
print(f"The last four digits of the number: {credit_number[15:]}")
print(credit_number[::5])
print(credit_number[::-5])

last_digits = credit_number[-4:]
print(f"Your number is: ####-####-####-{last_digits}")

print(f"The reversted number is:{credit_number[::-1]}")