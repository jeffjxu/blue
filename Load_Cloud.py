#
#
# main() will be run when you invoke this action
#
# @param Cloud Functions actions accept a single parameter, which must be a JSON object.
#
# @return The output of this action, which must be a JSON object.
#
#
import sys

# CLOUDANT REFERENCE - BLUE BAGUETTE #
# HANS STOETZER #

from cloudant.client import Cloudant
from cloudant.result import Result, ResultByKey
import json
import random

def get_db_entries(n):
    rand = random.randint(0,5804)
    return result_collection[rand:rand + n]
    
def make_pos_text(entry):
    nounsdict = entry['doc']['Nouns']
    verbsdict = entry['doc']['Verbs']
    sentence = ''
    if (len(nounsdict) == 0):
        sentence += 'There are no nouns in this phrase. '
    else:
        sentence += 'The nouns in the phrases are ' + nounsdict + '.'
    if (len(verbsdict) == 0):
        sentence += ' There are no verbs in this phrase.'
    else:
        sentence += ' The verbs in this phrase are '+ verbsdict + '.'

    return sentence
    
def randMultipleChoice(answer, ind, result_collection):
    correctInd = random.randint(0, 3)
    choiceArr = []
    wrongInd = ind + random.randint(5, 5804-ind-10)
    phrases = result_collection[wrongInd: wrongInd+3]
    db = {}
    for i in range(3):
        db[str(i+1)] = phrases[i]
    wrongO1 = db["1"]["doc"]["Original_Text"]
    wrongO2 = db["2"]["doc"]["Original_Text"]
    wrongO3 = db["3"]["doc"]["Original_Text"]
    wrongArr = [wrongO1, wrongO2, wrongO3]
    wrongCounter = 0
    for i in range(4):
        if i == correctInd:
            choiceArr.append(answer)
        else:
            choiceArr.append(wrongArr[wrongCounter])
            wrongCounter += 1
    return correctInd, choiceArr

    
def setVal(n, c):
    if n == c:
        return "this is right"
    else:
        return "this is wrong"

