import spacy

# Load the large English NLP model
nlp = spacy.load('en_core_web_sm')


# Replace a token with "REDACTED" if it is a name
def replace_name_with_placeholder(token):
    if token.ent_iob != 0 and token.ent_type_ == "PERSON":
        return "[REDACTED] "
    else:
        return token.text


def scrub(text):
    doc = nlp(text)
    with doc.retokenize() as retokenizer:
        for ent in doc.ents:
            retokenizer.merge(ent)
    tokens = map(replace_name_with_placeholder, doc)
    return "".join(tokens)


def redact(text):
    return scrub(text)
