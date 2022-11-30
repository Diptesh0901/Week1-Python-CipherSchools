# Looping Statements

a = 1
while a < 10:
    print(a)
    a += 1

print(iter("asdfaadf"))

name = "jatin"
print(type(name))
print("***")
# name._iter_


for c in name:
    print(c)
    print(type(c))

for i in range(5):
    print(i)

# Break Continue and Pass

print("aaaaaa" * 4)

for i in range(5):
    print(i)
    if i == 3:
        break

for i in [0, 1, 2, 3, 4]:
    print(i)
    i = 100
    print(i)

if True:
    print("Rest of the Code")

for i in range(5):
    print(i)
    if i == 3:
        break
else:
    print("something")
