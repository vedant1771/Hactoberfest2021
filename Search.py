paragraph = 'A snake charmer is a person who moves the streets with different types of the banks of the river Yamuna. It is snakes in his basket. He goes from one place to another to show various types of snakes and their tricks. He carries a pipe with which he plays music and snakes dance to his tune. He usually wears a colourful dress. The job of a snake charmer is quite dangerous. Some snakes are quite poisonous and can even bite him. It is not an easy task to catch and train them for the shows.'


if (paragraph.find('colourful') != -1):
	result = paragraph.find('colourful')
	print ("Substring found at index:", result )
else:
	print ("The paragraph doesn't contains given substring")
