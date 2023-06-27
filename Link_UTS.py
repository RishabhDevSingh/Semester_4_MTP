import requests
import pandas as pd

def annotate_text(text, api_key):
    api_url = 'https://uts-ws.nlm.nih.gov/rest/cui/lookup'
    params = {
        'ticket': api_key,
        'string': text,
        'format': 'json'
    }

    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'result' in data and 'results' in data['result']:
            annotations = data['result']['results']
            results = []
            for annotation in annotations:
                results.append({
                    'CUI': annotation['ui'],
                    'Term': annotation['name'],
                    'Semantic Type': annotation['rootSource']
                })
            return results
    return None

# Input text for entity linking
text = "Famotidine-associated delirium. A series of six cases. Famotidine is a histamine H2-receptor antagonist"

# UMLS API key
api_key = 'b64797fc-574d-4d2a-af49-5efd5b53da16'  

# Perform UMLS entity linking
annotations = annotate_text(text, api_key)

# Create DataFrame from annotations
df_annotations = pd.DataFrame(annotations)

# Print the annotations
print(df_annotations)