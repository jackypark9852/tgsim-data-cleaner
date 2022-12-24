import pandas as pd
import sys
import cleaner as cl
import graph as gr
import argparse

# Parse input
parser = argparse.ArgumentParser()
parser.add_argument(
    "input_excel_filename", help="the name of the excel file to process"
)
parser.add_argument("input_csv_filename", help="the name of the csv file to process")
parser.add_argument("output_filename", help="the name of the file to output")
args = parser.parse_args()

if not args.input_excel_filename:
    parser.error("the following argument is required: input_excel_filename")
if not args.input_csv_filename:
    parser.error("the following argument is required: input_csv_filename")
if not args.output_filename:
    parser.error("the following argument is required: output_filename")

input_excel_filename = args.input_excel_filename
input_csv_filename = args.input_csv_filename
output_filename = args.output_filename

# Open input files
fixes = pd.read_excel(input_excel_filename)
raw_data = pd.read_csv(input_csv_filename)
raw_data = raw_data.rename(columns={raw_data.columns[0]: "id"})

# Splice for useful information
fixes = fixes.loc[:, ["Initial ID", "Changed ID", "Time First Seen"]].dropna()

# Sort Rows by Time
fixes = fixes.sort_values(by=["Time First Seen"])

# Apply Fixes
graph = {}
invalid_fixes = []
redundant_fixes = []

for index, row in fixes.iterrows():
    changed_id = int(row["Changed ID"])
    initial_id = int(row["Initial ID"])
    time_first_seen = float(row["Time First Seen"])
    row_data = (index + 1, initial_id, changed_id, time_first_seen)
    if not cl.IsValidFix(initial_id, changed_id, graph):
        invalid_fixes.append(row_data)
        continue

    initial_id_actual = (
        initial_id if initial_id not in graph else gr.FindRootId(initial_id, graph)
    )
    changed_id_actual = (
        changed_id if changed_id not in graph else gr.FindRootId(changed_id, graph)
    )

    if initial_id_actual == changed_id_actual:
        redundant_fixes.append(row_data)
    else:
        if initial_id_actual not in graph:
            graph[initial_id_actual] = []
        if changed_id_actual not in graph:
            graph[changed_id_actual] = []
        cl.FixId(initial_id_actual, changed_id_actual, float(time_first_seen), raw_data)
        graph[changed_id_actual] = [initial_id_actual]

cl.PrintInvalidFixes(invalid_fixes)
cl.PrintRedundantFixes(redundant_fixes)

raw_data.to_csv(output_filename, index=False, chunksize=1000000)

print("PROCESS COMPLETE")
