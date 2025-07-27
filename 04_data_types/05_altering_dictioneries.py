art_galleries = {'10310': {'New Dorp Village Antiques Ltd': '(718) 815-2526'}, '11234': {}}
galleries_10007 = {'Nyabinghi African Gift Shop': '(212) 566-3336'}
print(galleries_10007)
art_galleries['10007'] = galleries_10007

# Update the dictionary
galleries_11234 = [
    ('A J ARTS LTD', '(718) 763-5473'),
    ('Doug Meyer Fine Art', '(718) 375-8006'),
    ('Portrait Gallery', '(718) 377-8762')]
art_galleries['11234'].update(galleries_11234)
print(art_galleries['11234'])

# Remove data from the dictionary
del art_galleries['11234']
galleries_10310 = art_galleries.pop('10310')
print(galleries_10310)
