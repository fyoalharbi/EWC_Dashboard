import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL of the webpage
url = 'http://127.0.0.1:5500/Esports%20World%20Cup%202024%20-%20Liquipedia%20Esports%20Wiki%20-%20main%20page.htm'

# Step 2: Fetch the content of the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# Step 3: Locate the prize pool table by its class
prizepool_section = soup.find('div', class_='csstable-widget collapsed general-collapsible prizepooltable')
# Step 4: Initialize lists to store the scraped data
#print(prizepool_section)

places = []
amounts = []
participants = []
headers = ['Place', "Prize", "Participant"]
# Step 5: Extract the rows containing the prize details
for row in prizepool_section.find_all('div', class_='csstable-widget-row'):
    # Extract place (1st, 2nd, etc.)
    
    place_div = row.find('div', class_=['csstable-widget-cell prizepooltable-place'])
    place = place_div.find('div').text.strip() if place_div else None
    places.append(place)
    
    # Extract prize amount
    amount = row.find(lambda tag: tag.name == 'div' and tag.get('class') == ['csstable-widget-cell'])
    amount = amount.text.strip() if amount else None
    amounts.append(amount)
    
    # Extract participant/team names (some may have multiple teams in one cell)
    participant = ', '.join([team.text.strip() for team in row.find_all('a')])
    participants.append(participant)
print(amounts)
# Step 6: Create a DataFrame to organize the data
df_prizepool = pd.DataFrame({
    'Place': places,
    'Prize': amounts,
    'Participants': participants
})

# Step 7: Save the DataFrame to an Excel or CSV file
output_file = 'esports_prizepool_2024.xlsx'
df_prizepool.to_excel(output_file, index=False)

print(f"Data successfully saved to {output_file}")
