ax = 110
print(ax)

def fn_outer():
	ax = 911
	def fn_inner():
		global ax
		# nonlocal ax
		print(ax)	# global@110 nonlocal@911
	fn_inner()
	print(ax)

fn_outer()
print(ax)

# 110
# 110	# 911
# 911
# 110