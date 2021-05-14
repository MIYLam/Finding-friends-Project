import csv
from character_interaction import answer_reader


def profile_manipulation(charac):
    csv_reader = csv.reader(charac, delimiter=',')
    