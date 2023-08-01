# Capstone Project: RPABiblio
# Robot to Combine CSV files downloaded from Scopus

# Import the relevant Python libraries
import os
import pandas as pd

# Get a list of the CSV files in current directory that start with scopus and end with .csv
csv_files = [file for file in os.listdir(os.getcwd()) if file.startswith('scopus') and file.endswith('.csv')]

# Create empty dataframe to store merged data
master_df = pd.DataFrame()

# Loop through each CSV file while reading the CSV file into a DataFrame
# then append the data to master DataFrame
for file in csv_files:
    df = pd.read_csv(file, encoding='utf-8')
    master_df = master_df._append(df, ignore_index=True)
# then remove the processed file
    os.remove(file)

# Set the output file name
output_file_name = 'export.csv'
output_file_base, output_file_ext = os.path.splitext(output_file_name)

# Checks if the current output file name already exists,
# and if so, add a counter to the file name
if os.path.isfile(output_file_name):
    counter = 1
    while os.path.isfile(output_file_name):
        output_file_name = f"{output_file_base}_{counter}{output_file_ext}"
        counter += 1

# Export the merged DataFrame to a CSV file
# encode in utf-8-sig to ensure characters do not deform (eg: úñ)
master_df.to_csv(output_file_name, index=False, encoding='utf-8-sig')

# When complete, print a success message along with the exported file name
print(f"CSV files merged successfully and exported as '{output_file_name}'.")
