mileage=2500
max_mileage=3000
car_age=6
max_age=8
price=25000.00
max_price=30000.00
# Check the mileage
if mileage > max_mileage:
    print("Too many miles")

# Check the age of the car
elif car_age >= max_age:
    print("Car is too old")

# Check the price
elif price > max_price:
    print("Over budget")

# If all conditions met
else:
    print("This car is worth considering!")