import spacy

nlp = spacy.load("en_core_web_lg")

def label_txt(txt):
  return nlp(txt)
