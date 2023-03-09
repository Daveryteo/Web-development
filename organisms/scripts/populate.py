import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append('C:/Users/keane/PycharmProjects/pythonProject/organisms')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'organisms.settings')
django.setup()

from proteins.models import *

#creating variables for the files
dataset = 'data/assignment_data_set.csv'
dataseq = 'data/assignment_data_sequences.csv'
pfamdesc = 'data/pfam_descriptions.csv'

pfam = set()
taxonomy = defaultdict(list)
domain = defaultdict()
protein = defaultdict(list)
proteindomainlink = defaultdict(list)

with open(pfamdesc) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')

    #for each row we store the id and description in the set
    for row in csv_reader:
        pfam.add((row[0], row[1]))

with open(dataseq) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    #make the protein id the key and store a list where the first element in the list is the sequence
    for row in csv_reader:
        protein[row[0]] = [row[1], '', '']
        
with open(dataset) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    for row in csv_reader:
        #check if taxonomy is in the dict if it is not add it
        if row[1] not in taxonomy.keys():
            #split the genus and species
            genus_species_split = row[3].split()
            #store the taxonomy entry
            #taxa_id is the key
            #[clade, genus, species]
            taxonomy[row[1]] = [row[2], genus_species_split[0], genus_species_split[1]]

        #check if domain is in the dict and add if it is not
        if row[5] not in domain.keys():
            #store the domain entry where domain_id is the key
            #store domain_description
            domain[row[5]] = row[4]

        #check if protein is in the dict and add if it is not
        if row[0] not in protein.keys():
            protein[row[0]] = ['', row[1], row[8]]

        else:
            #if the protein exists add the data to it
            #[sequence, taxa_id, length]
            protein[row[0]][1] = row[1]
            protein[row[0]][2] = row[8]
            
        #store the start and stop
        proteindomainlink[(row[0], row[5])] = [row[6], row[7]]

#delete everything and repopulate the database
Protein_Domain_link.objects.all().delete()
Pfam.objects.all().delete()
Taxonomy.objects.all().delete()
Protein.objects.all().delete()

#store data for foreign key
pfamRow = {}
taxaRow = {}
proteinRow = {}

#loop through all the data and creating the rows
for p in pfam:
    row = Pfam.objects.create(
        domain_id = p[0],
        domain_description = p[1]
    )
    row.save()
    pfamRow[p[0]] = row

for t_id, data in taxonomy.items():
    row = Taxonomy.objects.create(
        taxa_id = t_id,
        clade = data[0],
        genus = data[1],
        species = data[2]
    )
    row.save()
    taxaRow[t_id] = row
    
for p_id, data in protein.items():
    row = Protein.objects.create(
        protein_id = p_id,
        sequence = data[0],
        taxonomy = taxaRow[data[1]],
        length = data[2]
    )
    row.save()
    proteinRow[p_id] = row

for pd_id, data in proteindomainlink.items():
    row = Protein_Domain_link.objects.create(
        protein = proteinRow[pd_id[0]],
        pfam_id = pfamRow[pd_id[1]],
        description = domain[pd_id[1]],
        start = data[0],
        stop = data[1]
    )
    row.save()


