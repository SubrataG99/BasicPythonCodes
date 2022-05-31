
# Take a string from user and encrypt it as per offset given by user
# Example :
# String = 'Abcd', Offset = 2 --> Final = 'Cdef 

s = str(input('\nEnter a text : '))
key = int(input('Enter a number for OFFSET : '))
fs = ''
if 0 <= key < 26 :
    for i in range(len(s)) :
        if s[i] != ' ' :
            if 'A' <= s[i] <= 'Z' :
                fs = fs + (chr((ord(s[i]) + key) % ord('Z')))
            elif '0' <= s[i] <= '9' :
                fs = fs + (chr((ord(s[i]) + key) % 57))
            else :
                fs = fs + (chr((ord(s[i]) + key) % ord('z')))
        else :
            fs = fs + s[i]
print('Encrypted string is :', fs)

# print(s[0])
# print(ord(s[0]))
# print(chr(ord(s[0]) +  key))

# s[0] = s[0] + 1
# print(s[0])
# print(str(s [0] + 1))