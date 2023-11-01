from functools import reduce
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

def stem_sentence(input_string):
    words = word_tokenize(input_string)
    # using reduce to apply stemmer to each word and join them back into a string
    stemmed_sentence = reduce(lambda x, y: x + " " + ps.stem(y), words, "")
    return stemmed_sentence

def stem_df(reviews_df, column):
    try:
        for i in reviews_df.index:
            input_string = reviews_df.loc[i, column]
            output_str = stem_sentence(input_string)
            reviews_df.loc[i, column] = output_str
    except Exception as inst:
        print(type(inst))  # the exception type
        print(inst.args)  # arguments stored in .args
        print(inst)         # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
    else:
        print("Dataframe stemmed successfully")

# sentence = "Programmers program with programming languages"
# words = word_tokenize(sentence)
# # using reduce to apply stemmer to each word and join them back into a string
# stemmed_sentence = reduce(lambda x, y: x + " " + ps.stem(y), words, "")
#
# print(stemmed_sentence)




# import nltk
# nltk.download()
# from nltk.corpus import brown
# print(brown.words())