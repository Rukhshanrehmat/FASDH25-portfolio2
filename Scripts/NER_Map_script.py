import pandas as pd
import plotly.express as px

# Load data
counts = pd.read_csv("../Scripts/ner_counts.tsv", sep="\t")
coords = pd.read_csv("../Scripts/NER_gazetteer.tsv", sep="\t")

# Rename 'Place' to match 'placename'
counts = counts.rename(columns={"Place": "placename"})

# Merge data on 'placename'
data = pd.merge(counts, coords, on="placename")

# Convert 'Count' to numeric and clean up
data["Count"] = pd.to_numeric(data["Count"], errors="coerce")
data = data.dropna(subset=["Count", "latitude", "longitude"])

# Plot map
fig = px.scatter_geo(
    data,
    lat="latitude",
    lon="longitude",
    hover_name="placename",
    size="Count",
    color="Count",
    title="NER-Extracted Place Names (Jan 2024)",
    projection="natural earth"
)

# Save outputs
fig.write_html("ner_map.html")
fig.write_image("ner_map.png", scale=2)

# Optionally display
fig.show()


