#What is the Score?
score = int(input("What is your test score?"))

#Determine the grade 
if score >= 90:
    print('You got an A!')
elif score >= 80:
    print('You got a B!')
elif score >= 70:
    print('You got a C')
elif score >= 60:
    print('You got a d')
else:
    print('You got an F')