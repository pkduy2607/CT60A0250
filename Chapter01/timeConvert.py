seconds = int(input("Enter total seconds:\n"))
minute = seconds // 60
remaining_second = seconds - minute * 60

print("Minutes: " + str(minute))
print("Remaining seconds: " + str(remaining_second))
