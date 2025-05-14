# %%
import os
import collections
import pandas as pd

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

        comb = (title, year, journal_name, document_type)
        combs.append(comb)
    return combs        


all_combs = []
before_filter = 0
for file_name in os.listdir(json_dir_path):
    if file_name.endswith('.csv'):
        file_path = os.path.join(json_dir_path, file_name)
        data = pd.read_csv(file_path, encoding='utf-8')
        combs = parse(data)
        before_filter += len(data)

        # duplication check
        for comb in combs:
            title = comb[0]
            if title in [c[0] for c in all_combs]:
                print('duplicate title: {}'.format(title))
                continue
            all_combs.append(comb)

# %%
print("--"*30)
print(len(all_combs), 'Papers remain after first filters out of: ', before_filter )
print("--"*30)
# Frequency for journal venues

journal_venues = [c[2] for c in all_combs if c[3] == 'Article']
counter = collections.Counter(journal_venues)

with open('frequency/journal_venues.tsv', 'w') as f:
    for k, v in counter.most_common():
        f.write(f'{k}\t{v}\n')

print("\nJournal venues and frequencies are saved in frequency/journal_venues.tsv")

# Frequency for conference venues
conf_venues = [c[2] for c in all_combs if c[3] == 'Conference paper']
counter = collections.Counter(conf_venues)

with open('frequency/conf_venues.tsv', 'w') as f:
    for k, v in counter.most_common():
        f.write(f'{k}\t{v}\n')

print("\nConference venues and frequencies are saved in frequency/conf_venues.tsv")

