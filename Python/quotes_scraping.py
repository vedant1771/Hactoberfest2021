# Python program to scrape quotes from website and save it in a csv file.

# import required libraries
import requests
from bs4 import BeautifulSoup
import csv
    
# we will store the url of the website that we want to scrape in a variable 'url'.
url = "http://www.values.com/inspirational-quotes"

# Sending a HTTP request to the url and save the response in object 'r'.
r = requests.get(url)

# creating 'soup' object and passing two argument.
soup = BeautifulSoup(r.content, 'html5lib')

# creating a list to store quotes
quotes=[]  

# searching and extracting some desired data from the HTML content.
table = soup.find('div', attrs = {'id':'all_quotes'}) 
   
for row in table.findAll('div',
                         attrs = {'class':'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['lines'] = row.img['alt'].split(" #")[0]
    quotes.append(quote)

# saving all our data in some CSV file.
filename = 'quotes1.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['lines'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)