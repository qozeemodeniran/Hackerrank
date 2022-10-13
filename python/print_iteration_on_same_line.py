# n = int(input("Enter a positive integer: "))
# for i in range(1, n+1):
#     print(i, end="")

print(*range(1, int(input("Enter a positive integer: ")) +1), sep='')