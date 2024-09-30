import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://127.0.0.1:5500/Esports%20World%20Cup%202024%20-%20Liquipedia%20Esports%20Wiki%20-%20main%20page.htm'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='wikitable plainrowheaders sortable')

country = []
first = []
second = []
third = []
total = []

for row in table.find('tbody').find_all('tr'):
    
    c = row.find('th').find('span')
    country.append(c.find('a')['title']) if c else None 
    f = row.find('td')
    first.append(f.find('b').text if f else None)
    cells = row.find_all('td')#.find('b')

    if len(cells) > 0:
        second.append(cells[1].text.strip())  
        third.append(cells[2].text.strip())  
        total.append(cells[3].text.strip())  
first = first[1:]
df_tournaments = pd.DataFrame({
    'country': country,
    'first': first,
    'second': second,
    'third': third,
    'total': total,
})

output_file = 'country_medals.xlsx'
df_tournaments.to_excel(output_file, index=False)

print(f"Data successfully saved to {output_file}")
