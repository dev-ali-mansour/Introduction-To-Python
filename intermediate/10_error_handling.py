def average(values):
    try:
        # Code that might cause an error
        average_value = sum(values) / len(values)
        return average_value
    except:
        # Code to run if an error occurs
        print("average() accepts a list or set. Please provide a correct data type.")


sales_dict = {"cust_id": ["JL93", "MT12", "IY64"],
              "order_value": [43.21, 68.70, 82.19]}

average(sales_dict)


def average(values):
    # Check data type
    if type(values) in ["list", "set"]:
        # Run if the appropriate data type was used
        average_value = sum(values) / len(values)
        return average_value
    else:
        # Run if an Exception occurs
        raise TypeError("average() accepts a list or set. Please provide a correct data type.")


average(sales_dict)


def snake_case(text):
    # Check the data type
    if type(text) == str:
        clean_text = text.replace(" ", "_")
        clean_text = clean_text.lower()
        return clean_text
    else:
        # Return a TypeError error if the wrong data type was used
        raise TypeError(
            "The snake_case() function expects a string as an argument, please check the data type provided.")


print(snake_case("User Name 187"))
