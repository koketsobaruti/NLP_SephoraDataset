import pandas as pd
import os
from nltk.corpus import stopwords
import viewdatasets

def remove_stopwords():
    df = viewdatasets.read_data()
    stop_words = set(stopwords.words('english'))
    df['review_text'] = df['review_text'].apply(lambda x: ' '.join([word for word in x.split() if word.lower() not in stop_words]))
    return df

def create_file(df):
    try:
        df.to_csv('no_stopwords_reviews.csv')
    except Exception as inst:
        print(type(inst))  # the exception type
        print(inst.args)  # arguments stored in .args
        print(inst)  # __str__ allows args to be printed directly,
        # but may be overridden in exception subclasses
    else:
        print("file created")

__folder = os.path.dirname(os.path.abspath(__file__))
__filename = '%s/no_stopwords_reviews.csv' % __folder

def read_data():
    reviews_df = pd.read_csv(__filename,index_col=0)
    reviews_df = reviews_df.dropna()
    reviews_df = reviews_df.reset_index(drop=True)
    return reviews_df