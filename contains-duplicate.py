def containsDuplicate(nums, k):
	indices = {}
	for i in range(len(nums)):
		num = nums[i]
		if(indices.get(num) == None):
			indices[num] = i
		else:
			if(abs(indices.get(num) - i) <= k):
				return True
			else:
				indices[num] = i

	return False