books = {"Ahmed Ali": "Introduction To Python", "Sara Saad": "Fundamentals Of Artificial Intelligence",
         "Ali Mansour": "Fundamentals Of Machine Learning"}

# Check if "Sara Saad" is a key in books
if "Sara Saad" in books.keys():
    print(True)
else:
    print(False)

print("==================")

# Check if "Sara Saad" is not a key in books
if "Sara Saad" not in books.keys():
    print(True)
else:
    print(False)

print("==================")

# The and keyword
book_prices = {"IM92": 45.5, "FD09": 95.45, "ND15": 76.15, "HN13": 64.25}
if "FD09" in book_prices and min(book_prices.values()) > 60:
    print(True)
else:
    print(False)
