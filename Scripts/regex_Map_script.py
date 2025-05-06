# import neccessary libraries
import pandas as pd
import plotly.express as px

# Load regex counts and gazetteer files
counts = pd.read_csv("../Scripts/regex_counts.tsv", sep="\t")
coords = pd.read_csv("../gazetteers/geonames_gaza_selection.tsv", sep="\t")

#Check CHATGPT Solution 4A.1
# Write a code to rename 'asciiname' to 'placename' in the coords DataFrame to match counts
coords.rename(columns={'asciiname': 'placename'}, inplace=True)

# write a code to merge the data
data = pd.merge(counts, coords, on="placename")

# Create animated map showing place name frequency by month
fig = px.scatter_geo(
    data,
    lat="latitude",
    lon="longitude",
    hover_name="placename",
    size="count",
    animation_frame="month",
    projection="natural earth",
    title="Regex-extracted Place Names by Month"
)

# show map in internet browser
fig.show()

# Save to HTML and PNG files
fig.write_html("regex_map.html")
fig.write_image("regex_map.png")
