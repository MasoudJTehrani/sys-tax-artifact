# %%
import json, os
import collections

json_dir_path = './json_files'

# %%
def parse(data):
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
                print('duplicate title: {}'.format(title))
                continue
            all_combs.append(comb)

# %%
print(len(all_combs))
print(all_combs[0])
print(all_combs[1])

# %%

journal_venues = [c[4] for c in all_combs if c[2] == 'Journal']
counter = collections.Counter(journal_venues)

# with open('journal_venues.tsv', 'w') as f:
#     for k, v in counter.most_common():
#         f.write(f'{k}\t{v}\n')

for k, v in counter.most_common():
    print(k)

# %%
conf_venues = [c[4] for c in all_combs if c[2] == 'Conference Proceedings']
counter = collections.Counter(conf_venues)

# with open('conf_venues.tsv', 'w') as f:
#     for k, v in counter.most_common():
#         print(k, v)
#         f.write(f'{k}\t{v}\n')

for k, v in counter.most_common():
    print(k)

# %% [markdown]
# ### Apply venue filter

# %%
venue_filters = []
with open('venue_filter.txt', 'r') as f:
    for line in f:
        line = line.strip()
        venue_filters.append(line)

# %%
with open('papers_after_venue_filter.txt', 'w') as f:
    for comb in all_combs:
        if comb[4] in venue_filters:
            f.write(f'{comb[0]}\n')
            print(comb[0])

# %%
new_lines = []
with open('papersAndLink - papersAndLink.tsv', 'r') as f:
    for line in f:
        line = line.strip()
        spl = line.split('\t')
        print(len(spl))
        title = spl[0]
        for c in all_combs:
            if title == c[0]:
                # print(c[4], c[1])
                spl.append(str(c[4]))
                spl.append(str(c[1]))
                break
        new_lines.append('\t'.join(spl))
    
with open('papersAndLink_year_venue.tsv', 'w') as f:
    for line in new_lines:
        f.write(f'{line}\n')


