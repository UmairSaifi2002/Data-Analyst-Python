import numpy as np

ob1 = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])
ob2 = np.array([[19, 18, 17], [16, 15, 14], [13, 12, 11]])

sp = np.split(ob1, 3)
print(sp)

sp1 = sp[0]
sp2 = sp[1]
sp3 = sp[2]

ob3 = np.concatenate((sp1, sp2, sp3), axis=0)
print(ob3)

ob4 = np.reshape(ob1, (3, 3))

join = np.concatenate((ob4, ob2), axis=0)
print(join)

join1 = np.concatenate((ob4, ob2), axis=1)
print(join1)







