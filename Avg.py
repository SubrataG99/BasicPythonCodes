
# Take 'n' spaced integer as input from user and find out their average

n = int(input('\nEnter the number of terms : '))
numarr = (list(map(int, input('Enter : ').split())))[:n]
s = 0
print(numarr)
for i in numarr:
    s = s + i
    avg = float(s/n)
print('Average is :', format(avg, '.4f'))                                           # Average is printed upto 4 places of decimal
print('Average rounded off to :', round(avg, 2))                            # Average is rounded upto 2 places in this case