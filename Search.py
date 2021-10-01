word = 'Hello World'

result = word.find('hello')
print ("Substring 'hello' found at index:", result )

result = word.find('World')
print ("Substring 'World' found at index:", result )

if (word.find('welcome') != -1):
	print ("Contains given substring ")
else:
	print ("Doesn't contains given substring")
