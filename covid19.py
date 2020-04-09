from gazpacho import get,Soup
from pprint import pprint

URL = 'http://www.covid19.gov.ao'

html=get(URL)
soup=Soup(html)

numbers=soup.find('span',{'class':'big-number'})
labels=soup.find('span',{'class':'f-size2'})


for i in range(len(numbers)):
    numbers[i]=numbers[i].text

for i in range(len(labels)):
    labels[i]=labels[i].text

for i in range(len(numbers)):
    print(labels[i],':',numbers[i])

