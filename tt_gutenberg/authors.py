import pandas as pd

def list_authors(by_languages=False, alias=False):
    """ Function to list authors from Project Gutenberg dataset. """

    # Setup and read-in all CSV files from project gutenberg
    authors_df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    languages_df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
    metadata_df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
    subjects_df = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')

    # Merge Dataframes together 
    metadata_language_df = pd.merge(metadata_df, languages_df, on="gutenberg_id")
    metadata_w_authors_df = (pd.merge(metadata_language_df, authors_df, on="gutenberg_author_id"))

    # Aggregate total languages per author based on works
    grouped_df = metadata_w_authors_df.groupby(
            ["gutenberg_author_id", "author_x","alias"], as_index=False
            ).agg(sum_language_count=("total_languages", "sum")).sort_values(by="sum_language_count", ascending=False)

    if alias == False:
        return list(grouped_df["author_x"])
    else:
        return list(grouped_df["alias"])