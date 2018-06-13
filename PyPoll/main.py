import os

#establish root, data, and output 
root_path = os.path.join(os.getcwd(), ".")
data_path = os.path.join(root_path, "raw_data")
output_path = os.path.join(root_path, "output")

# Iterate through the listdir results
filepaths = []
for file in os.listdir(data_path):
    if file.endswith(".csv"):
        filepaths.append(os.path.join(data_path, file))