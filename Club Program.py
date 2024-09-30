import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
# Step 1: Define the URL of the webpage
url = 'http://127.0.0.1:5500/Esports%20World%20Cup%202024%20-%20Liquipedia%20Esports%20Wiki%20-%20main%20page.htm'

# Step 2: Fetch the content of the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='sortable wikitable2')

# Step 4: Initialize lists to store the scraped data
Country = []
Headquarters = []
team = []
Owner = []
b42024 = []
in2024 = []
En2024 = [] 
# Step 5: Iterate over each row in the table and extract the data
for row in table.find('tbody').find_all('tr'):
    c = row.find('th').find('span')
    Country.append(c.find('a')['title']) if c else None 
    cells = row.find_all('td')
    Headquarters.append(row.find('th').text.strip())
    if len(cells) > 0:
        # Extract text from each cell and append to respective lists
        #team name
        t = cells[0].find('span')
        team.append(t.find('span', class_='team-template-text').find('a')['title']) if t else None  # Date
        
        Owner.append(cells[1].text.strip())  # Prize Pool

        a = cells[2].find_all('img')
        a = ', '.join(link['alt'] for link in a)
        b42024.append(a) if a else b42024.append('None')
        
        a = cells[3].find_all('img')
        a = ', '.join(link['alt'] for link in a)
        in2024.append(a) if a else in2024.append('None')
        
        a = cells[4].find_all('img')
        a = ', '.join(link['alt'] for link in a)
        En2024.append(a) if a else En2024.append('None')
Headquarters = Headquarters[2:]

# Step 6: Create a DataFrame to organize the data
df_tournaments = pd.DataFrame({
    'Country': Country,
    'Headquarters': Headquarters,
    'team': team,
    'Owner': Owner,
    'Active prior to 2024': b42024,
    'returned in 2024': in2024, 
    'entered in 2024': En2024
})

# Step 7: Save the DataFrame to an Excel or CSV file
output_file = 'club_organization_2024.xlsx'
df_tournaments.to_excel(output_file, index=False)

print(f"Data successfully saved to {output_file}")
