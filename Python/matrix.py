# Python3 
# Matrix Product


# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list
test_list = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]

# printing original list
print("The original list : " + str(test_list))


# Matrix Product
res = prod([ele for sub in test_list for ele in sub])

print("The total element product in lists is : " + str(res))
