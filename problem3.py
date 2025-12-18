a = int(input("Enter a number: "))

if a % 2 == 0:
    limit = a - 1
else:
    limit = a

for i in range(1, limit + 1, 2):
    print(i, end=" ")
