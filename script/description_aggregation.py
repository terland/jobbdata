import pandas as pd
import numpy as np
from main import get_jobs
import networkx as nx 
import re
import matplotlib.pyplot as plt
import math  

# Clean text
def clean_html(desc):
    desc = desc.lower()
    desc = re.sub('<.>|</.>|<..>|</..>|<strong>|</strong>',' ',desc)
    desc = re.sub(' +',' ',desc)
    desc = desc.lower()
    return(desc)

# Get all job-descriptions, along with titles.
all_jobs = pd.DataFrame()


title_list = []
description_list = []
company_list = []

data = get_jobs(data = {'published' : '[2020-01-01,2020-03-01]'})

for job in data['content']:
    title_list.append(str(job['jobtitle']) + " @ " + job['title'])
    description_list.append(clean_html(str(job['description'])))
    company_list.append(job['employer']['name'])

all_jobs['company'] = company_list
all_jobs['title'] = title_list
all_jobs['description'] = description_list

# Implement bag-of-words modelling of data
print(len(all_jobs.index))

# Find list of common words
all_words = {}
words_to_remove = {}

num_words = 0

for desc in all_jobs['description']:
    words = desc.split()
    for word in words:
        if (word in all_words):
            all_words[word] += 1
        else:
            all_words[word] = 1
            num_words += 1


# Remove popular words
limit = 5

for word in all_words:
    if (all_words[word] >= limit):
        words_to_remove[word] = 1


# Return yes if {i,j} in edge-set of relative graph.
def related_jobs(job_i,job_j):
    common_words = {}
    for word in job_i['description'].split():
        common_words[word] = 1
    
    for word in job_j['description'].split():
        if (word in common_words):
            common_words[word] = 2
        else:
            common_words[word] = 1

    for word in words_to_remove:
        common_words[word] = 0
    
    num_single = 0
    num_pair = 0

    for word in common_words:
        if (common_words[word] == 1):
            num_single += 1
        if (common_words[word] == 2):
            num_pair += 1

    if (num_pair > math.sqrt(num_pair+num_single)*2):
        return(1)
    
    return(0)


# Generate graph
node_labels = {}

adj = []
for i in range(0,len(all_jobs.index)):
    adj.append([0]*len(all_jobs.index))

for i in range(0,len(all_jobs.index)):
    node_labels[i] = all_jobs['company'].iloc[i]
    for j in range(i+1,len(all_jobs.index)):
        #print(related_jobs(all_jobs.iloc[i],all_jobs.iloc[j]))
        adj[i][j] = related_jobs(all_jobs.iloc[i],all_jobs.iloc[j])
        adj[j][i] = related_jobs(all_jobs.iloc[i],all_jobs.iloc[j])

print(adj)

G = nx.from_numpy_matrix(np.array(adj))  
nx.draw(G, with_labels=True,labels = node_labels,font_size = 12) 
plt.show()