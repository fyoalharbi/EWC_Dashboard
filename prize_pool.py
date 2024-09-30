import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://127.0.0.1:5500/Esports%20World%20Cup%202024%20-%20Liquipedia%20Esports%20Wiki%20-%20main%20page.htm'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
prizepool_section = soup.find('div', class_='csstable-widget collapsed general-collapsible prizepooltable')

places = []
amounts = []
participants = []
headers = ['Place', "Prize", "Participant"]
for row in prizepool_section.find_all('div', class_='csstable-widget-row'):
    
    place_div = row.find('div', class_=['csstable-widget-cell prizepooltable-place'])
    place = place_div.find('div').text.strip() if place_div else None
    places.append(place)
    
    amount = row.find(lambda tag: tag.name == 'div' and tag.get('class') == ['csstable-widget-cell'])
    amount = amount.text.strip() if amount else None
    amounts.append(amount)
    
    participant = ', '.join([team.text.strip() for team in row.find_all('a')])
    participants.append(participant)
print(amounts)
df_prizepool = pd.DataFrame({
    'Place': places,
    'Prize': amounts,
    'Participants': participants
})

output_file = 'esports_prizepool_2024.xlsx'
df_prizepool.to_excel(output_file, index=False)

print(f"Data successfully saved to {output_file}")
