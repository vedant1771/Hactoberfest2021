# how to do google search using python script
# first intall beautifulsoup because it is one of the dependency of google search
# in terminal: pip install beautifulsoup4
# now install google package: pip install google
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = "Geeksforgeeks"

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	print(j)

  
