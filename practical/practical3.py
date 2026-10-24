# Practical 3 :

# Accept number of rows
n = int(input("Enter number of rows: "))

# Pyramid
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Reverse pyramid
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))