def compute_permutations(nums):
    visited_list = nums[:]
    for i in range(len(nums)):
			visited_list[i] = False
    return _compute_permutations(nums, None, visited_list, [], [])

def _compute_permutations(list, num, visited_list, permutations, permutation):
	if num is not None:
		permutation.append(num)

	if(len(permutation) == len(list)):
		permutations.append(permutation)
		return permutations

	for i in range(len(visited_list)):
		if(visited_list[i] == False):
			new_visited_list = visited_list[:]
			new_visited_list[i] = True
			_compute_permutations(list, list[i], new_visited_list, permutations, permutation[:])
					
	return permutations