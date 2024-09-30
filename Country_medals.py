import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL of the webpage
url = 'http://127.0.0.1:5500/Esports%20World%20Cup%202024%20-%20Liquipedia%20Esports%20Wiki%20-%20main%20page.htm'

# Step 2: Fetch the content of the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='wikitable plainrowheaders sortable')

# Step 4: Initialize lists to store the scraped data
country = []
first = []
second = []
third = []
total = []

# Step 5: Iterate over each row in the table and extract the data
for row in table.find('tbody').find_all('tr'):
    
    c = row.find('th').find('span')
    country.append(c.find('a')['title']) if c else None 
    f = row.find('td')
    first.append(f.find('b').text if f else None)
    cells = row.find_all('td')#.find('b')

    if len(cells) > 0:
        # Extract text from each cell and append to respective lists
        second.append(cells[1].text.strip())  # Event
        third.append(cells[2].text.strip())  # Prize Pool
        total.append(cells[3].text.strip())  # Participants
first = first[1:]
# Step 6: Create a DataFrame to organize the data
df_tournaments = pd.DataFrame({
    'country': country,
    'first': first,
    'second': second,
    'third': third,
    'total': total,
})

# Step 7: Save the DataFrame to an Excel or CSV file
output_file = 'country_medals.xlsx'
df_tournaments.to_excel(output_file, index=False)

print(f"Data successfully saved to {output_file}")
