#Assing each competition a time using float
time_1=float(input("Please give me how many minutes it took you to finish swimming:"))
time_2=float(input("Please give me how many minutes it took you to finish cycling: "))
time_3=float(input("Please give me how many minutes it took you to finish running: " ))

#Calculate and display the total time for the thriatlon
time=time_1+time_2+time_3
print(f"The total time taken to complete the triathlon is: {time}")

#Condition that determines which award category 
if(0<time<=100):
    print("The award that the participant will receive is: Provincial Colours")

elif(100<time<=105):
    print("The award that the participant will receive is: Provincial Half Colours")

elif(106<=time<=110):
    print("The award that the participant will receive is: Provincial Scroll")

else:
    print("No award")
