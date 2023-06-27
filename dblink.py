import requests

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
        return response.json()
    else:
        return None

# Example usage
text = "In unanesthetized, spontaneously hypertensive rats the decrease in blood pressure and heart rate produced by intravenous clonidine, 5 to 20 micrograms/kg, was inhibited or reversed by nalozone, 0.2 to 2 mg/kg. The hypotensive effect of 100 mg/kg alpha-methyldopa was also partially reversed by naloxone. Naloxone alone did not affect either blood pressure or heart rate. In brain membranes from spontaneously hypertensive rats clonidine, 10(-8) to 10(-5) M, did not influence stereoselective binding of [3H]-naloxone (8 nM), and naloxone, 10(-8) to 10(-4) M, did not influence clonidine-suppressible binding of [3H]-dihydroergocryptine (1 nM). These findings indicate that in spontaneously hypertensive rats the effects of central alpha-adrenoceptor stimulation involve activation of opiate receptors. As naloxone and clonidine do not appear to interact with the same receptor site, the observed functional antagonism suggests the release of an endogenous opiate by clonidine or alpha-methyldopa and the possible role of the opiate in the central control of sympathetic tone."
annotations = annotate_text(text)
if annotations:
    for annotation in annotations['Resources']:
        print(annotation['@URI'])
else:
    print("An error occurred during annotation.")