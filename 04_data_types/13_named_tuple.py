from collections import namedtuple

nyc_eateries = [
    {'name': "Joe's Hot Dogs", 'location': 'Central Park - 5th Ave', 'park_id': 'M010', 'type_name': 'Cart'},
    {'name': 'City Bites', 'location': 'Prospect Park West', 'park_id': 'B005', 'type_name': 'Kiosk'},
    {'name': 'Green Garden Café', 'location': 'Battery Park', 'park_id': 'M022', 'type_name': 'Restaurant'},
    {'name': 'Sunset Snacks', 'location': 'Sunset Park', 'park_id': 'B010', 'type_name': 'Truck'},
    {'name': 'River View Grill', 'location': 'Riverside Park', 'park_id': 'M017', 'type_name': 'Restaurant'}
]

Eatery = namedtuple('Eatery', ['name', 'location', 'park_id', 'type_name'])
eateries = []
for eatery in nyc_eateries:
    details = Eatery(
        eatery['name'],
        eatery['location'],
        eatery['park_id'],
        eatery['type_name'])
    eateries.append(details)
print(eateries[0])

# Leveraging namedtuples for better readability
for eatery in eateries[:3]:
    print(eatery.name)
    print(eatery.park_id)
    print(eatery.location,"\n")
