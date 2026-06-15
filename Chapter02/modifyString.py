s = input("Enter a string:\n")
n = int(input("Enter an integer:\n"))

result = s[: n - 1] + '@' + s[n:]
print(f"The new string is: {result}")
