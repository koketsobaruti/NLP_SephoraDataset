import re
import removePunc
import pandas as pd

reviews_df= removePunc.read_data()
pattern = r'\'\S+'
reviews_df['review_text'] = reviews_df['review_text'].apply(lambda x: x.replace(" ",""))
reviews_df['review_title'] = reviews_df['review_title'].apply(lambda x: x.replace(" ",""))

try:
    reviews_df.to_csv('cleaned_data.csv')
except Exception as inst:
    print(type(inst))  # the exception type
    print(inst.args)  # arguments stored in .args
    print(inst)  # __str__ allows args to be printed directly,
    # but may be overridden in exception subclasses
else:
    print("file created")