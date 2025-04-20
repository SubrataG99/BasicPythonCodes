import matplotlib.pyplot as plt
import random

c = []
f = []
k = []
for i in range(100) :
	c.append(random.randint(-80, 10000))
print(c)

for i in c :
	f.append((i * (9/5)) + 32)
	k.append(i + 273)
print(f)
print(k)


plt.plot(c, f, marker='o', label='F')
plt.plot(c, k, marker='*', label='K')
plt.xlabel('Celsius')
plt.ylabel('Farhenheit')
plt.title('Temperature graph!')
plt.legend()
plt.show()