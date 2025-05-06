# FASDH25-MiniProject-2
This project uses two different techniques — regular expressions with a gazetteer, and named entity recognition (NER) — to extract and visualize place names mentioned in news articles about the Gaza conflict. The goal is to evaluate and compare the performance of both methods through quantitative data and geospatial visualizations.
## Folder Structure
FASDH25-Portfolio2/
├── Scripts/ # Python scripts for regex, NER, gazetteer, and map generation
│ ├── regex_script_final.py
│ ├── Gaza_NER2_rukhshan_shabir_Samrin.py
│ ├── build_gazetteer.py
│ ├── regex_Map_script.py
│ └── NER_Map_script.py
│
├── AI Documentations/ # Individual documentation files by team members
│ ├── AI Documentation_Shabir_Karim.docx
│ ├── AI_documentation_Rukhshan_rehmat.docx
│ └── AI_documentation_Samrin_Alam.docx
│
├── Data/
│ ├── Input/ # Gazetteer and count data used for processing
│ │ ├── ner_counts.tsv
│ │ ├── NER_gazetteer.tsv
│ │ ├── regex_counts.tsv
│ │ └── geonames_gaza_selection.txt
│ │
│ └── Output/ # Processed data and generated maps
│ ├── regex_counts.tsv
│ ├── NER_gazeetteer.tsv
│ ├── ner_counts.tsv
│ ├── regex_map.PNG
│ ├── regex_map.HTML
│ ├── ner_map.PNG
│ └── ner_map.HTML
│
├── articles/ # News articles corpus (January 2024)
├── gazatteers/ # Additional gazetteer files if any
└── README.md # Project documentation
I hope the above structure explains our repository, it explains what each folder and file contains.
## Project Discription
This portfolio project explores the automatic extraction and mapping of geographic place names from a corpus of Gaza-related news articles. It focuses on two natural language processing approaches:
1. Regex + Gazetteer Matching: This method uses pattern matching with enhanced regular expressions based on a gazetteer of Gaza locations.
2. Named Entity Recognition (NER): This method uses the `stanza` NLP library to detect place names from raw text.

## Project Steps

### 2A: Regex and Gazetteer-Based Place Extraction
####  Objective
To identify and count mentions of Gaza place names in a collection of news articles using regular expressions and an enriched gazetteer, focusing only on articles published after the Gaza war began (October 7, 2023).
#### Script Overview
The script follows these key steps:

1. Load Gazetteer:
    Reads the file geonames_gaza_selection.tsv.
    Extracts multiple name variants for each place to build a more complete list of matchable names.

2. Compile Regex Patterns:
    Each place's names are escaped for regex safety and joined into a single regex pattern with word boundaries (`\b`) to match whole words only.
    Patterns are stored in a dictionary with the `asciiname` as the key.

3. Process Articles:
    Loops through all `.txt` files in the `articles` folder.
    Extracts the date from each filename and filters out articles published before `2023-10-07`.

4. Match and Count:
    For each article, all regex patterns are applied to count how often each place is mentioned.
    Counts are aggregated per place, per month(`YYYY-MM`).

5. Write Results to File:
    Outputs the counts to a TSV file named `regex_counts.tsv` with the format:
    This file is used later to generate maps and visualize which areas in Gaza are most frequently mentioned in the articles.
    
### 2B: Extracting Place Names from News Articles using Stanza NER
#### Objective
To process a large collection of news texts using NLP and generate a tsv file listing:
 Each unique place name
 How many times each was mentioned across the dataset
This tsv output can later be visualised as a map to understand which geographic locations dominate news reporting.
#### Script Overview 
1. Install and Set Up Stanza: 
   The stanza library is installed, and the English-language model is downloaded. This prepares the NLP toolkit for tokenization and named entity recognition (NER).

2.  Create the NLP Pipeline:
   A reusable Stanza pipeline is built using the `tokenize` and `ner` processors. This setup enables efficient text segmentation and entity extraction for each article.

4. Extract Location Entities: 
   The script loops through each `.txt` article file, processes its text through the NLP pipeline, and extracts named entities labeled as `GPE` (geo-political entity) or `LOC` (location). 

5. Normalize and Count Mentions: 
   Extracted place names are cleaned and standardized to ensure consistent counting. A dictionary is used to keep a running total of how many times each place is mentioned.

6. Write Results to File: 
   The place mention counts are saved in a TSV file called `ner_counts.tsv`, with two columns:

### 3: Create a gazetteer for the NER places
#### Objective
This project traces the geographic mentions in a collection of articles by extracting place names and visualizing their frequency on interactive maps.
#### Script Overview
1. Article Collection:
   A dataset of news articles is gathered and saved in a folder. These articles serve as the raw input for all further processing.

2. Place Name Extraction (Regex and NER):
    Regex + Gazetteer: A curated list of Gaza place names is matched using regex. Multiple name variants are compiled per location to improve recall.  
    NER (Stanza): A neural NLP pipeline automatically detects location-based named entities (GPE and LOC) in each article.  
   Both methods produce `.tsv` files that count how many times each place is mentioned.

3. Geocoding (NER only):
   Unique place names identified by NER are passed through the GeoNames API to fetch geographic coordinates.  
   For names that fail to return results, manual Google searches are used. Results are saved in `NER_gazetteer.tsv`.

4. Mapping: 
   Using plotly.express, two kinds of maps are generated: 
    Regex Map:An interactive animated map showing monthly place name frequencies. 
    NER Map: A static map visualizing January 2024 frequencies with coordinates from the geocoding step. 
    Each map is saved in both .html (interactive) and .png (static) formats.

