from gazpacho import get,Soup
from pprint import pprint
import json
from datetime import datetime

#current date time object
dt=datetime.now().replace(microsecond=0)


# Datetim in ISO 8601
# datetime.datetime.now().replace(microsecond=0).isoformat()

URL = 'http://www.covid19.gov.ao'

html=get(URL)
soup=Soup(html)

numbers=soup.find('span',{'class':'big-number'})
labels=soup.find('span',{'class':'f-size2'})


for i in range(len(numbers)):
    numbers[i]=numbers[i].text
    labels[i]=labels[i].text

for i in range(len(numbers)):
    print(labels[i],':',numbers[i])

# data to JSON
json_data={}
for i in range(len(numbers)):
    json_data[labels[i]]=int(numbers[i])

print(json_data)

