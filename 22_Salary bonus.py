# Calculate the bonus of an employee and display the salary after bonus.

sal=int(input('enter your salary'))
gen=input('enter your gender')

if gen=='male':
    bonus=0.05*sal

else:
    bonus=0.10*sal

if sal<=20000:
    bonus=bonus+0.03*sal

sal=sal+bonus

print('sal is',sal)