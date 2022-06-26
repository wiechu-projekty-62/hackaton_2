import getting_data as gd

def prepare_email(your_choice):
    if your_choice == 'y':
        new_name = input("Give the student's surname you are looking for: ").capitalize()
        if new_name == '':
            print("Error")
        generate_searching = search_name(new_name, students_list)
        return generate_searching

def search_name(name, students):
    lista = []
    for key, value in students.items():
        if name in key:
            lista.append(value)
    print(lista)
    return lista
def mess(na, ta, gr):
    message = "Hi {},\nThis is a reminder that you have {} tasks left to\
    submit before you can graduate. Your current grade is {} and can increase\
    to {} if you submit all assignments before the due date 15.06.2022.\n"

    print(message.format(na, ta, gr, int(gr) + 1))

if __name__ == "__main__":
    groups = ['3A', '3C']
    print("*****Message generator for the selected student*****")
    print("Possible classes:".center(50))
    for classes in groups:
        print('*****', classes, '*****')
    try:
        groupfile = input("Select group of students:".center(50))
        open_group_file = gd.open_csv_file(groupfile)
        students_list = gd.create_students_dict(open_group_file)
        print("Look for: student -- press -- y or Y")
        your_choice_ = input("").lower()
        try:
            generate_new_search = prepare_email(your_choice_)
            na = generate_new_search[0][0]
            ta = generate_new_search[0][2]
            gr = generate_new_search[0][3]
            mess(na, ta, gr)
        except Exception as e:
            print('Error', e)
    except FileNotFoundError as fn:
        print("Error", fn)


else:
    print('The file was imported as a module')