# Import pandas
import pandas

# Import pandas using an alias
import pandas as pd

# Sales dictionary
sales = {"user_id": ["KM37", "PR19", "YU88"],
         "order_value": [197.75, 208.21, 134.99]}

# Convert to pandas DataFrame
sales_df = pd.DataFrame(sales)
print(sales_df)

# Reading in a CSV file in our current directory
sales_df = pd.read_csv("sales.csv")

# Checking the data type
print(type(sales_df))

# DataFrame method to preview the first five rows
print(sales_df.head())
