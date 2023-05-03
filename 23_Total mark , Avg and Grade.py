# Calculate the total mark , Avg. mark and grade of a student.

Phy=int(input('enter the Phy mark'))
Chem=int(input('enter the Chem mark'))
Bio=int(input('enter the Bio mark'))
Math=int(input('enter the Math mark'))
IT=int(input('enter the IT mark'))
Eng=int(input('enter the Eng mark'))

Totalmark=Phy+Chem+Bio+Math+IT+Eng
print('Totalmark is ',Totalmark)

Avg=Totalmark/6
print('Avg is ',Avg)

if Avg>=90:
    print('O Grade')

elif Avg>=80 and Avg<=89:
    print('E Grade')

elif Avg>=70 and Avg<=79:
    print('A Grade')

elif Avg>=60 and Avg<=69:
    print('B Grade')

elif Avg>=50 and Avg<=59:
    print('C Grade')

elif Avg>=40 and Avg<=49:
    print('D Grade')

else:
    print('Fail! Better luck next time')