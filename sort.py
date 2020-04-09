from math import floor

def bubble_sort(array):
	size = len(array)
	for i in range(size):
		for k in range(size-1):
			if(array[k] > array[k+1]):
				temp = array[k]
				array[k] = array[k+1]
				array[k+1] = temp
	return array

def merge_sort(array):
	size = len(array)
	if(size <= 1):
		return array
	if(size == 2):
		if(array[0] > array[1]):
			temp = array[0]
			array[0] = array[1]
			array[1] = temp
		return array
	
	mid = (size/2)

	return merge(merge_sort(array[0:mid]), merge_sort(array[mid:size]))

def merge(left_array, right_array):
	sorted_array = []
	left_array_index = 0
	right_array_index = 0

	for i in range(len(left_array) + len(right_array)):
		if(right_array_index >= len(right_array)):
			sorted_array.append(left_array[left_array_index])
			left_array_index += 1
			continue
		elif(left_array_index >= len(left_array)):
			sorted_array.append(right_array[right_array_index])
			right_array_index += 1
			continue
		if(left_array[left_array_index] <= right_array[right_array_index]):
			sorted_array.append(left_array[left_array_index])
			left_array_index += 1
		elif(left_array[left_array_index] > right_array[right_array_index]):
			sorted_array.append(right_array[right_array_index])
			right_array_index += 1
		
	
	return sorted_array
