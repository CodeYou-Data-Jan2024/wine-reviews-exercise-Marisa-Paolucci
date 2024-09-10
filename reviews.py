import pandas as pd

# Reads the file in from data csv file
df_wine_reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")

# groupby('country') groups the data by the 'country' column. agg() allows you to perform multiple aggregations at once. 'size' counts the number of reviews, and the average is calculated by mean and points. reset_index() restores 'country' as a column instead of an index.
summary_df = df_wine_reviews.groupby('country').agg(count=('country', 'size'), points=('points', 'mean')).reset_index()

# Round(1) is used to round the average points to one decimal place.
summary_df['points'] = summary_df['points'].round(1)

#print(summary_df)

# this writes the summary to the csv folder using .to_csv. Use data/ to have it saved under the dat folder. index=False can be used to exclude the index column when saving to the csv file. 
summary_df.to_csv('data/reviews_per_country.csv', index=False)




