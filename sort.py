def bubble_sort(array):
	size = len(array)
	for i in range(size):
		for k in range(size-1):
			if(array[k] > array[k+1]):
				temp = array[k]
				array[k] = array[k+1]
				array[k+1] = temp
	return array
