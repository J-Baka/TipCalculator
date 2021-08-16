print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill?\n"))
print("$" + str(total_bill))

tip = int(input("What percentage would you like to tip? 10, 12, or 15?\n"))
print(tip)

people = int(input("How may people are splitting the bill?\n"))
print(people)

final_bill = (total_bill + (total_bill * (tip / 100))) / people

# Will round the result to 2 decimals
result = "{:.2f}".format(final_bill)

print(f"Each person should pay: ${result}")

