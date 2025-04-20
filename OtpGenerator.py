'''
Write a program to generate an OTP based on the number of digits you want
'''

import random

def otp(n) :
	s = ''
	for i in range(n) :
		s = s + str(random.randint(0, 9))
		# print(s)
	return(s)

print('Your otp is :', otp(5))