#Initial Condition:

row1=2

#Counter Controlled Iteration Loop
for i in range(1,10):
    if(1 <= i <= 5):
        star_patern = '*' * i
        print(star_patern)      
    else:
        star_patern2='*' * (i-row1)
        print(star_patern2)
        row1=row1+2

