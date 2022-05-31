
# Take a string and print it characterwise such that it looks like someone is typing

import sys
from time import sleep

def typing(text, t=0.0555):
    for ch in text:
        sleep(t)
        sys.stdout.write(ch)
        sys.stdout.flush()

s = str(input('\nEnter a Word or Sentence : '))
for i in range(len(s)):
    for j in range(i, len(s)):
        typing(s[j])
    print(' ')