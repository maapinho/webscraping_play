from gazpacho import get,Soup
from pprint import pprint
import json
from datetime import datetime

#current date time object
dt=datetime.now().replace(microsecond=0)
print(dt)
print(dt.isoformat())

# Datetim in ISO 8601
# datetime.datetime.now().replace(microsecond=0).isoformat()

URL='http://www.kinguilahoje.com/'

html=get(URL)
soup=Soup(html)

quotations=soup.find('span',{'class':'quotation'})

dolar=quotations[0].text
euro=quotations[1].text

#pprint(quotations)
print('dolar:',dolar)
print('euro:',euro)

dolar_integer=int(dolar.split()[1])
euro_integer=int(euro.split()[1])

# data to JSON
json_data={'Dolar':dolar_integer,'Euro':euro_integer}

#print(json_data)

#output JSON data as a string
print(json.dumps(json_data))
