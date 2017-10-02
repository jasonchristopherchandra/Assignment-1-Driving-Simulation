number = input("Enter number ")
if  number.isnumeric():
    if  int(number)%2 == 0:
        print("Bob")
    else:
        print("Alice")
else:
   print("You input a non numberic value. Program stopped")
