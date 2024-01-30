import pandas as pd

def merge_dataframes(attr_df, partition_df):
    # Merge the two dataframes on the index
    merged_df = partition_df.join(attr_df['Male'], how='inner')

    # Convert -1 to 0 in the 'male' column
    merged_df['Male'] = merged_df['Male'].apply(lambda x: 0 if x == -1 else x)

    merged_df.reset_index(inplace=True)

    return merged_df