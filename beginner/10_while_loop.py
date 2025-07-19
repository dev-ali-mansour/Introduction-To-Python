# Total tickets available
tickets = 5

# Number of tickets sold
tickets_sold = 0

while tickets_sold < tickets:
    # Increment tickets sold
    tickets_sold += 1
    # Print remaining tickets
    print(tickets - tickets_sold)

print("==================")

tickets = 10
tickets_sold = 0
# Breaking a loop
while tickets_sold < tickets:
    print(tickets - tickets_sold)
    break

print("==================")

while tickets_sold < tickets:
    # Increment sold tickets
    tickets_sold += 1
    # Conditional statements inside loop
    if tickets - tickets_sold > 7:
        print("Plenty of tickets remaining")
    elif tickets - tickets_sold > 3:
        print("Some tickets remaining")
    else:
        print("Low number of tickets!")
