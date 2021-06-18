import spacy


# Load the large English NLP model
nlp = spacy.load('en_core_web_sm')


def extract(text):
    # Parse the text with spaCy. This runs the entire pipeline.
    doc = nlp(text)

    # 'doc' now contains a parsed version of text. We can use it to do anything we want!
    # For example, this will print out all the named entities that were detected:
    entities = list()

    for entity in doc.ents:
        entities.append(F"{entity.text} ({entity.label_})")

    return entities
