import requests
import pandas as pd
import json

def annotate_text(text):
    api_url = 'https://api.dbpedia-spotlight.org/en/annotate'
    params = {
        'text': text,
        'confidence': '0.5',
        'support': '10'
    }
    headers = {
        'Accept': 'application/json'
    }

    response = requests.get(api_url, params=params, headers=headers)
    if response.status_code == 200:
        annotations = response.json()['Resources']
        results = []
        for annotation in annotations:
            results.append({
                'Surface Form': annotation['@surfaceForm'],
                'URI': annotation['@URI']
            })
        return results
    else:
        return None

# Read input text from the JSON file
with open('filtered_data.json', 'r') as json_file:
    data = json.load(json_file)

# Perform DBpedia Spotlight annotation for each document
all_annotations = []
for value in data.values():
    document_text = value
    annotations = annotate_text(document_text)
    if annotations:
        all_annotations.extend(annotations)

# Create DataFrame from annotations
df_annotations = pd.DataFrame(all_annotations)

# Export annotations to Excel
df_annotations.to_excel('annotations.xlsx', index=False)
print("Annotations exported to annotations.xlsx")