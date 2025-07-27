import math

out_of_cookies = True
if out_of_cookies:
    print("Run to the store NOW!")

apples = 2
if apples:
    print("We have apples.")

apples = 0
if apples:
    print("We have apples.")

# Truthy           Falsey
#  1                0
#  "Cookies"        ""
#  ["Cake","Pie"]   []
#  {"key":"value"}  {}
#                   None

x = 0.1 + 1.1
print(x == 1.2)
print(x)

