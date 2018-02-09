import numpy as np

def batch_gen(dt, batch_size, shuffle=False):
	num_data = dt.shape[0]
	num_batch = num_data // batch_size
	num_left = num_data % batch_size
	if shuffle:
		idx = np.random.permutation(num_data)
	else:
		idx = np.arange(num_data)
	while True:
		for batch in range(num_batch):
			idx_start = batch * batch_size
			idx_end = idx_start + batch_size
			idx_batch = idx[idx_start:idx_end]
			yield dt[idx_batch]
		if num_left:
			idx_batch = idx[idx_end:]
			yield dt[idx_batch]


if __name__ == '__main__':
	dt_dmy = np.arange(14).reshape([-1,2])
	gen = batch_gen(dt_dmy, 2)
	for dt in gen:
		print(dt)