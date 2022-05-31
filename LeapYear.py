
# Take a year and check if the year is a leap year or not; is it Century leap year or not

n = int(input('\nEnter the year : '))

if n%4==0:
    if n%400==0:
        print(n, 'is a century leap year\n')
    else:
        print(n, 'is a normal leap year\n')
else:
    print(n, 'is not a leap year\n')