import functools

def add3(x=0, y=0, z=0):
	return x + y + z

add3_partial = functools.partial(add3, x=1, y=2, z=3)
print(add3_partial())