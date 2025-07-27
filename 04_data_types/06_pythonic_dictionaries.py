art_galleries = {'Miakey Art Gallery': '(718) 686-0788', 'Morning Star Gallery Ltd': '(212) 334-9330',
                 'New York Art Expo Inc': '(212) 363-8280'}
for gallery, phonenum in art_galleries.items():
    print(gallery)
    print(phonenum)

# Checking dictionary for data
art_galleries = {'10010': {'Nyabinghi African Gift Shop': '(212) 566-3336'}}
print('11234' in art_galleries)
if '10010' in art_galleries:
    print('I found: %s' % art_galleries['10010'])
else:
    print('No galleries found.')

