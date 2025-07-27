# Creating and looping through dictionaries
galleries = [('Tate Modern', 3056), ('MoMA', 1432), ('Guggenheim', 1546), ('Uffizi', 1765), ('Prado', 28014)]
art_galleries = {}
for name, zip_code in galleries:
    art_galleries[name] = zip_code

for name in sorted(art_galleries)[-5:]:
    print(name)

# Finding by key
# print(art_galleries['Louver']) # Uncommenting this line will raise a KeyError if 'Louver' is not in the dictionary

# Safely finding by key
print(art_galleries.get('Louver', 'Not Found'))
