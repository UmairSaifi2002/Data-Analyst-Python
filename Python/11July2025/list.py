l = [1,2,3,4,5,6,7,8,9,10]
print(l)
print(type(l))
l1 = list([1,2,3,4,5,6,7,8])
print(l1)
print(type(l1))

# slicing in list
print(l[0])  # First element
print(l[1])  # Second element
print(l[3])  # Fourth element
print(l[-2]) # Second last element
print(l[2:8])  # From index 2 to 8
print(l[::-1])   # Reverse the list
print(l[-5:-8:-1])  # Sublist using negative index

# list method
l.append(23)  # Append 11 to the list
print(l)
l.insert(0, 10)  # Insert 0 at the beginning
print(l)
l.remove(10)  # Remove the first occurrence of 10
print(l)
ll = ['a', 'b', 'c', 'd', 'e']
ll.append(l)  
print(ll)  # List of lists
ll.extend(l)
print(ll)  # Extended list with elements of l


# some imp concept
a = ['a', 'b', 'c', 'd', 'e']
b = a
print(a)
# ['a', 'b', 'c', 'd', 'e']
print(b)
# ['a', 'b', 'c', 'd', 'e']
b[2] = 4
print(b)
# ['a', 'b', 4, 'd', 'e']
print(a) 
# ['a', 'b', 4, 'd', 'e']

# a and b are pointing to the same list object
# To create a copy of the list, use the copy() method or slicing

c = ['u','m','a','i','r']  # Create a shallow copy of a
d = c.copy()  # Alternatively, you can use slicing: c = a[:]
print(c)
# ['a', 'b', 4, 'd', 'e']
print(d)
# ['u', 'm', 'a', 'i', 'r']
d.append('s')
print(d)

