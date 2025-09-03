import numpy as np

ob1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
ob2 = np.array_split(ob1, 3)
print(ob2)

ob3 = np.array_split(ob1, 4)
print(ob3)

ob4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sp1, sp2, sp3 = np.array_split(ob4, 3)
print(sp1)
print(sp2)
print(sp3)

split1 = np.array_split(ob4, 3)
print(split1)


split2 = np.array_split(ob4, 3, axis=1)
print(split2)
print(split2[0])
print(split2[1])
print(split2[2])

# ----------------------------------------------------
# sorting

print(np.sort(ob1))
print(np.sort(ob4, axis=0))
print(np.sort(ob4, axis=1))

print(np.sort(ob1)[::-1])
print(np.sort(ob4, axis=0)[::-1])
print(np.sort(ob4, axis=1)[:, ::-1])




