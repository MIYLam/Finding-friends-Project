from csv import reader
from random import randint
from time_counter import *

time_of_day = "morning"
class Questions:            #Using to 
    def __init__(self, file_content):
        self.questions = file_content

    def questions_reader(self):
        question_list = []
        line_counter = 0
        for row in self.questions:
            if line_counter == 0:
                line_counter = line_counter + 1
            else:
                question_list.append(row[0])

        return question_list

class Question_selection:
    def __init__(self, question_list):
        self.question_list = question_list
    
    def question_selector(self):
        list_number = randint(0, len(self.question_list)-1)
        selected_question = self.question_list[list_number]

        return selected_question


#class that handles dialogue 
class Dialogue: 
    def __init__(self, csv_file):
        self.file = csv_file

    def dialogue_list(self, question):
        dialogue_options = []
        line_counter = 0
        for row in self.file:
            if row[0] != question:
                line_counter = line_counter + 1
            else:
                dialogue_options.extend([row[1],row[3],row[5]])
        
        return dialogue_options       
    
    def dialogue_type(self, question):            
        dialogue_types = {}
        line_counter = 0
        for row in self.file:
            if row[0] != question:
                line_counter = line_counter + 1
            else:
                for answer in range(1,6):
                    if answer%2 == 0:
                        pass 
                    else:
                        dialogue_types[row[answer]] = row[answer+1]                       
        return dialogue_types

                           

file_contents = []
with open(time_of_day + "questions.csv", "r") as morning_file:
    read_file = reader(morning_file, delimiter=',')
    for row in read_file:
        file_contents.append(row)




dialogue_questions =  Questions(file_contents).questions_reader() #These variables need to be interated throuhg a for loop        
chosen_question = Question_selection(dialogue_questions).question_selector()
current_dialogue = Dialogue(file_contents).dialogue_list(chosen_question)