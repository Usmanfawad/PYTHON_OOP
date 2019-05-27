class plants:
    def __init__(self,name,type,id):
        self.name=name
        self.type=type
        self.id=id

    def plants_interface():
        print(u"\u25C9"*14)
        print("Welcome to XYZ Farm")
        print(u"\u25C9" * 14)
        print("\n")
        print("Choose the action you wish to proceed with! ")
        print("1) Add Edible plants\n2) Add Non Edible plants\n3) View all farm plants")

        user_input= input("Enter the corresponding numbers to proceed further- ")
        if user_input=='1':
            edible_object=edible_plants.create_ediblefruit_object()
            print('\n\n')
            print("You added {} {}s in the farm.".format(edible_object.quantity_plant,edible_object.name_plant))


class edible_plants:
    mango_price=   70
    apple_price=   50
    banana_price=  30
    tomatoe_price= 20
    def __init__(self,name_plant,quantity_plant):
        self.name_plant=     name_plant
        self.quantity_plant= quantity_plant

    @classmethod
    def create_ediblefruit_object(cls):
        print(">>>FRUITS YOU CAN ADD TO THE FARM<<<")
        print("1) Mango\n2) Apple\n3) Banana\n4) Tomatoe")
        print("Please choose the corresponding number for the fruit you wish to add-\n\n")
        name_plant=     input("Enter the fruit you wish to add in your farm: ")
        quantity_plant= input("Enter quantity of the plant you added:             ")
        if name_plant.lower()=='mango':
            print("The total cost of {} you added to the farm is {}Rs/- ".format(name_plant, (int(quantity_plant) * int(edible_plants.mango_price))))
        elif name_plant.lower()=='apple':
            print("The total cost of {} you added to the farm is {}Rs/- ".format(name_plant, (int(quantity_plant) * int(edible_plants.apple_price))))
        elif name_plant.lower()=='banana':
            print("The total cost of {} you added to the farm is {}Rs/- ".format(name_plant, (int(quantity_plant) * int(edible_plants.banana_price))))
        elif name_plant.lower()=='tomatoe':
            print("The total cost of {} you added to the farm is {}Rs/- ".format(name_plant, (int(quantity_plant)*  int(edible_plants.tomatoe_price))))
        else:
            print("Sorry, the fruit you're trying to add does not grow in our farm! ")

        return cls(name_plant,quantity_plant)

plants.plants_interface()