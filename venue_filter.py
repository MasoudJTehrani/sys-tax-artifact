import json, os
import pandas as pd
# ### Apply venue filter

json_dir_path = './findpapers'

# %%
def parse(data):
    """Parse the JSON data and extract relevant information."""
    combs = []
    for entry in data['papers']:
        title = entry.get('title')
        abstract = entry.get('abstract')
        urls = entry.get('urls')
        publication_date = entry.get('publication_date')
        doi = entry.get('doi')
        authors = entry.get('authors')
        publication = entry.get('publication')
        year = int(entry.get('publication_date').split('-')[0])

        category = publication.get('category')
        publisher = publication.get('publisher')
        journal_name = publication.get('title')

        # filter 1
        if publication.get('is_potentially_predatory') == 'true':
            continue
        # filter 2
        if publisher is not None and \
            ('Multidisciplinary Digital Publishing Institute' in publisher or 'MDPI' in publisher):
            continue
        
        if urls is not None and len(urls) > 0:
            url = urls[0]
        else:
            url = ""
        comb = (title, publication_date, category, publisher, journal_name, abstract, url)
        combs.append(comb)
    return combs      

# %%
all_combs = []
for file_name in os.listdir(json_dir_path):
    if file_name.endswith('.json'):
        file_path = os.path.join(json_dir_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            combs = parse(data)
        
        # duplication check
        for comb in combs:
            title = comb[0]
            if title in [c[0] for c in all_combs]:
                continue
            all_combs.append(comb)

# The chosen_venues.txt is created manually based on the frequency of the venues 
# and the author's knowledge of relevant venues (also included in the white_list.txt).
venue_filters = []
with open('chosen_venues.txt', 'r') as f:
    for line in f:
        line = line.strip()
        venue_filters.append(line)

# Convert the filtered papers to a pandas DataFrame and save as a CSV file
filtered_combs = [
    {"title": comb[0], "abstract": comb[5], "URLs": comb[6], "venue": comb[4], "year": comb[1]}
    for comb in all_combs if comb[4] in venue_filters
]

df = pd.DataFrame(filtered_combs, columns=["title", "abstract", "URLs", "venue", "date"])
df.to_csv('papers_after_venue_filter.csv', index=False)
print("created papers_after_venue_filter.csv")
