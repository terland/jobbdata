import pandas as pd
from main import get_jobs
import re

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

data = get_jobs()
for job in data['content']:
    title_list.append(str(job['jobtitle']) + " @ " + job['title'])
    description_list.append(clean_html(str(job['description'])))

all_jobs['title'] = title_list
all_jobs['description'] = description_list

# Implement bag-of-words modelling of data

print(all_jobs)