from datetime import datetime
name = input("Entre your name:")
age = int(input("Entre your age:"))
hundredth_age = int((100-age) + datetime.now().year)
if age > 0:
    print("Hlo",name , "you will turn 100 years old in the year" , hundredth_age)
else:
    print("Invalid age")