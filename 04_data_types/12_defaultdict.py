from collections import defaultdict

# Dictionary Handling

nyc_eateries_parks = [
    ('M010', 'MOHAMMED MATIN'),
    ('M010', 'PRODUCTS CORP.'),
    ('M010', 'Leob Boathouse Resturant'),
    ('M010', 'Nandita Inc.'),
    ('M010', 'SALIM AHMED'),
    ('M010', 'THE NY PICNIC COMPANY'),
    ('M010', 'THE NEW YORK PICNIC COMPANY,INC.'),
    ('M010', 'NANDITA, INC.'),
    ('M010', 'JANANI FOOD SERVICE, INC.')
]
eateries_by_park = {}
for park_id, name in nyc_eateries_parks:
    if park_id not in eateries_by_park:
        eateries_by_park[park_id] = []
    eateries_by_park[park_id].append(name)
print(eateries_by_park['M010'])

# Using defaultdict for the same task
eateries_by_park = defaultdict(list)
for park_id, name in nyc_eateries_parks:
    eateries_by_park[park_id].append(name)
print(eateries_by_park['M010'])

nyc_eateries = [
    {'name': 'Mobile Food Truck', 'phone': '0123456789', 'website': 'www.site,com'},
    {'name': 'Restaurant', 'website': 'www.site,com'},
    {'name': 'Food Cart', 'phone': '0123456789', 'website': 'www.site,com'},
    {'name': 'Snack Bar', 'website': 'www.site,com'},
    {'name': 'Food Cart', 'phone': '0123456789'},
    {'name': 'Mobile Food Truck', 'phone': '0123456789', 'website': 'www.site,com'},
]
eatery_contact_types = defaultdict(int)
for eatery in nyc_eateries:
    if eatery.get('phone'):
        eatery_contact_types['phones'] += 1
    if eatery.get('website'):
        eatery_contact_types['websites'] += 1
print(eatery_contact_types)
