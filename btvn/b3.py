_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

new_tuple = ()
for x in _tuple:
    if x not in new_tuple:
        new_tuple += (x,)

print(new_tuple)