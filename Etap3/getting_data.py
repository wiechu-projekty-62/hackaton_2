import csv

filename = 'students.csv'


def students_list():
    try:
        with open(filename) as f:
            reader = csv.reader(f)
            students = []
            imiona_nazwiska = []
            zadania = []
            ocena = []
            for row in reader:
                students.append(row)
                imnazw = row[1] + row[2]
                imiona_nazwiska.append(imnazw)
                zad = row[3]
                zadania.append(zad)
                oc = row[4]
                ocena.append(oc)
            print(imiona_nazwiska)
    except FileNotFoundError as fnf:
        print("Error", fnf)

students_list()
