import requests
import json

# Step 1: Define the API URL for Liquipedia Esports
api_url = 'https://liquipedia.net/esports/api.php'

# Step 2: Set up the parameters for the query
params = {
    'action': 'query', 
    'format': 'json',  
    'titles': 'Esports_World_Cup/2024',  # Page title to query
    'prop': 'revisions',
    'rvprop': 'content',
    'rvlimit': 'max'  # Get the maximum number of revisions allowed
}

# Step 3: Prepare to store the full content and handle continuation
full_content = ""
continue_token = {}  # Used to store continuation token

# Step 4: Loop to handle multiple requests for paginated content
while True:
    if continue_token:
        params.update(continue_token)  # Add continuation token if available

    # Make the API request
    response = requests.get(api_url, params=params)
    data = response.json()

    # Extract the page content from the response
    pages = data['query']['pages']
    page_id = next(iter(pages))  # Get the first page ID
    revisions = pages[page_id].get('revisions', [])

    # Concatenate the content from each revision
    for revision in revisions:
        full_content += revision['*']

    # Check if a continuation token exists
    if 'continue' in data:
        continue_token = data['continue']  # Update the token for the next request
    else:
        break  # No more pages to request

# Step 5: Save the entire response (full content) to a JSON file
output_data = {
    "title": pages[page_id]['title'],  # Include the page title
    "content": full_content             # Full wikitext content of the page
}

# Step 6: Write the output data to a JSON file
output_file = 'esports_world_cup_2024_full.json'
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(output_data, file, ensure_ascii=False, indent=4)

print(f"Full page content saved to {output_file}")
import pandas as pd
import json

# Step 1: Load the JSON data from the file
input_file = 'esports_world_cup_2024_full.json'
with open(input_file, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Step 2: Prepare the data for Excel
# We can store the title and content in separate columns
data = {
    'Title': [json_data['title']],
    'Content': [json_data['content']]
}

# Step 3: Convert the data to a pandas DataFrame
df = pd.DataFrame(data)

# Step 4: Save the DataFrame to an Excel file
output_file = 'esports_world_cup_2024_full.xlsx'
df.to_excel(output_file, index=False)

print(f"Data successfully saved to {output_file}")