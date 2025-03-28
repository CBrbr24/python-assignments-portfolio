import numpy as np

a = 0
b = 1
x = 0

#f = (np.exp(x))**(np.log(x))



while a < x < b:
    if (((np.exp(a))**(np.log(a))) < 0) and ((np.exp(b)**(np.log(b))) < 0):
        t = (a+b)/2
        x=+0.1

        if (np.exp(t))**(np.log(t)) < 0:
            a = t

        elif (np.exp(t))**(np.log(t))>0:
            b = t
    if ((b-a)<0.0000000001):
        print(a,b)
        break