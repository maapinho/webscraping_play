from gazpacho import get,Soup
from pprint import pprint

URL='http://www.kinguilahoje.com/'

html=get(URL)
soup=Soup(html)

quotations=soup.find('span',{'class':'quotation'})

dolar=quotations[0].text
euro=quotations[1].text

#pprint(quotations)
print('dolar:',dolar)
print('euro:',euro)
