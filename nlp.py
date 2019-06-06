import nltk
from crawl import get_movie_targets, get_synopsis_from_imdb_id
from sklearn.feature_extraction.text import CountVectorizer

def tokenize_text(text):
    return nltk.word_tokenize(text)

def get_noun_tokens(tokens):
    target_pos = ['FW', 'NN', 'NNS', 'NNP', 'NNPS']
    pos_tag = nltk.pos_tag(tokens)
    return [token[0] for token in pos_tag if token[1] in target_pos]

def cut_by_frequency(tokens, criterion):
    result = {}
    for token in tokens:
        if token in result:
            result[token] += 1
        else:
            result[token] = 1
    filtered_result = list(filter(lambda x: x[1] > 5, result.items()))
    return sorted(filtered_result, key=lambda x: x[1],reverse=True)

def make_document(text):
    tokens = tokenize_text(text)
    noun_tokens = get_noun_tokens(tokens)
    noun_tokens = cut_by_frequency(noun_tokens, 8)
    return ' '.join([elem[0] for elem in noun_tokens])

