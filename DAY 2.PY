# 1.Arthematic oprator
a = 10
b = 5

print(f"addition: {a} + {b} = {a + b}")
print(f"subtraction: {a} - {b} = {a - b}")
print(f"multiplication: {a} * {b} = {a * b}")
print(f"division: {a} / {b} = {a / b}")
print(f"floow division: {a} // {b} = {a // b}")
print(f"exponential: {a} ** {b} = {a ** b}")
print(f"modulus: {a} % {b} = {a % b}")

# 2.Assignment operators
x = 10
x += 5
print(f"x += 5 makes x : {x}")

#3.logical operators
c = 10
d = 5

print((c > d) and (c < d))
print((c > d) or (c < d))
print(not (c>d))

# 4.Bitwise operator
print(f"5 & 7 (bitwise AND) {5 & 7}")
print(f"5 | 7 (bitwise OR) {5 | 7}")

# 5.commparision operator
e = 10
f = 5
print(e == f)
print(e != f)
print(e <= f)
print(e >= f)
print(e << f)
print(e >> f)

# 6.identity operator
g = [1,2,3]
h = [1,2,3]
i = 3

print(g == h)
print(g is h)
print(g is not i)

# 7.Membership operator
fruits = ['apple', 'banana','cherry']
print('apple' in fruits)
print('grappes' not in fruits)


## 8. F-String  
name = "yathin"
age = 17
print(f"Hello {name.upper()}, you will be {age +1} next year!")