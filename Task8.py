import datetime
class ordering_system:
    menu_dict={}
    date_today=datetime.datetime.today().strftime("%D")

    def __init__(self,branch_code,date,location):
        self.branch_code= branch_name
        self.date= datetime.datetime.today().strftime("%D")
        self.location= location

    @classmethod
    def login_client(cls):
        client_name=input("Enter client's name: ")
        cls.client_name=client_name
        print("\n"*10)
        print(ordering_system.date_today)
        print("------Welcome Mr",cls.client_name)
        ordering_system.welcome_screen()

    @classmethod
    def welcome_screen(cls):
        print("\n"*10)

        print("1) Add Flavours")
        print("2) Enter Customer Details")
        print("3) Place order")
        print("4) View order details")
        print("5) Logout")

        user_choice= input("Enter 1,2,3,4 or 5: ")
        while user_choice not in ['1','2','3','4','5','6']:
            print("Please enter 1,2,3,4 or 5 only!")

        if user_choice=='1':
            flavours.add_flavour_object()
            print(flavours.flavours_dict)
            user_main_menu = input("Press -M- to go back to main menu:  ")
            if user_main_menu.lower() == 'm':
                ordering_system.welcome_screen()


        elif user_choice=='2':
            ordering_system.enter_customer_details()
            user_main_menu= input("Press -M- to go back to main menu:  ")
            if user_main_menu.lower()=='m':
                ordering_system.welcome_screen()

        elif user_choice=='3':
            print("\n"*30)
            open_file=open("Flavours.txt","r")
            read=open_file.read()
            print(read)
            open_file.close()
            if read=="":
                print("\n"*20)
                print("No Pizzas available! ")
                user_main_menu = input("Press -M- to go back to main menu:  ")
                if user_main_menu.lower() == 'm':
                    ordering_system.welcome_screen()

            else:
                pizza_name=input("Enter pizza name: ")
                quantity=   input("Enter quantity  : ")
                ordering_system.place_order(pizza_name,quantity)
                user_main_menu = input("Press -M- to go back to main menu:  ")
                if user_main_menu.lower() == 'm':
                    ordering_system.welcome_screen()
        if user_choice=="4":
            pass

        if user_choice=='5':
            print("\n"*20)
            print("GOOD BYE!",cls.client_name)


    @classmethod
    def place_order(cls,pizza_name,quantity):
         pass

    @classmethod
    def enter_customer_details(cls):
        details= customer.create_customer_object()
        print("{:<20} : {}\n{:<20} : {}\n{:<20} : {}".format("Customer Name",details.name,"Customer ID",details.address,"Customer Cell No",details.cellno))

class order:
    def __init__(self,id):
        self.id=id


class customer:
    def __init__(self,name,address,cellno):
        self.name= name
        self.address= address
        self.cellno=cellno

    @classmethod
    def create_customer_object(cls):

        name=    input("Enter Customer's name:    ")
        address= input("Enter Customer's Address: ")
        cellno=  input("Enter Customer's cell-no: ")
        return cls(name,address,cellno)


class pizza:
    def __init__(self,size,price,crust_type):
        self.size=size
        self.price=price
        self.crust_type=crust_type

class flavours:
    counter=0
    flavours_dict={}
    def __init__(self,name_flavour,ingredients):
        self.name_flavour=name_flavour
        self.ingredients=ingredients
        flavours.flavours_dict[self.name_flavour] = self.ingredients

    @classmethod
    def add_flavour_object(cls):
        name_flavour = input("Enter Flavour name:    ")
        ingredients = input("Enter ingredients: ")
        flavours.counter+=1
        print(flavours.counter)
        file_read=open("Flavours.txt",'r')
        content_file=file_read.read()
        file_read.close()
        flavours_description =content_file+ str(flavours.counter) + ")" + str(name_flavour) + "-" + str(ingredients)+"\n"
        open_file = open("Flavours.txt", 'w')
        write_to_file = open_file.write(flavours_description)
        return cls(name_flavour, ingredients)


ordering_system.login_client()