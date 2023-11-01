import os
import re
import remove_stopwords
import pandas as pd

reviews_df= remove_stopwords.read_data()
pattern = r'\'\S+'
reviews_df['review_text'] = reviews_df['review_text'].apply(lambda x: re.sub(pattern,"", str(x)))
reviews_df['review_title'] = reviews_df['review_title'].apply(lambda x: re.sub(pattern,"", str(x)))

try:
    reviews_df.to_csv('removedPunc_data.csv')
except Exception as inst:
    print(type(inst))  # the exception type
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
else:
    print("file created")

__folder = os.path.dirname(os.path.abspath(__file__))
__filename = '%s/removedPunc_data.csv' % __folder

def read_data():
    reviews_df = pd.read_csv(__filename,index_col=0)
    reviews_df = reviews_df.dropna()
    reviews_df = reviews_df.reset_index(drop=True)
    return reviews_df