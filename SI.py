
# Take p, r, t as input and calculate the SI (Simple Interest) as per formula and print the result upto 2 places of decimal

p = float(input('\nEnter the Principle : '))
r = float(input('Enter Rate : '))
t = float(input('Enter Time period : '))

si = (p*r*t)/100

print('For principle of', p, 'at a rate of', r, 'for a period of', t, 'years is -->')
print('Simple Interest : (', format(si, '.4f'), 'rounded off to)', round(si, 2))
print('Amount :(', format(si+p, '.4f'), 'rounded off to)', round((si+p), 2),  '\n')

#               Only 3 places of decimal --> format(output, '.3f)