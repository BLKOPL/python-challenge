import os
import csv

#establish root, data, and output 
root_path = os.path.join(os.getcwd(), ".")
data_path = os.path.join(root_path, "raw_data")
output_path = os.path.join(root_path, "output")

#iterate through all csv to apply standard code
#This allows the code to apply to any new .csv added
filepaths = []
for file in os.listdir(data_path):
    if file.endswith(".csv"):
        filepaths.append(os.path.join(data_path, file))

#Applying .DictReader method to standardize python code for all files in filepath list
for file in filepaths:
    tot_revenue = 0
    month_count = 0
    revenue = 0 
    rev_change = 0
    data_dict_list = []
    with open(file, newline="") as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            #establish rev_diff dictionary to cauculate max/min
            rev_diff = {"rev_diff": int("{Revenue}".format(**row)) - revenue}
            rev_change = rev_change + int("{Revenue}".format(**row)) - revenue
            revenue = int("{Revenue}".format(**row))
            tot_revenue += revenue
            month_count += 1
            data_dict_list.append({**row, **rev_diff})
        #parse out data_dict_list into max and min dictionaries
        increase_dict = dict(max(data_dict_list, key=lambda x:x["rev_diff"]))
        decrease_dict = dict(min(data_dict_list, key=lambda x:x["rev_diff"]))
        #pull dqate and rev_diff valuesw for corresponding min/max months.
        increase_date = increase_dict.get("Date")
        increase_revdiff = increase_dict.get("rev_diff")
        decrease_date = decrease_dict.get("Date")
        decrease_revdiff = decrease_dict.get("rev_diff")
        #skip over data in the first row 
        first_row = data_dict_list[0]
        first_row_revdiff = first_row.get("rev_diff")
        rev_change = rev_change - first_row_revdiff
        avg_change = int(rev_change/(month_count-1))

        #grab the filename from the original path 
        #note that _, gets rid of the path and , getss rid of the .csv
        _, filename = os.path.split(file)
        filename, _ = filename.split(".csv")

        #print results to terminal using template literals
        print(
            f"Financial Analysis = {filename}\n"
            f"----------------------------\n"
            f"Total Months = {month_count}\n"
            f"Total Revenue = {tot_revenue}\n"
            f"Average Revenue Change = {avg_change}\n"
            f"Greatest Increase In Revenue: {increase_date} (${increase_revdiff}\n"
            f"Greatest Decrease In Revenue: {decrease_date} (${decrease_revdiff}\n"
        )

        #generate .txt file for datasets and export that to output folder.
        text_path = os.path.join(output_path, filename + ".txt")
        with open(text_path, "w") as text_file:
            text_file.write(
            f"Financial Analysis = {filename}\n"
            f"----------------------------\n"
            f"Total Months = {month_count}\n"
            f"Total Revenue = {tot_revenue}\n"
            f"Average Revenue Change = {avg_change}\n"
            f"Greatest Increase In Revenue: {increase_date} (${increase_revdiff}\n"
            f"Greatest Decrease In Revenue: {decrease_date} (${decrease_revdiff}\n"
        )


