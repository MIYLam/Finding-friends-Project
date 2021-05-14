import csv

morning_questions = open("morningquestions.csv", "r")

class Questions:
    def __init__(self, question_csv):
        self.question_csv = question_csv

    def questions_reader(self):
        question_list = []
        reader = csv.reader(self.question_csv, delimiter=',')
        line_counter = 0
        for row in reader:
            if line_counter == 0:
                line_counter = line_counter + 1
                pass
            else:
                question_list.append(row[1])

        return question_list

morning = Questions(morning_questions)