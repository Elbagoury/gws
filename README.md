# GWS:Automation
## Covert Txt to Csv Explanation:
1. Regex patterns: Regular expressions are used to match lines starting with Date:, Subject:, Message-ID:, and Delivered-To:.
2. Data collection: Extracted values are stored in lists. We ensure all lists have the same length by limiting the entries to the shortest list (min()).
3. CSV writing: The csv module writes the extracted data into a CSV file.
   
The script will generate a CSV file named email_summary.csv with the required fields.
