import spacy
from spacy.lang.en.stop_words import STOP_WORDS


def word_frequencies(docx, stopwords):
    word_frequencies = {}
    for word in docx:
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] +=1
    return word_frequencies


def sentence_tokenization(docx, stopwords, maximum_frequency, word_freq):
    sentence_list = [sentence for sentence in docx.sents]
    sentence_scores = {}
    for sent in sentence_list:
        for word in sent:
            if word.text.lower() in word_freq.keys():
                if len(sent.text.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_freq[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_freq[word.text.lower()]
    from heapq import nlargest
    summarized_sentences = nlargest(7,sentence_scores, key=sentence_scores.get)
    final_sentences = [w.text for w in summarized_sentences]
    summary = ' '.join(final_sentences)
    return summary


def summarize(text1):
    # from string import punctuation
    # document1 = open('London.txt')
    # text1 = document1.read()
    # Text Preprocessing + Tokenization
    stopwords = list(STOP_WORDS)
    # len(stopwords)
    nlp = spacy.load("en_core_web_sm")
    docx = nlp(text1)
    # for token in docx:
    #    print(token.text)
    word_freq = word_frequencies(docx, stopwords)
    maximum_frequency = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = (word_freq[word]/maximum_frequency)
    return sentence_tokenization(docx, stopwords, maximum_frequency, word_freq)


#summarize()
# word_frequencies()