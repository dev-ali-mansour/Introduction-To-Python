cookies = ["chocolate chip", "peanut butter", "sugar"]
cookies.append("Triggel")
print(cookies)
print(cookies[2])

# Combining lists
cakes = ["strawberry", "vanilla"]
deserts = cookies + cakes
print(deserts)

cookies.extend(cakes)
print(cookies)

# Finding an element in the list
position = cookies.index('sugar')
print(position)

# Removing an element from the list
name = cookies.pop(position)
print(name)
print(cookies)

# Iterating over a list
titlecase_cookies = [cookie.title() for cookie in cookies]
print(titlecase_cookies)

# Sorting a list
print(cookies)
sorted_cookies = sorted(cookies)
print(sorted_cookies)
