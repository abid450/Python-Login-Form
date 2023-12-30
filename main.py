# Login Registration Form-------------------------------------
print("Please Login The Registation")
UserName = input("Enter your UserName : ")
Gmail    = input("Enter your Gmail    : ")
if UserName == Gmail:
    print("Please Enter The Correct Number")
Password = input("Enter your Password : ")

if Gmail == Password:
    print("Please Enter The Password")
Confirm = input("Confirm your Password : ")

if Confirm == Password:
    print("Your Login SuccessFully")

else:
    print("Please Confirm Your Password")
