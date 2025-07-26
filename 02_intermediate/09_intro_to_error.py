# TypeError
# "Hello" + 5

# ValueError
# float("Hello")

# Import pandas package
import pandas as pd

# Create Pandas DataFrame
products = pd.DataFrame({"Id":["ABC1"],
                         "price":[29.99]})

# Try to access the non-existent "tag" column
print(products["tag"])

