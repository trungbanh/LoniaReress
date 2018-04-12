import numpy as np
def lr2 (X,Y,t0,t1):    
    tong1 =float()
    tong2 = float()
    for i in range (len(X)):
        tong1 = tong1 + (Y[i]-(t0+t1*X[i]))
        tong2= tong2 + ((Y[i]-(t0+t1*X[i]))*X[i])
    return tong1,tong2

X = np.array([1,2,4])
Y = np.array([2,3,6])
e = 0.2
t0 =0 
t1 =1

for i in range (2):
    h1 ,h2 = lr2(X,Y,t0,t1)
    t0 = t0+e*h1
    t1 = t1+e*h2


print(t0,t1)
for i in range(len(a)):
    print (t0+t1*a[i])
# print(t0,t1) => -1.9600000000000002 -4.960000000000002
# print (t0+t1*5) => -26.76

# ket qua se dung khi e<0,01

from sklearn.linear_model import LinearRegression
import numpy

X = numpy.array([23,29,49,64,74,87,96,97,109,119,149,145])
Y = numpy.array([1,2,3,4,4,5,6,6,7,8,9,9])

X=X.reshape(-1,1)
Y=Y.reshape(-1,1)


lm = LinearRegression(normalize=True)

lm.fit(X,Y)

print(lm.intercept_)
print(lm.coef_)

print(lm.predict([[156]])) #=> 9.75826542
print (lm.predict([[166]])) #=> 10.39724478

''' 
sai so voi thuc te ~0.3 
'''





