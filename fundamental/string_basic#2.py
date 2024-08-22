user_name = input("Enter a user name:")
if len(user_name) < 5:
    print("An user name must has at less five charactors")
elif len(user_name) > 12:
    print("Your user name cannot be more than 12 charactors")
elif not user_name.find(" ")==-1:
    print("Your user name cannot contain spaces")
else:
    print(f"Welcome {user_name}")

email="@gmail.com"
email_account=user_name+email
print(f"Your email account is: {email_account}")

