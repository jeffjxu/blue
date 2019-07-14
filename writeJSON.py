import json
import random

def randMultiChoice(answer):
    correctInd = random.randint(0, 3)
    wrongO1 = 'fetch phrase 1'
    wrongO2 = 'fetch phrase 2'
    wrongO3 = 'fetch phrase 3'
    wrongOArr = [wrongO1, wrongO2, wrongO3]
    wrongCounter = 0
    letterArr = ['A', 'B', 'C', 'D']
    choiceArr = []
    for i in range(4):
        if i == correctInd:
            choiceArr.append(answer)
        else:
            choiceArr.append(wrongOArr[wrongCounter])
            wrongCounter += 1
    correctLetter = letterArr[correctInd]
    return (correctLetter, choiceArr)

question1 = 'question1'
answer1 = "answer1"
q1Letter, q1o = randMultiChoice(answer1)

question2 = 'question2'
answer2 = 'answer2'
q2Letter, q2o = randMultiChoice(answer2)

question3 = 'question3'
answer3 = 'True'

question4 = 'question4'
answer4 = 'answer4'
q4Letter, q4o = randMultiChoice(answer4)

question5 = 'question5'
answer5 = 'False'


with open('skill-Language-Teacher.json') as json_file:
    data = json.load(json_file)
    for node in data['dialog_nodes']:
        if (node['title'] == 'Multiple Choice 1'):
            node['output']['generic'][0]['title'] = question1
            for option in node['output']['generic'][0]['options']:
                if option['label'] == q1Letter:
                    option['value']['input']['text'] = 'This is right'
                elif option['label'] != q1Letter:
                    option['value']['input']['text'] = 'This is wrong'
                if option['label'] == 'A':
                    option['label'] = q1o[0]
                elif option['label'] == 'B':
                    option['label'] = q1o[1]
                elif option['label'] == 'C':
                    option['label'] = q1o[2]
                elif option['label'] == 'D':
                    option['label'] = q1o[3]
                '''for option in node['output']['generic'][0]['options']:
                    print((option['label'] + option['value']['input']['text'] + '\n'))'''
        elif (node['title'] == 'Multiple Choice 2'):
            node['output']['generic'][0]['title'] = question2
            for option in node['output']['generic'][0]['options']:
                if option['label'] == q2Letter:
                    option['value']['input']['text'] = 'This is right'
                elif option['label'] != q2Letter:
                    option['value']['input']['text'] = 'This is wrong'
                if option['label'] == 'A':
                    option['label'] = q2o[0]
                elif option['label'] == 'B':
                    option['label'] = q2o[1]
                elif option['label'] == 'C':
                    option['label'] = q2o[2]
                elif option['label'] == 'D':
                    option['label'] = q2o[3]
        elif (node['title'] == 'True/False 3'):
            node['output']['generic'][0]['title'] = question3
            for option in node['output']['generic'][0]['options']:
                if option['label'] == answer3:
                    option['value']['input']['text'] = 'This is right'
                elif option['label'] != answer3:
                    option['value']['input']['text'] = 'This is wrong'
        elif (node['title'] == 'Multiple Choice 4'):
            node['output']['generic'][0]['title'] = question1
            for option in node['output']['generic'][0]['options']:
                if option['label'] == q2Letter:
                    option['value']['input']['text'] = 'This is right'
                elif option['label'] != q2Letter:
                    option['value']['input']['text'] = 'This is wrong'
                if option['label'] == 'A':
                    option['label'] = q4o[0]
                elif option['label'] == 'B':
                    option['label'] = q4o[1]
                elif option['label'] == 'C':
                    option['label'] = q4o[2]
                elif option['label'] == 'D':
                    option['label'] = q4o[3]
        elif (node['title'] == 'True/False 5'):
            node['output']['generic'][0]['title'] = question5
            for option in node['output']['generic'][0]['options']:
                if option['label'] == answer5:
                    option['value']['input']['text'] = 'This is right'
                elif option['label'] != answer5:
                    option['value']['input']['text'] = 'This is wrong'
        elif (node['title'] == 'Show answer 1'):
            node['output']['generic'][0]['values'][0]['text'] = ('The correct answer is ' + answer1)
        elif (node['title'] == 'Show answer 2'):
            node['output']['generic'][0]['values'][0]['text'] = ('The correct answer is ' + answer2)
        elif (node['title'] == 'Show answer 4'):
            node['output']['generic'][0]['values'][0]['text'] = ('The correct answer is ' + answer4)

'''
dbPrint = json.dumps(data, sort_keys=True, indent=2, separators=(',', ':'))
print(dbPrint)

with open('new.json', 'w') as outfile:
    json.dump(data, outfile, indent=2)'''
