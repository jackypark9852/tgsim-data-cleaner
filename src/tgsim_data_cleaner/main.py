import pandas as pd 
import sys
import cleaner as cl
import graph as gr

ARGUMENT_COUNT = 3
if(len(sys.argv) != ARGUMENT_COUNT):
    print("Please ")

fix_excel_name = sys

# Open excel file 
fixes = pd.read_excel('ScriptTest1_Fixes.xlsx')
raw_data = pd.read_csv('test1.csv')
raw_data = raw_data.rename(columns={ raw_data.columns[0]: "id" })

# Splice for useful information
fixes = fixes.loc[:,['Initial ID','Changed ID', 'Time First Seen']].dropna()

# Sort by Time 
fixes = fixes.sort_values(by=['Time First Seen'])

#Construct graph 
graph = {}
invalid_fixes = []
redundant_fixes = []

for index, row in fixes.iterrows():
    changed_id = int(row['Changed ID'])
    initial_id = int(row['Initial ID'])
    time_first_seen = float(row['Time First Seen'])
    row_data = (index + 1, initial_id, changed_id, time_first_seen)
    if not cl.IsValidFix(initial_id, changed_id, graph): 
        invalid_fixes.append(row_data)
        continue
        
    initial_id_actual = initial_id if initial_id not in graph else gr.FindRootId(initial_id, graph)  
    changed_id_actual = changed_id if changed_id not in graph else gr.FindRootId(changed_id, graph)
    
    if(initial_id_actual == changed_id_actual):
        redundant_fixes.append(row_data)
    else: 
        if(initial_id_actual not in graph): 
            graph[initial_id_actual] = []
        if(changed_id_actual not in graph): 
            graph[changed_id_actual] = []
        cl.FixId(initial_id_actual, changed_id_actual, float(time_first_seen), raw_data)
        graph[changed_id_actual] = [initial_id_actual]

cl.PrintInvalidFixes(invalid_fixes) 
cl.PrintRedundantFixes(redundant_fixes)

raw_data.to_csv('output_01.csv', index=False)

print('PROCESS COMPLETE')

