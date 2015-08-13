import numpy as np

a=np.array([1,1,2])
b=np.array([2,1,2])
print a,b
print (a==b).mean()

c=np.random.choice(3,size=100)
d=np.random.choice(3,size=100)
print c
print d

result = np.random.randint(0, 3, c.size)
while True:
	bad = (result == c) | (result == d)
   	if not bad.any():
   		print result
    result[bad] = np.random.randint(0, 3, bad.sum())

