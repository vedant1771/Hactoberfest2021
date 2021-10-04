# Buy and Sell Stock I

def buyAndSellStock(stocks):
	max_value = 0
	minSoFar = stocks[0]
	n = len(stocks)
	for i in range(1, n):
		if minSoFar > stocks[i]:
			minSoFar = stocks[i]
		if stocks[i] - minSoFar > max_value:
			max_value = stocks - minSoFar
	return max_value
	
# Test 1:
arr = [7,1,5,3,6,4]
print(buyAndSellStock(arr)

# Test 2:
arr = [7,6,4,3,1]
print(buyAndSellStock(arr)
