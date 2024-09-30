import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL of the webpage
url = 'http://127.0.0.1:5500/Esports%20World%20Cup%202024%20-%20Liquipedia%20Esports%20Wiki%20-%20main%20page.htm'

# Step 2: Fetch the content of the webpage
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', class_='sortable wikitable1')

# Step 4: Initialize lists to store the scraped data
country = []
first = []
second = []
third = []
total = []

# Step 5: Iterate over each row in the table and extract the data
for row in table.find('tbody').find_all('tr'):
    c = row.find('th')
    #country.append(c.find('a')['title']) if c else None 
    """
    cells = row.find_all('td')
    if len(cells) > 0:
        # Extract text from each cell and append to respective lists
        games.append(cells[0].text.strip())  # Game
        dates.append(cells[1].text.strip())  # Date
        events.append(cells[2].text.strip())  # Event
        prizepools.append(cells[3].text.strip())  # Prize Pool
        participants.append(cells[4].text.strip())  # Participants
        winners.append(cells[6].find('img')['alt'])
        Runner_up.append(cells[7].find('img')['alt'])
"""
print(c)

"""
# Step 6: Create a DataFrame to organize the data
df_tournaments = pd.DataFrame({
    'Game': games,
    'Date': dates,
    'Event': events,
    'Prize Pool': prizepools,
    'Participants': participants,
    'winners': winners, 
    'Runner-up': Runner_up
})

# Step 7: Save the DataFrame to an Excel or CSV file
output_file = 'esports_tournaments_2024.xlsx'
df_tournaments.to_excel(output_file, index=False)

print(f"Data successfully saved to {output_file}")
"""