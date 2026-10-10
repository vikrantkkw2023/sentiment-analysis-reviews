import pandas as pd
df = pd.read_csv('data/reviews.csv')
print("Here is the structure of the DataFrame:","\n",df.head())
print("Shape of the DataFrame:",'\n', df.shape)
print("Null values in each column:",'\n', df.isnull().sum())
print("Columns in the DataFrame:",'\n', df.columns)      
print("Column names:",'\n',df.columns.tolist())


TEXT_COL = "Text"      # change to your review text column
RATING_COL = "Score"   # change to your star rating column

print(df[RATING_COL].value_counts().sort_index())

def to_sentiment(r):
    if r <= 2:
        return "negative"
    elif r == 3:
        return "neutral"
    return "positive"

df["sentiment"] = df[RATING_COL].map(to_sentiment)
print(df["sentiment"].value_counts(normalize=True))