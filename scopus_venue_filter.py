import json, os
import pandas as pd
# ### Apply venue filter

json_dir_path = './scopus'

# %%
def parse(data):
    """Parse the CSV data and extract relevant information."""
    combs = []
    for _, entry in data.iterrows():
        document_type = entry['Document Type']
        # only keep published conference or journal papers
        if document_type not in ['Article', 'Conference paper'] or entry['Publication Stage'] != 'Final':
            continue
        title = entry['Title']
        journal_name = entry['Source title']
        year = entry['Year']
        abstract = entry['Abstract']
        link = entry['Link']

        comb = (title, abstract, link, journal_name, year)
        combs.append(comb)
    return combs        
    

all_combs = []
for file_name in os.listdir(json_dir_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(json_dir_path, file_name)
        data = pd.read_csv(file_path, encoding='utf-8')
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
    {"title": comb[0], "abstract": comb[1], "link": comb[2], "venue": comb[3], "year": comb[4]}
    for comb in all_combs if comb[3] in venue_filters
]

df = pd.DataFrame(filtered_combs, columns=["title", "abstract", "link", "venue", "year"])
df.to_csv('papers_after_venue_filter.csv', index=False)
print("created papers_after_venue_filter.csv")
