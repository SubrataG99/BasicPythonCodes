# Write a code to decipher a message written in old keypad phones to convert from set of numbers into readable string
'''
For example :
code = 4433555.555666
message = "hello"
'''

code = input("Enter the code in keypad format : ")
message = ''
c2m = [[' ', '_'], ['.', ',', '?'], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

codeLen = len(code)
i = 0
while (i < codeLen - 1) :
    if (code[i] == '.') :
        i = i + 1
    cint = int(code[i])
    cnt = 0
    if ((code[i] == code[i+1]) ) :
        j = i + 1
        while (j < codeLen) :
            if (code[i] == code[j]) :
                cnt = cnt + 1
                j = j + 1
            else :
                break
        i = i + cnt + 1
    else :
        i = i + 1
    message = message + c2m[cint][(cnt % len(c2m[cint]))]
    cnt = 0
if (cnt == 0) :
    message = message + c2m[int(code[-1])][0]
print("Message is :", message, '\n')