#Enter the user age
age=int(input("Please enter your age: "))

#Conditions:

if(age<13):
    print("You qualify for the kiddie discount.")

elif(age==21):
    print("Congrats on your 21st.")

elif(40<=age<65):
    print("You're over the hill.")

elif(65<=age<=100):
    print("Enjoy your retirement!")

elif(age>100):
    print("Sorry, you're dead.")

else:
    print("Age is but a number.")
