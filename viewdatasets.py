import os
import pandas as pd
from customer_reviews import reviews_data

__folder = os.path.dirname(os.path.abspath(__file__))
__filename = '%s/lemmatized_reviews.csv' % __folder

def read_data():
    new_reviews_df = pd.read_csv(__filename,index_col=0)
    new_reviews_df = new_reviews_df.dropna()
    new_reviews_df = new_reviews_df.reset_index(drop=True)
    return new_reviews_df


