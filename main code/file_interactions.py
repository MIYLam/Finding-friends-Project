from csv import reader
from random import randint
from time_counter import *

time_of_day = "morning"
class Questions:            #Using to 
    def __init__(self, used_questions):
        self.question_list = []
        self.used_question = used_questions
        self.file_contents = []
        self.dialogue_options = []
        with open(time_of_day + "questions.csv", "r") as morning_file:
            read_file = reader(morning_file, delimiter=',')
            for row in read_file:
                self.file_contents.append(row)

        self.questions_reader()
        self.question_selector()
        self.dialogue_list()
        self.dialogue_type()

    def questions_reader(self):
        line_counter = 0
        print(self.used_question) 
        for row in self.file_contents:
            if line_counter == 0:
                line_counter = line_counter + 1
            else:
                self.question_list.append(row[0])
        for word in self.question_list:
            if word in self.used_question:
                self.question_list.remove(word)
        print(self.question_list)
                


    
    def question_selector(self):
        list_number = randint(0, len(self.question_list)-1)
        self.selected_question = self.question_list[list_number]





    def dialogue_list(self):

        line_counter = 0
        for row in self.file_contents:
            if row[0] != self.selected_question:
                line_counter = line_counter + 1
            else:
                self.dialogue_options.extend([row[1],row[3],row[5]])
        
      
    
    def dialogue_type(self):            
        self.dialogue_types = {}
        line_counter = 0
        for row in self.file_contents:
            if row[0] != self.selected_question:
                line_counter = line_counter + 1
            else:
                for answer in range(1,6):
                    if answer%2 == 0:
                        pass 
                    else:
                        self.dialogue_types[row[answer]] = row[answer+1]                       




