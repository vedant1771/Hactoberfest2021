message = input("> ")

words = message.split(' ')
# print(words)

emojis = {
    ":)": "😀",
    ":(": "😞",
    ":/": "😑",
    ";)": "😉",
    "lol" : "😂",
   "sick":"😨",
   "happy": "😀",
   "mermaid": "🧜‍"
}
output = ""

for word in words:
    output += emojis.get(word, word)

print(output)
