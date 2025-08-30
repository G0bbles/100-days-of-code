print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = (int(input("What percentage tip would you like to give? 10, 12, or 15? ")) / 100) + 1
people = int(input("How many people would you like to split the bill with? "))
print(f"Each person should pay {(bill * tip_percent)/people:.2f}")
