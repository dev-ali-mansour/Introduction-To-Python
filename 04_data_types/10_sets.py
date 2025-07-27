# Set: Unique, Unordered, Mutable

# Creating a set
cookies_eaten_today = ['chocolate chip', 'peanut butter', 'chocolate chip', 'oatmeal cream', 'chocolate chip']
types_of_cookies_eaten = set(cookies_eaten_today)
print(types_of_cookies_eaten)

# Modifying a set
# Adding new items to the set
types_of_cookies_eaten.add('biscotti')
types_of_cookies_eaten.add('chocolate chip')
print(types_of_cookies_eaten)

# Updating sets
cookies_hugo_ate = ['chocolate chip', 'anzac']
types_of_cookies_eaten.update(cookies_hugo_ate)
print(types_of_cookies_eaten)

# Removing items from a set
types_of_cookies_eaten.discard('biscotti') # Safely remove an element from the set by value
print(types_of_cookies_eaten)
print(types_of_cookies_eaten.pop())
print(types_of_cookies_eaten.pop())

cookies_jason_ate=set(['chocolate chip', 'oatmeal cream','Penut butter'])
cookies_hugo_ate=set(['chocolate chip', 'anzac'])
print(cookies_jason_ate.union(cookies_hugo_ate))
print(cookies_jason_ate.intersection(cookies_hugo_ate))
print(cookies_jason_ate.difference(cookies_hugo_ate))
