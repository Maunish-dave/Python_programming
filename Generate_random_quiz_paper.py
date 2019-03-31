import os
import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quizNum in range(35):
    quizfile = open("capitalQuiz{}.txt".format(quizNum+1), 'w')
    answerkey = open("anskwetKey{}.txt".format(quizNum+1),'w')
    quizfile.write("Name:\nDate:\nEnroll:\n\n")
    quizfile.write("('' * 20) state quiz (form {})".format(quizNum+1))
    state = list(capitals.keys())
    random.shuffle(state)
    
    for questionNum in range(50):
        correctAnswer = capitals[state[questionNum]]
        wrongAnswer = list(capitals.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer,3)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
        quizfile.write("{}. what is captital of {}\n".format(questionNum+1,state[questionNum]))
        for i in range(4):
            quizfile.write("{}  {}\n".format('ABCD'[i],answerOptions[i]))
        quizfile.write("\n")
        
        answerkey.write("{} ans {}".format(questionNum + 1,'ABCD'[answerOptions.index(correctAnswer)]))
    quizfile.close()
    answerkey.close()
            
