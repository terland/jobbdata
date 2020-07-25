import pandas as pd
from main import get_jobs
import re

# Clean text
def clean_html(desc):
    desc = desc.lower()
    desc = re.sub('<.>|</.>|<..>|</..>',' ',desc)
    desc = re.sub(' +',' ',desc)
    desc = desc.lower()
    return(desc)

print(clean_html('<a/> Www <p> pwpwpda </p>'))

# Get all job-descriptions, along with titles.

all_jobs = pd.DataFrame()


title_list = []
description_list = []

data = get_jobs()
for job in data['content']:
    title_list.append(str(job['jobtitle']) + " @ " + job['title'])
    


    description_list.append(str(job['description']))

all_jobs['title'] = title_list
all_jobs['description'] = description_list
print(all_jobs)