5. Documentation and Packaging:
   The entire workflow, including scripts, input/output data, and analysis notes, is organized in a structured folder with a README.md file. 
   A critical reflection comparing regex vs. NER performance is included as part of the final deliverables.

### 4A: 4A. Map the regex-extracted placenames
#### Objective
To visualize the frequency of place names extracted using regular expressions, we used plotly.express to generate an interactive, animated map. This map displays how often each Gaza location was mentioned month-by-month.
#### Script Overview
1. Data Preparation:
    Loaded the file (regex_counts.tsv) which contains monthly mention counts of places.
    Loaded the file (geonames_gaza_selection.tsv) to get the latitude and longitude for each place.
    Renamed the (asciiname) column to (placename) to allow a successful merge.
    Merged the datasets on (placename) to combine frequency and coordinate data.

2. Map Creation:
    Used (px.scatter_map) to create a monthly animated scatter map.
    Each dot represents a place, with size proportional to the number of mentions.
    The map is animated by month (animation_frame="month"), allowing us to trace temporal trends.
    A red-yellow color scale (YlOrRd) was used to visually represent intensity.

3. Output:
    Saved as (regex_map.html) for the interactive version.
    Exported as (regex_map.png) for the static image.

#### Why This Approach:
We experimented with both static and animated maps. The animated version was chosen because it clearly illustrates how the spatial focus of media coverage shifts over time. Using marker size to represent frequency makes it easier to spot hotspots, while hover labels enhance interactivity and interpretability.

### 4B. Map the NER-extracted placenames
#### Objective
This map displays the frequency of place names extracted using Named Entity Recognition (NER) in January 2024. It offers a snapshot of how often each location was mentioned in the article dataset for that month.
#### Script Overview 
1. Data Preparation:
    Loaded (ner_counts.tsv), which contains frequency counts for places detected using NER.
    Loaded (NER_gazetteer.tsv), which includes latitude and longitude for those places obtained via GeoNames API or manual lookup.
    Renamed the column (Place) in the counts data to (placename) to allow for merging.
    Merged both datasets using the (placename) column.
    Converted the (Count) column to numeric and removed any rows with missing coordinate or count data.

2. Map Creation:
    Used (px.scatter_map) to plot each place with a bubble representing its frequency.
    Color and size of the markers correspond to the number of mentions.
    Hover labels show the place names for interactivity and readability.
3. Output:
    Saved as (ner_map.html) for the interactive version.
    Exported as (ner_map.png) for the static image.

##  Advantages and Disadvantages of Regex + Gazetteer vs. NER
### Regex + Gazetteer
Advantages: 
1. Highly accurate when matching known place names from the curated list.
2. Reduces false positives by only counting names explicitly listed in the gazetteer.
3. Allows precise control over what is counted and how (e.g., spelling variants).
Disadvantages:
1. Limited recall: will not detect any place names not in the gazetteer.
2. Rigid: fails to recognize variations, abbreviations, or misspellings not accounted for.
3. Treats close variants like (Jabaliya) and (Jabalia) as different places unless both are explicitly listed—this can split true counts across forms.
4. Manual effort required to build and maintain the gazetteer.
### Name Entity Recognition
Advantages:
1. Flexible: can identify unseen or unexpected place names in the text.
2. Less manual effort required—no need to predefine a list of place names.
3. Uses linguistic context, which can improve detection of nuanced place mentions.
Disadvantages: 
1. Lower precision: can include non-Gazan or ambiguous locations (e.g., common names like "Rafah" outside Gaza).
2. Sensitive to model limitations: performance depends on training data and model quality.
3. Geocoding required afterward, which can introduce noise or errors.

## Final Map Outputs
### Regex Map
![Regex Map](./data/output/regex_map.png)

### NER Map
![NER Map](./data/output/NER_map.png)


## Comparison of January 2024 Maps (Regex vs. NER)
There are two key differences between the maps generated from the regex and NER methods:

1. In the NER map, the locations are spread across the globe, including places outside Gaza. In contrast, the regex map is strictly limited to locations within Gaza, based on the curated gazetteer.

2. The counts for many places in the NER map are higher than those in the regex map. For example, the frequency of (Gaza) in the NER map is significantly higher than in the regex map. This may be due to the NER model identifying more variations or contexts of the place name that the regex method did not capture.

## Self Analysis
1. Weakness:
One of the main challenges in the project was handling the inconsistency in place names, especially with the NER method. The NER approach resulted in many duplicate or slightly different forms of the same place, which were treated as separate entries (for example, "Jabalia" and "Jabaliya"). Merging all these variations manually within the limited timeframe was not possible, which led to inflated or fragmented counts. Additionally, many places identified by NER had no coordinates available through automated geocoding services like GeoNames. We attempted to manually look up missing coordinates for several entries (e.g., Africa4Palestine, Jawwal, Pashias, Qffd, Almawasi, Alarouri, Alahli, etc.), but found that some were not real geographic locations—rather, they were names of organizations, people, or unclear terms. In the regex approach, another issue was inconsistency in results across different group members, possibly caused by small differences in regex implementation, encoding, or input file handling. This made it difficult to fully align outputs for comparison and verification.

2. Improvements:
If we had more time, several improvements could significantly enhance the quality of the results. First, we would invest more effort in cleaning and normalizing the NER output, possibly using fuzzy matching, gazetteer linking, or clustering techniques to merge near-duplicate place names. Second, we would automate and improve the geocoding process by integrating fallback services or using contextual filtering to exclude non-geographic entities before assigning coordinates. For the regex method, creating a shared, tested preprocessing script would ensure consistency in outputs across environments. We would also expand the gazetteer with more variant spellings and transliterations to capture place names that were missed. Finally, additional qualitative analysis—such as classifying mentions by article tone or event context—would make the maps more informative and analytically rich.





 
 


