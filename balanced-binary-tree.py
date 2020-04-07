def isBalanced(root):
	return _isBalanced(root)["isBalanced"]

def _isBalanced(node):
	output = {
		"isBalanced": True, "height": 0
	}
	if(not node):
		return output
	
	left = _isBalanced(node.left)
	right = _isBalanced(node.right)

	output["isBalanced"] = left["isBalanced"] and right["isBalanced"] and abs(left["height"] - right["height"]) <= 1
	output["height"] = 1 + max(left["height"], right["height"])

	return output