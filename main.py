Password = input("Enter in a password: ")
accepted_password = input("Confirm your password: ")

def info():
    accepted_password = input("Confirm your password: ")
    if Password == accepted_password:
        print('Password validated')
    elif Password!=accepted_password:
          print('Password invalid')
          input("Enter in a password: ")
          input("Confirm your password: ")
info()         