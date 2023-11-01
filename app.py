from customer_reviews import reviews_data
import viewdatasets
import pandas as pd
from tokenization import stem_df
from lemmatize import lemmatize_df
import remove_stopwords


# reviews_df = reviews_data.read_data()
# # #conduct lemmatizing for the review_text column
# print('starting first process of lemmatizing')
# column = 'review_text'
# reviews_df = lemmatize_df(reviews_df, column)
# print('starting second process of lemmatizing')
# column = 'review_title'
# reviews_df = lemmatize_df(reviews_df, column)
#
# #create a new csv file with new dataset
# reviews_data.create_new_file(reviews_df)

# reviews_df = reviews_data.read_data()
# new_reviews_df = viewdatasets.read_data()
#
# print(reviews_df['review_text'].head(5))
# print(new_reviews_df['review_text'].head(5))

# column = 'review_text'
# no_stopwords_df = remove_stopwords.remove_stopwords()
# # # column = 'review_title'
# # no_stopwords_df = remove_stopwords.remove_stopwords()
# remove_stopwords.create_file(no_stopwords_df)
#
#
# reviews_df = viewdatasets.read_data()
new_reviews_df= remove_stopwords.read_data()
#
# print(reviews_df['review_text'].head(5))
print(new_reviews_df['review_text'].head(5))