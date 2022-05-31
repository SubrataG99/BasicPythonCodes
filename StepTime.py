
# Take a range and print how much millisecond it takes to complete the loop for that range
# {minimum print statement to be given else 0.0 ms comes}

import time

n = int(input('\nEnter a  range : '))
init = time.time()
for i in range(n):
    print(' ', end='')
print('\nYour defined', n, 'steps took', (time.time()-init), 'milliseconds\n')