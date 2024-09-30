import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://127.0.0.1:5500/Esports%20World%20Cup%202024%20Player%20List%20-%20Liquipedia%20Esports%20Wiki.htm'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'sortable wikitable'})  # Adjust the class or ID to target the right table


headers = [header.text.strip() for header in table.find_all('th')]

country_rows = []
rows = []
for row in table.find_all('tr')[1:]:  
    if(row.find('img')['alt'].strip() ):
        columns = row.find('td').find('img')['alt'].strip()
        country_rows.append(columns)
        
    columns = row.find_all('td') 
    columns = [col.text.strip() for col in columns]
    rows.append(columns)

country_df = pd.DataFrame(country_rows, columns=['Country'])
df = pd.DataFrame(rows, columns=headers)
df_combined = pd.concat([country_df, df], axis=1)
print(df_combined)

output_file = 'esports_world_cup_2024_country_representation_games.xlsx'
df_combined.to_excel(output_file, index=False)

print(f"Table successfully saved to {output_file}")
