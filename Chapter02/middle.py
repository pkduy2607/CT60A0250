a = input("Enter the first string: ")
b = input("Enter the second string: ")

position = len(a) // 2
result = a[:position] + b + a[position:]

print(result)
