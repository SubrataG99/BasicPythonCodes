
# Take a temperature in a degree and convert it to any other degree

print('\n1: Farhenheit to Celsius')
print('2: Celsius to Fahrenheit')
print('3: Celsius to Kelvin')
print('4: Kelvin to Celsius')
print('5: Fahrenheit to Kelvin')
print('6: Kelvin to Fahrenheit')
choice = int(input('What you want to perform : '))

if choice==1:
    f = float(input('Enter temperature in Fahrenheit : '))
    f2c = (f-32)*(5/9)
    print(f, 'degree fahrenheit =', f2c, 'degree Celsius\n')
elif choice==2:
    c = float(input('Enter temperature in Celsius : '))
    c2f = (c * (9/5)) + 32
    print(c, 'degree celsius =', c2f, 'degree fahrenheit\n')
elif choice==3:
    c = float(input('Enter temperature in Celsius : '))
    c2k = c + 273
    print(c, 'degree Celsius =', c2k, 'Kelvin\n')
elif choice==4:
    k = float(input('Enter temperature in Kelvin : '))
    k2c = k - 273
    print(k, 'Kelvin =', k2c, 'degree Celsius\n')
    if k2c==0:
        print('Almost impossible to achieve')
elif choice==5:
    f = float(input('Enter temperature in Farhenheit : '))
    f2k = ((f-32)*(5/9)) + 273
    print(f, 'degree Fahrenheit =', f2k, 'Kelvin\n')
elif choice==6:
    k = float(input('Enter temperature in Kelvin : '))
    k2f = ((k-273) * (9/5)) + 32
    print(k, 'Kelvin =', k2f, 'degree Fahrenheit\n')
else:
    print('INVALID CHOICE (Check again)')