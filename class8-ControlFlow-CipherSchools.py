n = 5

for i in range(n):
    for j in range(n):
        print(i, end = " ")
    print("\n")

for i in range(n):
    for j in range(n):
        print(n-j,end = " ")
    print()

for i in range(n):
    for j in range(n):
        print(j+1, end = " ")
    print()

for i in range(n):
    for j in range(n):
        print(i+1, end = " ")
    print()

n = 9

for i in range(n):
    for j in range(n):
        print(max(i+1, j+1, n-i, n-j), end = " ")
    print()

n = 5
for i in range(n):
    for j in range(n):
        print((i,j), end = " ")
    print()

print(max(1, 2, 3, 4, 5, 6, 7))

n = 5
for i in range(n):
    for j in range(n):
        print(max(i, j), end = " ")
    print()

for i in range(n):
    for j in range(n):
        print(n-i-1, end = " ")
    print()

for i in range(n):
    for j in range(n):
        print(n-j-1, end = " ")
    print()

for i in range(n):
    for j in range(n):
        print(max(max(i+1, j+1), max(n-j,n-i)), end = " ")
    print()

print(sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 9]))



