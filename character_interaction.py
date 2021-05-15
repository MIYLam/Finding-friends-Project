import csv

morning_file = open("morningquestions.csv", "r")

class Questions:            #Using to 
    def __init__(self, questions):
        self.questions = questions

    def questions_reader(self):
        question_list = []
        reader = csv.reader(self.questions, delimiter=',')
        line_counter = 0
        for row in reader:
            if line_counter == 0:
                line_counter = line_counter + 1
            else:
                question_list.append(row[1])

        return question_list

morning_questions = Questions(morning_file) #These variables need to be interated throuhg a for loop 
