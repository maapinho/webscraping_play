from gazpacho import get,Soup
from pprint import pprint

html=get('http://www.kinguilahoje.com/')
soup=Soup(html)

quotations=soup.find('span',{'class':'quotation'})

dolar=quotations[0].text
euro=quotations[1].text

#pprint(quotations)
print('dolar:',dolar)
print('euro:',euro)