def main(dict):
    # CREDENTIALS #
    # THESE ARE ADMIN CREDENTIALS WITH ALL PERMISSIONS ENABLED.....NO PRESSURE #
    
    USERNAME = "ef15632f-93ee-4c1d-adbc-57c18369feae-bluemix"
    PASSWORD = "1124dcfb3c559ffd80306c960ea3fc7cf74814902493828c5bf47f3c3de88b02"
    ACCOUNT_NAME = "ef15632f-93ee-4c1d-adbc-57c18369feae-bluemix"
    
    # Use Cloudant to create a Cloudant client using account #
    
    client = Cloudant(USERNAME, PASSWORD, account=ACCOUNT_NAME, connect=True, auto_renew=True)
    
    # Perform client tasks by establishing a session #
    
    session = client.session()
    database = client['master_dataset_v1']
    result_collection = Result(database.all_docs, include_docs=True)
    rand = random.randint(0,5804)
    db = {}
    phrases = result_collection[rand:rand + 5]
    for i in range(5):
        db[str(i+1)] = phrases[i]
    print(db)
    
    #creating information about the phrases
    phrE1=db["1"]['doc']['Original_Text']
    phrF1=db["1"]['doc']['Translation']
    phrase1 = "Our phrase is " + phrF1 + " , it means " + phrE1 + " in English. Would you like to see the part of speech of each word or the definition of each word? You can also move on to the next phrase"
    aud1=db["1"]['doc']['Translation']
    #print(phrF1)
    pos1 = make_pos_text(db["1"])
    
    phrE2=db["2"]['doc']['Original_Text']
    phrF2=db["2"]['doc']['Translation']
    phrase2 = "Our phrase is " + phrF2 + " , it means " + phrE2 + " in English. Would you like to see the part of speech of each word or the definition of each word? You can also continue to the next phrase"
    aud2=db["2"]['doc']['Translation']
    pos2 = make_pos_text(db["2"])
    
    phrE3=db["3"]['doc']['Original_Text']
    phrF3=db["3"]['doc']['Translation']
    phrase3 = "Our phrase is " + phrF3 + " , it means " + phrE3 + " in English. Would you like to see the part of speech of each word or the definition of each word? You can also type continue for the next phrase"
    aud3=db["3"]['doc']['Translation']
    pos3 = make_pos_text(db["3"])
    
    phrE4=db["4"]['doc']['Original_Text']
    phrF4=db["4"]['doc']['Translation']
    phrase4 = "Our phrase is " + phrF4 + " , it means " + phrE4 + " in English. Would you like to see the part of speech of each word or the definition of each word? Type continue or next to move on"
    aud4=db["4"]['doc']['Translation']
    pos4 = make_pos_text(db["4"])
    
    phrE5=db["5"]['doc']['Original_Text']
    phrF5=db["5"]['doc']['Translation']
    phrase5 = "Our phrase is " + phrF5 + " , it means " + phrE5 + " in English. Would you like to see the part of speech of each word or the definition of each word?"
    aud5=db["5"]['doc']['Translation']
    pos5 = make_pos_text(db["5"])
    
    #creating the first question
    #Question 1: what does -insert phrase- mean in English?
    #Multiple Choice: each is an English phrase from the database
    question1="Question 1: what does " + phrF1 + " mean in English?"
    q1cPhrase = phrE1
    q1c, q1choice = randMultipleChoice(q1cPhrase, rand, result_collection)
    q1o1val = setVal(0, q1c)
    q1o2val = setVal(1, q1c)
    q1o3val = setVal(2, q1c)
    q1o4val = setVal(3, q1c)
    q1oArr = [q1o1val, q1o2val, q1o3val, q1o4val]
    
    #creating the second question
    #Question 2: what part of speech is this word, -insert word-?
    #Multiple Choice: Noun Verb
    #print(db["2"]['doc'])
    #print("DEBUG!")
   # print(db["2"]['doc']['Nouns'])
    secondstrN = db["2"]['doc']['Nouns']
    secondstrV = db["2"]['doc']['Verbs']
    
    nounlist = secondstrN.split(",")
    verblist = secondstrV.split(",")
    #print("DEBUG!")
    #print(nounlist[0])
    choosePos = random.randint(0,1)
    #0 : nounlist
    #1 : verblist
    #2 : neither
    if choosePos == 0 and nounlist == []:
        choosePos = 1
    elif choosePos == 1 and verblist == []:
        choosePos = 0
    elif nounlist == [] and verblist == []:
        #should not go into here
        choosePos = 2
        
    if choosePos == 0:
        word = random.choice(nounlist)
        q2cPhrase = "Noun"
    elif choosePos == 1:
        word = random.choice(verblist)
        q2cPhrase = "Verb"
    else:
        word = "aimer"
        choosePos = 1
        q2cPhrase = "Verb"
        
    question2 = "Question 2: Is " + word + " a Noun or a Verb?"
        
    q2choice = ["Noun", "Verb"]
    
    q2valNoun = setVal(0, choosePos)
    q2valVerb = setVal(1, choosePos)
    q2oArr = [q2valNoun, q2valVerb]
    
    
    #creating the third question
    #Question 3: what is -insert french word- in English?
    #Multiple Choice: each is an English word (either all noun or all adj)
    thirdstrN = db["3"]['doc']['Nouns']
    thirdstrV = db["3"]['doc']['Verbs']
    
    nounlist3 = thirdstrN.split(",")
    verblist3 = thirdstrV.split(",")
    #print("DEBUG!")
    #print(nounlist[0])
    choosePos3 = random.randint(0,1)
    #0 : nounlist
    #1 : verblist
    #2 : neither
    if choosePos3 == 0 and nounlist3 == []:
        choosePos3 = 1
    elif choosePos3 == 1 and verblist3 == []:
        choosePos3 = 0
    elif nounlist3 == [] and verblist3 == []:
        #should not go into here
        choosePos3 = 2
        
    if choosePos3 == 0:
        word3 = random.choice(nounlist3)
        q3cPhrase = "Noun"
    elif choosePos3 == 1:
        word3 = random.choice(verblist3)
        q3cPhrase = "Verb"
    else:
        word3 = "aimer"
        choosePo3s = 1
        q3cPhrase = "Verb"
        
    question3 = "Question 3: Is " + word3 + " a Noun or a Verb?"
        
    q3choice = ["Noun", "Verb"]
    
    q3valNoun = setVal(0, choosePos3)
    q3valVerb = setVal(1, choosePos3)
    q3oArr = [q3valNoun, q3valVerb]
    
    #creating the fourth question
    #Question 4: fill in the blank: -insert french phrase with one word removed-
    #Multiple Choice: one option is the word removed, other options are random
    q4nouns = (db["4"]['doc']['Nouns']).split(",")
    q4verbs = (db["4"]['doc']['Verbs']).split(",")
    q4allwords = q4nouns + q4verbs 
    grabWord = random.choice(q4allwords)
    manipulate4 = phrF4
    fillinblank4 = manipulate4.replace(grabWord, "_______")
    #print(fillinblank4)
    
    q4choices = []
    q4choices.append(grabWord)
    
    q1_nouns = (db["1"]['doc']['Nouns']).split(",")
    q1_verbs = (db["1"]['doc']['Verbs']).split(",")
    q2_nouns = (db["2"]['doc']['Nouns']).split(",")
    q2_verbs = (db["2"]['doc']['Verbs']).split(",")
    q3_nouns = (db["3"]['doc']['Nouns']).split(",")
    q3_verbs = (db["3"]['doc']['Verbs']).split(",")
    q5_nouns = (db["5"]['doc']['Nouns']).split(",")
    q5_verbs = (db["5"]['doc']['Verbs']).split(",")
    rand_words = q1_nouns + q1_verbs + q2_nouns + q2_verbs + q3_nouns + q3_verbs + q5_nouns + q5_verbs
    
    for i in range(3):
        f = True
        while (f):
            potWord = random.choice(rand_words)
            if potWord not in q4choices:
                q4choices.append(potWord)
                f = False
                

    random.shuffle(q4choices)
    q4c = q4choices.index(grabWord)
    
    q4o1val = setVal(0, q4c)
    q4o2val = setVal(1, q4c)
    q4o3val = setVal(2, q4c)
    q4o4val = setVal(3, q4c)
    q4oArr = [q4o1val, q4o2val, q4o3val, q4o4val]
    q4cPhrase = grabWord
    question4="Question 4: fill in the blank: " + fillinblank4
    

    
    
    
    
    
    
    #creating the fifth question
    #Question 5: True or False : This phrase "-insert french phrase-"" is in the
    #category, "-insert intent-"
    #True/False
    category = db["5"]['doc']['Category']
    other1 = db["1"]['doc']['Category']
    other2 = db["2"]['doc']['Category']
    other3 = db["3"]['doc']['Category']
    other4 = db["4"]['doc']['Category']
    
    otherOptions = []
    if other1 != category: otherOptions.append(other1)
    if other2 != category: otherOptions.append(other2)
    if other3 != category: otherOptions.append(other3)
    if other4 != category: otherOptions.append(other4)
    
    chooseCat = random.randint(0,1)
    #0 : False
    #1 : True
    if chooseCat == 0 and otherOptions == []:
        chooseCat = 1
    
    if chooseCat == 0:
        catchosen = random.choice(otherOptions)
    else:
        catchosen = category
    
    question5 = "Question 5: True or False : This phrase "+ phrF5 +" is in the category, "+ catchosen + "."
        
    q5choice = ["False", "True"]
    
    q5valFalse = setVal(0, chooseCat)
    q5valTrue = setVal(1, chooseCat)
    q5oArr = [q5valFalse, q5valTrue]
    
    
    
    RET = {}
    
    #populating the dictionary with phrases for the lesson
    RET["phrase1"] = phrase1
    RET["aud1"] = aud1
    RET["pos1"] = pos1
    
    RET["phrase2"] = phrase2
    RET["aud2"] = aud2
    RET["pos2"] = pos2
    
    RET["phrase3"] = phrase3
    RET["aud3"] = aud3
    RET["pos3"] = pos3
    
    RET["phrase4"] = phrase4
    RET["aud4"] = aud4
    RET["pos4"] = pos4
    
    RET["phrase5"] = phrase5
    RET["aud5"] = aud5
    RET["pos5"] = pos5
    
    #populating the dictionary with the first question 
    RET["question1"] = question1
    RET["q1c"] = q1c
    RET['q1cPhrase'] = q1cPhrase
    RET['q1choice'] = q1choice
    RET['q1oArr'] = q1oArr
    
    #populating the dictionary with the second question 
    RET["question2"] = question2
    RET["q2c"] = choosePos
    RET["q2cPhrase"] = q2cPhrase
    RET["q2choice"] = q2choice
    RET["q2oArr"] = q2oArr
    
    #populating the dictionary with the third question 
    RET["question3"] = question3
    RET["q3c"] = choosePos3
    RET["q3cPhrase"] = q3cPhrase
    RET["q3choice"] = q3choice
    RET["q3oArr"] = q3oArr
    
    
    #populating the dictionary with the fourth question 
    RET["question4"] = question4
    RET["q4c"] = q4c
    RET['q4cPhrase'] = q4cPhrase
    RET['q4choice'] = q4choices
    RET['q4oArr'] = q4oArr
    
    #populating the dictionary with the second question 
    RET["question5"] = question5
    RET["q5c"] = chooseCat
    RET["q5cPhrase"] = phrF5
    RET["q5choice"] = q5choice
    RET["q5oArr"] = q5oArr
    
    
    
    #print(RET)
    
    return RET
    #returnvar = result_collection[0][0]
    #print(returnvar['doc']['Original_Text'])
    #client.disconnect()
    
    #return returnvar
    


