from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from functools import reduce
# Initialize wordnet lemmatizer
wnl = WordNetLemmatizer()
# Example inflections to reduce
example_words = ["program","programming","programer","programs","programmed"]

def lemmatize_sentence(input_string):
    # Perform lemmatization
    words = word_tokenize(input_string)
    # print("{0:20}{1:20}".format("--Word--", "--Lemma--"))
    lemmatized_sentence = reduce(lambda x, y: x + " " + wnl.lemmatize(y, pos="v"), words, "")
    return lemmatized_sentence

def lemmatize_df(df, column):
    count = 0
    try:
        for i in df.index:
            input_string = df.loc[i, column]
            output_str = lemmatize_sentence(input_string)
            df.loc[i, column] = output_str
            count = count + 1
    except Exception as inst:
        print(type(inst))  # the exception type
        print(inst.args)  # arguments stored in .args
        print(inst)         # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
        print(count)
    else:
        print("Dataframe lemmatized successfully")
        return df