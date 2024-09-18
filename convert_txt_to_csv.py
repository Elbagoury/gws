import re
import csv

# File paths
input_file = "input.txt"
output_file = "email_summary.csv"

# Read the data from the text file
with open(input_file, 'r') as file:
    input_text = file.read()

# Regex patterns to extract the relevant information
date_pattern = re.compile(r'Date:\s(.+)', re.IGNORECASE)
subject_pattern = re.compile(r'Subject:\s(.+)', re.IGNORECASE)
message_id_pattern = re.compile(r'Message-ID:\s(.+)', re.IGNORECASE)
delivered_to_pattern = re.compile(r'Delivered-To:\s(.+)', re.IGNORECASE)

# Lists to store the extracted data
data = []

# Extract all relevant lines
dates = date_pattern.findall(input_text)
subjects = subject_pattern.findall(input_text)
message_ids = message_id_pattern.findall(input_text)
delivered_tos = delivered_to_pattern.findall(input_text)

# Ensure all lists have the same length
num_entries = min(len(dates), len(subjects), len(message_ids), len(delivered_tos))

# Prepare the data for CSV
for i in range(num_entries):
    data.append([dates[i], subjects[i], message_ids[i], delivered_tos[i]])

# Write the data to a CSV file
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Subject", "Message-ID", "Delivered-To"])
    writer.writerows(data)

print(f"Data successfully written to {output_file}")
