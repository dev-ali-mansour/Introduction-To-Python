art_galleries = {
    '10021': {
        "The Metropolitan Museum of Art": '(212) 535-7710',
        'The Frick Collection': '(212) 288-0700',
        'The Museum of Modern Art': '(212) 708-9400',
    },
    '10013': {
        "New Museum of Contemporary Art": '(212) 219-1222',
        'The Drawing Center': '(212) 219-2166',
        'The Museum at the Fashion Institute of Technology': '(212) 217-4558',
    },
    '10001': {
        "The Museum at the Fashion Institute of Technology": '(212) 217-4558',
        'The Rubin Museum of Art': '(212) 620-5000',
        'The Museum of Arts and Design': '(212) 956-3535',
    },
    '10009': {
        "The Museum of the American Indian": '(212) 514-3700',
        'The Tenement Museum': '(212) 431-0233',
        'The Museum of Chinese in America': '(212) 619-4785',
    },
    '10011': {
        'The Rubin Museum of Art': '(212) 620-5000',
        'The Museum at the Fashion Institute of Technology': '(212) 217-4558',
        'The Drawing Center': '(212) 219-2166',
    },
    '10022': {
        "The Museum of Modern Art": '(212) 708-9400',
        'The Museum of Arts and Design': '(212) 956-3535',
        'The Frick Collection': '(212) 288-0700',
        'The Metropolitan Museum of Art': '(212) 535-7710',
    },
    '10027': {
        "Paige's Art Gallery": '(212) 513-1577',
        'Triple Candie': '(212) 243-2100',
        'Artifact Motherland Inc': '(212) 966-5550',
        'Inner City Art Gallery': '(212) 966-5550',
    },
    '10019': {
        'The Museum of the American Indian': '(212) 514-3700',
        'The Tenement Museum': '(212) 431-0233',
        'The Museum of Chinese in America': '(212) 619-4785',
        'The New Museum of Contemporary Art': '(212) 219-1222',
    },
    '11106': {
        'The Museum of Arts and Design': '(212) 956-3535',
        'The Rubin Museum of Art': '(212) 620-5000',
        'The Museum at the Fashion Institute of Technology': '(212) 217-4558',
    },
    '10128': {
        'The Metropolitan Museum of Art': '(212) 535-7710',
        'The Frick Collection': '(212) 288-0700',
        'The Museum of Modern Art': '(212) 708-9400',
        'The Museum of Arts and Design': '(212) 956-3535',
    }}

# Accessing the keys of the dictionary
print(art_galleries.keys())

# Accessing the values of the dictionary
print(art_galleries['10027'])

# Accessing nested data
print(art_galleries['10027']['Triple Candie'])
