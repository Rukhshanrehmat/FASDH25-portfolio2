# Importing all necessary libraries

import re         # for  using regular expresssions
import os         # this library is to work with folders and files
import pandas as pd  # for handling data

articles_folder = "../articles"                              # this code defines which folder to use
gazetteer_path = "../gazetteers/geonames_gaza_selection.tsv" # load the gazetteer from the tsv file

# write a code to create an empty dictionary to store regex patterns for each place name
patterns = {}
# wirte a code to read gazetteer data
with open(gazetteer_path, encoding="utf-8") as file:
    data = file.read()
# write a code to split gazetter data into individual row by newline
rows = data.split("\n")
# write a code to loop through each row
for row in rows[1:]:
    columns = row.split("\t")    # this will split the columns using tabs
    if not columns[0].strip():   # It will skip rows with empty aciiname 
        continue                 # it explains skip this and move to next if it is incomplete
 # write a code to check if there are at least 6 columns, skip rows that don't have enough columns
    if len(columns) < 6:
        continue
    # write a code to extract asciiname (column 0)
    asciiname = columns[0].strip()
    # create a list to store all names
    all_names = [asciiname]
    # write a code to include column 4 (code is adapted with the help of CHATGPT: Check Solution 2A.1)
    if len(columns) > 4:
        name_col = columns[4].strip()
        if name_col:
            all_names.append(name_col)
    # write a code to include column 5 (code is adapted with the help of CHATGPT: Check Solution 2A.1)
    if len(columns) > 5:
        alternate_names = columns[5].strip()
        if alternate_names:
            alternate_list = alternate_names.split(",")    # this code will get individual alternate names splitted by commas
            for alt in alternate_list:
                alt = alt.strip()
                if alt:
                    all_names.append(alt)
    # The following chunk of codes are adapted with the help of CHATGPT : check solution 2A.1
    
    # write a code to escape all names so that special characters do not break the regex
    escaped_names = [re.escape(name) for name in all_names if name]

    # Build a single regex that matches any of the name variations
    # The word boundaries (\b) ensure we match whole words only
    regex_string = r"\b(" + "|".join(escaped_names) + r")\b"

    # Compile the regex with case-insensitive flag
    compiled_pattern = re.compile(regex_string, re.IGNORECASE)

    # Store the compiled regex and a count (starting at 0)
    # Use the asciiname as the dictionary key
    patterns[asciiname] = {
        "pattern": compiled_pattern,
        "count": 0
    }
    
# write a code to define the start date of war
mentions_per_month = {}    # make an empty dictionary
war_start = "2023-10-07"

#write a code to loop through articles
for filename in os.listdir(articles_folder):
    if not filename.endswith(".txt"):
        continue            # this code will only process the text files

    # extract date from filename Check Solution 2A.2
    date_str = filename.split("_")[0]
    # write a code to skip article if it's before the war started
    if date_str < war_start:
        continue
    # extract month as "YYYY-MM"
    month_key = date_str[:7]
    # write a code that give filepath to the current articles
    file_path = os.path.join(articles_folder, filename) # Check Solution 2A.3
    # write a code to load and process the articles
    with open(file_path, encoding="utf-8") as file:
        text = file.read()

# for the following some codes i took help of my friend and CHATGPT to Understand Check Solution 2A.4
    # write a code to loop through each places
    for place in patterns:
        regex = patterns.get(place).get("pattern")
        matches = regex.findall(text)
    
        if matches:
            if place not in mentions_per_month: # If this place has never been recorded before, this will record it 
                mentions_per_month[place] = {}

            if month_key not in mentions_per_month[place]:  # If this month hasn't been recorded for the place, this will record it
                mentions_per_month[place][month_key] = 0
# write a code to give total count
            mentions_per_month[place][month_key] += len(matches)



# Check CHATGPT Solution 2A.5
# Now, create a file named "regex_counts.tsv"
# We use "with" so that python closes the file automatically after writing. 
with open("../Scripts/regex_counts.tsv", "w", encoding="utf-8") as f:
    
    # Write the header line for the TSV file
    f.write("placename\tmonth\tcount\n")        # Here in this code \t means tab. So this code writes Placename[TAB]month[TAB]count.

    # Loop through each place. 
    for place in mentions_per_month:
        #write a code to get monthly counts for each place
        month_counts = mentions_per_month[place]
        # Loop through each month and its count
        for month in month_counts:
            count = month_counts[month]
            # Write a code to add one row to the file in tab-separated format
            f.write(f"{place}\t{month}\t{count}\n")
    
