
# Take a String defining Roman numerals of any number and return the decimal equivalent of the number

def Roman2Decimal(n):
    tally = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    s = 0
    for i in range(len(n)-1):
        left = n[i]
        right = n[i+1]
        if tally[left] < tally[right] :
            s = s - tally[left]
        else :
            s = s + tally[left]
    s = s + tally[n[-1]]
    return s

word = str(input('\nEnter in Roman numerals : '))
r2d = Roman2Decimal(word.upper())
print('The Roman Numeral \"', word.upper(), '\" in decimal is :', r2d, '\n')