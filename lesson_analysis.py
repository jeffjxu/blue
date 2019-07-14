# HANS STOETZER
# PROJECT BLUE BAGUETTE 2019
# NLP BACKEND FEATURES USED TO POPULATE MASTER DATASET

import json
import random
import spacy
import pandas as pd
from pandas.io.json import json_normalize
from ibm_watson import NaturalLanguageUnderstandingV1, LanguageTranslatorV3, TextToSpeechV1
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions, SentimentOptions
import IPython.display as ipd

# WATSON NLU CONSTRUCTOR
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version = "2018-11-16",
    iam_apikey = "API_KEY",
    url = "https://gateway.watsonplatform.net/natural-language-understanding/api"
)

# WATSON TRANSLATOR CONSTRUCTOR
language_translator = LanguageTranslatorV3(
    version = "2018-05-01",
    iam_apikey = "API_KEY",
    url = "https://gateway.watsonplatform.net/language-translator/api"
)

# WATSON TEXT TO SPEECH CONSTRUCTOR
text_to_speech = TextToSpeechV1(
    iam_apikey = "API_KEY",
    url = "https://stream.watsonplatform.net/text-to-speech/api"
)

# LOAD SPACY FR MODEL
nlp = spacy.load("fr")

# LOAD SHOW DATASET
show_dataset = pd.read_csv("friends.csv", index_col=0)

def generate_random_phrase():
    return show_dataset["Lines"][random.randint(0,len(show_dataset))]
  
def translate(text):
    translation = language_translator.translate(
        text = text, 
        model_id = "en-fr"
    ).get_result()
    
    return translation["translations"][0]["translation"]

def categories(text):
    response = natural_language_understanding.analyze(
        text = text, 
        features = Features(
            categories = CategoriesOptions(limit=1) 
        )).get_result()
    
    return json.dumps(response["categories"])

def sentiment(text):
    response = natural_language_understanding.analyze(
        text = text, 
        features = Features(
            sentiment = SentimentOptions(document=True)
        )).get_result()
    
    return json.dumps(response["sentiment"])

def syntax(text):
    doc = nlp(text)
    
    df = pd.DataFrame(columns=("Original Text","Lemma","POS Coarse", "POS Fine","Dependency Relation"))

    for token in doc:
        df.loc[token] = [token.text, token.lemma_, token.pos_, token.tag_, token.dep_]

    df = df.reset_index(drop=True)
    
    return df

def nouns(text):
    df = syntax(text)
    nouns = df.loc[df["POS Coarse"] == "NOUN"]
    return set(nouns["Lemma"])

def verbs(text):
    df = syntax(text)
    verbs = df.loc[df["POS Coarse"] == "VERB"]
    verbs = list(verbs["Lemma"])

    aux = df.loc[df["POS Coarse"] == "AUX"]
    aux = list(aux["Lemma"])

    verbs = verbs + aux
    return set(verbs)

# DEMO #

# RANDOM DIALOGUE FROM SCRIPT # 
random_text = generate_random_phrase()
print(random_text)

# TRANSLATED DIALOGUE #
translation = translate(random_text)
print(translation)

# SENTIMENT #
sentiment_data = sentiment(translated_text)
print(sentiment_data)

# CATEGORIES #
category_data = categories(translated_text)
print(category_data)

# NOUNS #
noun_list = nouns(translated_text)
print(noun_list)

# VERB LIST #
verb_list = verbs(translated_text)
print(verb_list)

# SYNTAX #
syntax_data = syntax(translated_text)
syntax_data

# END DEMO #

# UNIMPLEMENTED FEAUTURES #

# DEPENDENCY DIAGRAM #

doc = nlp(translated_text)

spacy.displacy.render(doc, style="dep")

# WATSON PRONUNCIATION #

# WATSON TEXT TO SPEECH -> TEMP FILE
with open('temp.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            translated_text,
            voice='fr-FR_ReneeV3Voice',
            accept='audio/mp3'        
        ).get_result().content)
audio_file.close()

# WATSON PLAYBACK
ipd.Audio("temp.mp3")

