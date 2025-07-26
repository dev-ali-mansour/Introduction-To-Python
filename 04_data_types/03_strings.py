# Formatted strings
cookie_name = "Anzac"
cookie_price = "$1.99"
print(f"Each {cookie_name} cookie cost {cookie_price}.")

# Joining with a string
child_ages = ["3", "4", "7", "8"]
print(", ".join(child_ages))
print(f"The children are ages {', '.join(child_ages[0:3])}, and {child_ages[-1]}.")

# Matching parts of a string
boy_names = ["Mohamed", "Yousef", "Ahmed"]
print([name for name in boy_names if name.startswith('A')])

print("long" in "Life is a long lesson in humility.")
print("life" in "Life is a long lesson in humility.")
print("life" in "Life is along lesson in humility.".lower())
