import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

def display_ner_results(text: str):
  doc = nlp(text)
  
  displacy.serve(doc, style="ent")
