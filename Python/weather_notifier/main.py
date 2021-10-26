from bs4 import BeautifulSoup
import notify2
import requests

def fetch_weather():
	print("Enter City Whose Weather is Needed(First Alphabet in Capital)")
	city=input()
	url='https://www.weather-forecast.com/locations/'+city+'/forecasts/latest'
	page=requests.get(url)
	soup=BeautifulSoup(page.content,'html.parser')
	table=[]
	for x in soup.find('tr',class_='b-forecast__table-description b-forecast__hide-for-small days-summaries'):
		table.append(x.text)
	l=[]
	t=table[1]
	s=""
	n=len(t)
	i=0
	while i<n:
		if t[i]==')':
			break
		i+=1
	i+=1	
	while i<n:
		if t[i]!='.':
			s=s+t[i]
		else:
			l.append(s)
			s=""
		i+=1
	l.append(city)
	return l

def notify():
	r=fetch_weather()
	result=""
	l=len(r)
	i=0
	while i<l-1:
		result+=r[i]
		result+='. '
		i+=1
	city=r[l-1]
	icon_path="/home/aakarsh/Desktop/Desktop Notification/download.jpeg"
	notify2.init("City Weather Today(1-3 days)")
	n=notify2.Notification("Weather Notifier")
	n.set_urgency(notify2.URGENCY_NORMAL)
	n.set_timeout(1000)
	n.update("Current Weather Of "+city,result,icon=icon_path)
	n.show()
if __name__=="__main__":
	notify()
