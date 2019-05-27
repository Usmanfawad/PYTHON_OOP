import datetime
class main_interface:

    office_id= 'UIT-002'
    date_today = datetime.datetime.today().strftime("%D")

    def __init__(self,doffice_id):
        self.date = datetime.datetime.today().strftime("%D")
        self.id=office_id


    def show_interface():
        print("\n"*30)
        print("<<<UIT ADMISSION OFFICE INTERFACE>>>")
        print("Date:",main_interface.date_today)
        print("\n")
        print("1) Register new Student.\n2) Add discipline.\n3) Add courses.\n4) View all disciplines.\n5) View all courses.\n6) Quit.")
        user_input=input("Enter the corresponding number to proceed: ")
        if user_input=='1':
            print("\n"*30)
            student.create_student_object()
            user_main_menu = input("Press -M- to go back to main menu:  ")
            if user_main_menu.lower() == 'm':
                main_interface.show_interface()
        elif user_input=='2':
            print("\n"*30)
            disciplines.create_discipline_object()
            user_main_menu = input("Press -M- to go back to main menu:  ")
            if user_main_menu.lower() == 'm':
                main_interface.show_interface()
        elif user_input=='3':
            print("\n"*30)
            courses.create_courses_object()
            user_main_menu = input("Press -M- to go back to main menu:  ")
            if user_main_menu.lower() == 'm':
                main_interface.show_interface()
        elif user_input=='4':
            print("\n"*30)
            file_read = open("discipline.txt", 'r')
            content_file = file_read.read()
            print(content_file)
            file_read.close()
            user_main_menu = input("Press -M- to go back to main menu:  ")
            if user_main_menu.lower() == 'm':
                main_interface.show_interface()
        elif user_input=='5':
            print("\n"*30)
            file_read_1 = open("courses.txt", 'r')
            content_file_1 = file_read_1.read()
            print(content_file_1)
            file_read_1.close()
            user_main_menu = input("Press -M- to go back to main menu:  ")
            if user_main_menu.lower() == 'm':
                main_interface.show_interface()
        elif user_input=='6':
            pass


class student:
    def __init__(self,name,dob,cellno,cnic,address):
        self.name=   name
        self.dob=    dob
        self.cellno= cellno
        self.cnic=   cnic
        self.address=address
    @classmethod
    def create_student_object(cls):
        default_id= 1
        name=    input("Enter student's name                      | ")
        dob = input("Enter student's DOB in the format dd-mm-yy| ")
        cellno=  input("Enter student's cell no                   | ")
        cnic =   input("Enter student's cnic no                   | ")
        if len(cnic) != 13:
            cnic=input("Please Enter 13 characters only           | ")
        address= input("Enter student's address                   | ")
        default_id+=1
        print(default_id)
        return cls(name,dob,cellno,cnic,address)

class disciplines:
    counter_1 = 1
    def __init__(self,discipline_name):
        self.disciplines_name=discipline_name
    @classmethod
    def create_discipline_object(cls):

        discipline_name=input("Enter the name of discipline you wish to add: ")
        file_read = open("discipline.txt", 'r')
        content_file = file_read.read()
        file_read.close()
        disciplines_description = content_file +str(disciplines.counter_1)+") "+ str(discipline_name)+ "\n"
        open_file = open("discipline.txt", 'w')
        write_to_file = open_file.write(disciplines_description)
        disciplines.counter_1+=1
        return cls(discipline_name)

class courses:
    counter_2=1
    def __init__(self,course_name):
        self.course_name=course_name
    @classmethod
    def create_courses_object(cls):
        course_name = input("Enter the name of course you wish to add: ")
        file_read_1 = open("courses.txt", 'r')
        content_file_1 = file_read_1.read()
        file_read_1.close()
        courses_description = content_file_1 + str(courses.counter_2) + ") " + str(course_name) + "\n"
        open_file_1 = open("courses.txt", 'w')
        write_to_file_1 = open_file_1.write(courses_description)
        courses.counter_2 += 1
        return cls(course_name)


main_interface.show_interface()