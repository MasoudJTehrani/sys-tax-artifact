# %%
import json, os
import collections

json_dir_path = './json_files'

# %%
def parse(data):
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
        comb = (title, year, category, publisher, journal_name, abstract, url)
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
journal_venues = [c[4] for c in all_combs if c[2] == 'Journal']
conf_venues = [c[4] for c in all_combs if c[2] == 'Conference Proceedings']

# %%
for x in conf_venues:
    print(x)

# %%
def filter_venues(venues, query):
    # Lowercase the query and split it into terms
    terms = query.split(" OR ")
    # Filter papers based on title, conference, keywords, or abstract
    matching_venues = []
    for venue in venues:
        found = False
        for term in terms:
            if term in venue.lower():
                found = True
                break
        if found and venue not in matching_venues:
            matching_venues.append(venue)

    return matching_venues


query = "secure OR security OR privacy OR software engineering OR testing OR verification"
matching_confs = filter_venues(conf_venues, query)
matching_journals = filter_venues(journal_venues, query)

print("Matching Conferences:", len(matching_confs))
print("Matching Journals:", len(matching_journals))


# %%
excluded_journals = ['International Data Privacy Law',
                   'Asian Security',
                   'Security and Human Rights',
                   'International Journal of Nuclear Security',
                   'Journal of Strategic Security'
]
excluded_confs = ['DASC/PiCom/CBDCom/CyberSciTech',
                'AsianHOST',
                'International Symposium on Hardware Oriented Security and Trust',
                'International Conference and Exhibition on Health, Safety, Security, Environment',
                'Emerging Imaging and Sensing Technologies for Security and Defence',
                'International Conference on Software Engineering, Artificial Intelligence, Networking and Parallel/Distributed Computing',
                'TrustCom/BigDataSE',
                'International Symposium on Technologies for Homeland Security',
                'International Conference on Networking, Information Systems and Security: Envisage Intelligent Systems in 5G/6G-Based Interconnected Digital Worlds',
                'ACM ASIA Conference on Cyber-Physical System Security Workshop',
                'ACM on Asia Conference on Computer and Communications Security'
]

for ex in excluded_journals:
    for v in matching_journals:
        if ex in v:
            matching_journals.remove(v)

for ex in excluded_confs:
    for v in matching_confs:
        if ex in v:
            matching_confs.remove(v)

print("Matching Conferences:", len(matching_confs))
print("Matching Journals:", len(matching_journals))

# %%
def check_duplicate_papers(combs):
    title_count = collections.Counter([c[0].lower() for c in combs])
    dup = []
    for title, count in title_count.items():
        if count > 1:
            dup.append(title)
    return dup


add_journal_papers, add_conf_papers = [], []
for c in all_combs:
    if c[4] in matching_journals:
        add_journal_papers.append(c)
    if c[4] in matching_confs:
        add_conf_papers.append(c)
    
print(len(add_conf_papers))
dups = check_duplicate_papers(add_conf_papers)
for d in dups:
    for p in add_conf_papers:
        if d in p[0].lower():
            add_conf_papers.remove(p)
print(len(add_conf_papers))

print(len(add_journal_papers))
dups = check_duplicate_papers(add_journal_papers)
for d in dups:
    for p in add_journal_papers:
        if d in p[0].lower():
            add_journal_papers.remove(p)
print(len(add_journal_papers))

# %%
with open('papersAndLink - papersAndLink.tsv', 'r') as f:
    for line in f:
        line = line.strip()
        spl = line.split('\t')
        title = spl[0]

        for c in add_journal_papers:
            if title in c[0]:
                add_journal_papers.remove(c)
                break
        for c in add_conf_papers:
            if title in c[0]:
                add_conf_papers.remove(c)
                break
            
print(len(add_conf_papers))
print(len(add_journal_papers))    

# %%
# titles	abstract	URL	useful?	venue	year
with open('papersAndLink_se_sec.tsv', 'w') as f:
    # comb = (title, year, category, publisher, journal_name)
    for c in add_journal_papers:
        f.write('{}\t{}\t{}\t{}\t{}\n'.format(c[0], c[5], c[6], c[4], c[1]))
    for c in add_conf_papers:
        f.write('{}\t{}\t{}\t{}\t{}\n'.format(c[0], c[5], c[6], c[4], c[1]))


