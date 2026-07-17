import requests
from bs4 import BeautifulSoup
a=requests.get('https://quotes.toscrape.com')
b=a.text
s=BeautifulSoup(b,'html.parser')
y=s.find_all('span',class_='text')
z=s.find_all('small',class_='author')
y_list=[x.text for x in y]
z_list=[c.text for c in z]
for o,p in enumerate(y_list):
    print(f'{o+1}. {p}')
    
print('AUTHORS')
    
for u,i in enumerate(z_list):
    print(f'{u+1}. {i}')