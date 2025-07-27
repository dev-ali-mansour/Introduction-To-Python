from collections import Counter

nyc_eatery_types = ['Mobile Food Truck', 'Restaurant', 'Food Cart', 'Snack Bar', 'Food Cart', 'Mobile Food Truck',
                    'Food Cart', 'Vegetable Cart', 'Speciality Cart', 'Restaurant', 'Vegetable Cart',
                    'Mobile Food Truck', 'Restaurant', 'Speciality Cart', 'Restaurant', 'Mobile Food Truck',
                    'Restaurant', 'Snack Bar', 'Vegetable Cart', 'Speciality Cart', 'Vegetable Cart', 'Restaurant',
                    'Mobile Food Truck', 'Vegetable Cart', 'Restaurant', 'Snack Bar', 'Speciality Cart', 'Restaurant',
                    'Mobile Food Truck', 'Restaurant', 'Vegetable Cart', 'Mobile Food Truck', 'Restaurant']
nyc_eatery_count_by_types = Counter(nyc_eatery_types)
print(nyc_eatery_count_by_types)
print(nyc_eatery_count_by_types['Restaurant'])
print(nyc_eatery_count_by_types.most_common(3))
