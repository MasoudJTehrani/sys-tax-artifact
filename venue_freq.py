# %%
import json, os
import collections

json_dir_path = './findpapers'

# %%
def parse(data):
    """Parse the JSON data and extract relevant information."""
    combs = []
    for entry in data['papers']:
        title = entry.get('title')
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

        comb = (title, year, category, publisher, journal_name)
        combs.append(comb)
    return combs        


all_combs = []
before_filter = 0
for file_name in os.listdir(json_dir_path):
    if file_name.endswith('.json'):
        file_path = os.path.join(json_dir_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            combs = parse(data)
            before_filter += len(data['papers'])
        
        # duplication check
        for comb in combs:
            title = comb[0]
            if title in [c[0] for c in all_combs]:
                print('duplicate title: {}'.format(title))
                continue
            all_combs.append(comb)

# %%
print("--"*20)
print(len(all_combs), ' Papers remain after first filters out of: ', before_filter )
print("--"*20)
# Frequency for journal venues

journal_venues = [c[4] for c in all_combs if c[2] == 'Journal']
counter = collections.Counter(journal_venues)

with open('frequency/journal_venues.tsv', 'w') as f:
    for k, v in counter.most_common():
        f.write(f'{k}\t{v}\n')

print("\nJournal venues and frequencies are saved in frequency/journal_venues.tsv")

# Frequency for conference venues
conf_venues = [c[4] for c in all_combs if c[2] == 'Conference Proceedings']
counter = collections.Counter(conf_venues)

with open('frequency/conf_venues.tsv', 'w') as f:
    for k, v in counter.most_common():
        f.write(f'{k}\t{v}\n')

print("\nConference venues and frequencies are saved in frequency/conf_venues.tsv")
