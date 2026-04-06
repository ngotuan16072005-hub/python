_tuple = ('ab', 'b', 'e', 'c', 'd', 'e', 'ab')

new_tuple = tuple(x for x in _tuple if _tuple.count(x) == 1)

print(new_tuple)