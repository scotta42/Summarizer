import spacy
import textacy.extract
from pathlib import Path

# Load the large English NLP model
nlp = spacy.load('en_core_web_sm')


def fact_extract(text, entity):
    # Parse the document with spaCy
    doc = nlp(text)
    # Extract semi-structured statements
    subjects = [" ", " "]+entity.split(' ')
    for word in subjects:
        if word != " ":
            statements = textacy.extract.semistructured_statements(doc, "London")
    # Print the results
    fact_list = list()
    fact_list.append("Here are the things I know about london:")

    for statement in statements:
        subject, verb, fact = statement
        fact_list.append(f" - {fact}")
    return fact_list
