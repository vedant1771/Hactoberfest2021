def narcissistic_number(number):
	return number == sum([int(x) ** len(str(number)) for x in str(number)])

for x in range(1,1000):
    if narcissistic_number(x)==1:
        print(x)
