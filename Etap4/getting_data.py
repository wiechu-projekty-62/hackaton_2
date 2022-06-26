import csv

def open_csv_file(filename):
    with open(filename + '.csv') as f:
        reader = csv.reader(f)
        students = list(reader)
    return students

def create_students_dict(lista):
    students = {}
    for element in lista:
        students[element[0] + element[1] + element[2]] = [element[1], element[2], element[3], element[4]]
    return students




