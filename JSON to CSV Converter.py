#!/usr/bin/env python
# coding: utf-8

import json
import ijson
import pandas as pd
from progress.bar import IncrementalBar

filename = input("Enter the filename without extension: ")

with open(filename+'.json', encoding='ansi') as json_data:
    output_data = json.load(json_data)

ci_data = output_data['cis']

bar = IncrementalBar('Progress', max = len(ci_data))

column_names = ['Name', 'Vendor', 'Version', 'CI Type']

ci_list = pd.DataFrame(columns=column_names)

for data in ci_data:
    ci_name = data['properties']['name']
    ci_vendor= data['properties']['discovered_vendor'] or "None"
    ci_version= data['properties']['version'] or "None"
    ci_type = data['type']
    
    ci_list = ci_list.append({'Name':ci_name,'Vendor':ci_vendor,'Version': ci_version,'CI Type':ci_type}, ignore_index=True)
    bar.next()
    
bar.finish()

ci_list.to_csv(filename+'.csv', index=False, encoding='utf-8')