import numpy as np

A = np.array([1,2,3,4])

print(A+A)
print(A**2)
print(np.sqrt(A))
print(np.log(A))

dot = 0
c = np.array([3,3])
d = np.array([2,5])
for e,f in zip(c,d):
    dot += e*f
print(dot)
print(d*c)
print(np.sum(c*d))
print((c*d).sum())
print(np.dot(c,d))
print(c.dot(d))
print(d.dot(c))

#dot = (3*2)+(3*5)

amag = np.sqrt((c*c).sum())
print(amag)

amag = np.linalg.norm(c)
print(amag)

cosangle = c.dot(d)/(np.linalg.norm(c)* np.linalg.norm(d))
print(cosangle)

#amag = magnitude 

#actual angle = angle
angle = np.arccos(cosangle)
print(angle)

#matrix
M = np.array([[1,4],[5,6]])
print(M[0,0])
print(M[0][1])

L = [[1,4],[5,7]]
print(L[0])
print(M)

M2 = np.matrix([[1,2],[9,8]])
print(M2)

A2 = np.array(M2)

print(A2)

print(A2.T)

R = np.random.randn(8,9)
print(R)
print(R.mean())
print(R.var())
Z = np.zeros((9,9))
print(Z)

O = np.ones((2,5))
print(O)

#R2 = np.random.randint((6,6))
#print(R2)

#Inverse of a matrix
M2inv = np.linalg.inv(M2)
print(M2inv)
#Checking if the inverse is correct
print(M2.dot(M2inv))
print(M2inv.dot(M2))

#determinant of matrix
print(np.linalg.det(M2))

#diagonal elements
print(np.diag(M2))

print(np.diag([1,4]))

#Inner product and outer product of vectors
u = np.array([1,2])
v = np.array([3,4])

print(u.dot(v))
print(np.inner(u,v))
print(np.outer(u,v))

#Sum of diagonals

print(np.diag(M2).sum())
print(np.trace(M2))

print(np.array([[1,2],[5,6]]).sum())

print(M2+M)

#Solving in linear system

P = np.matrix([[1,2],[5,6]])
t = np.array([3,4])

x = np.linalg.inv(P).dot(t)
print(x)

x = np.linalg.solve(P,t)
print(x)

    