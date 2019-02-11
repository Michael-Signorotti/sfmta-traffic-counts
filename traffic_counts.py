"""
Converts the SFMTA traffic count data from pdf format to a Pandas dataframe.

The method converts the SFMTA traffic count dataset from pdf format to a pandas
dataframe. This utility converts the data successfully as of the current
version of the hosted dataset on 1/12/19.
"""
import tabula
import re

url_of_pdf = "https://www.sfmta.com/sites/default/files/reports/2016/SFMTA%20Traffic%20Count%20Data%201993-2015%20with%20cover%20sheet.pdf"
file_destination = "traffic_counts.csv"

# Retrieve pdf at url_of_pdf in a pandas DataFrame
df = tabula.read_pdf(url_of_pdf, pages="2-1496", lattice=True)

# Delete NOTES column
df = df[[col for col in df.columns if col.upper() != "NOTES"]]

# Rename columns so that their names have no spaces
col_list = ["PRIMARY_STREET", "CROSS_STREET", "AT", "CROSS_STREET_2",
            "DIRECT", "DAY", "DATE", "VOLUME", "AM_PEAK", "PM_PEAK"]
df.columns = col_list

# Use all caps and remove spaces for consistency
df = df.applymap(lambda x: x.strip().upper() if type(x) == str else x)

# Eliminate rows which only consist of table headers
df = df[df["PRIMARY_STREET"] != "PRIMARY STREET"]

'''
Remove carriage returns from all entries to avoid errors in rendering the csv
'''
for col in col_list:
    df[col] = df[col].apply(lambda x: re.sub("\r", "", str(x)))

df.reset_index()
# Save as a csv file
df.to_csv(file_destination)
