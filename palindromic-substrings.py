def getPalindromicSubstrings(s):
	count = 0
	for i in range(len(s)):
		count += 1
		for k in range(i+1, len(s)):
			if(is_palindrom(s, i, k)):
				count += 1
	return count

def is_palindrom(s, start, end):
	while(start <= end):
		if(s[start] != s[end]):
			return False
		start += 1
		end -= 1
	return True