# Zipping tuples
us_cookies = ['Chocolate Chip', 'Brownies ', 'Penut Butter', 'Oreos', 'Oatmeal Raisin']
in_cookies = ['Punjabi', 'Fruit Cake Rusk', 'Marble Cookies', 'Kaju Pista Cookies', 'Almond Cookies']
top_pairs = list(zip(us_cookies, in_cookies))
print(top_pairs)

# Unpacking tuples
us_name_1, in_name_1 = top_pairs[0]
print(us_name_1)
print(in_name_1)

# Unpacking with a for loop
for us_cookie, in_cookie in top_pairs:
    print(in_cookie)
    print(us_cookie)

# Enumerating positions
for idx, item in enumerate(top_pairs):
    us_cookie,in_cookie=item
    print(idx,us_cookie,in_cookie)

# Beware of tailing commas!
item2='butter',
print(item2)