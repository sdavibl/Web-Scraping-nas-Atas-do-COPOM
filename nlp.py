import re
import spacy
import pandas as pd
import numpy as np

def lemmetizador(string):
    nlp = spacy.load("pt_core_news_lg")
    def lemmetizar(string):
        string = re.sub("[^A-zÀ-ú0-9]+", ' ', string).lower()
        desabilitar = ["parser", "ner", "tagger", "entity_linker", "entity_ruler", "textcat", "textcat_multilabel", "trainable_lemmatizer",
              "senter", "sentencizer", "transformer"]
        doc = nlp.pipe(string, disable=desabilitar)
        return " ".join([token.lemma_ for token in doc if not token.is_stop])