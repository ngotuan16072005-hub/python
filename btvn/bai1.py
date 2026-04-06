_tuple = ('a', 'b', 'd', 'e')

new_tuple = _tuple[:2] + ('c',) + _tuple[2:]

print(new_tuple)