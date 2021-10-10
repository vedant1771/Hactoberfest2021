secret_no = 9
guess_count = 0
guess_limit = 3

print('You have three chances to guess a correct number')
while guess_count < guess_limit:
    guess = int(input('Guess a number: '))
    guess_count += 1
    if guess == secret_no:
        print('You Won')
        break
else:
    print('You Failed')
