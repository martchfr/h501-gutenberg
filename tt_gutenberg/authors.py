import pandas as pd

def list_authors():

    # Setup and read-in all CSV files
    gutenberg_authors = r"C:\Users\martchfr\OneDrive - Indiana University\Graduate School\MIS\INFO-H 501\Projects\h501-gutenberg\tt_gutenberg\gutenberg_authors.csv"
    gutenberg_metadata = r"C:\Users\martchfr\OneDrive - Indiana University\Graduate School\MIS\INFO-H 501\Projects\h501-gutenberg\tt_gutenberg\gutenberg_metadata.csv"
    authors_df = pd.read_csv(gutenberg_authors)
    metadata_df = pd.read_csv(gutenberg_metadata)

    # Merge Dataframes
    metadata_w_authors_df = pd.merge(metadata_df, authors_df, on="gutenberg_author_id")
    metadata_w_authors_df["translation_count"] = 1

    grouped_df = metadata_w_authors_df.groupby(
        ["gutenberg_author_id", "alias"], as_index=False
        ).agg(sum_translation_count=("translation_count", "sum")).sort_values(by="sum_translation_count", ascending=False)

    author_list_descending = list(grouped_df["alias"])
        
    return author_list_descending
