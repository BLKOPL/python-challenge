import os
import csv

#establish root, data, and output 
root_path = os.path.join(os.getcwd(),".")
data_path = os.path.join(root_path,"raw_data")
output_path = os.path.join(root_path,"output")

#iterate through all csv to apply standard code
#This allows the code to apply to any new .csvs added
filepaths = []
for file in os.listdir(data_path):
    if file.endswith(".csv"):
        filepaths.append(ows.path.join(data_path, file))

#Applying DictReader method to standardize python code for all files in filepath list
for file in filepaths:
    tot_revenue = 0
    month_count = 0
    revenue = 0 
    rev_change = 0
    data_dict_list = []
    with open(file, newline="") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader