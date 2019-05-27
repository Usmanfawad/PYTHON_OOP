# Task3

class houses:
    def __init__(self,city,location,block,price,parking,rooms,kitchen,color):
        self.city= city
        self.location= location
        self.block=block
        self.price=price
        self.parking=parking
        self.rooms=rooms
        self.kitchen=kitchen
        self.color=color


    def house_description(self):
        print("House type: {}\nCity: {}\nLocation: {}\nBlock: {}\nPrice: {}\nParking: {}\nRooms: {}\nKitchen: {}".format(self.__class__.__name__,self.city,self.location,self.block,self.price,self.parking,self.rooms,self.kitchen) )

class appartment(houses):
    def info_appart(self,city,location,block,price,parking,rooms,kitchen,houseno,floorno,color):
        super.__init__(city,location,block,price,parking,rooms,kitchen)
        pass
    def app_change_color(self,color):
        print("Appartment color changed from {} to {}".format(self.color,color))
    def app_renewate(self):
        print("Your appartment has been renewated")


class bungalow(houses):
    def info_bungalow(self,city,location,block,price,parking,rooms,kitchen,houseno):
        super.__init__(city, location, block, price, parking, rooms, kitchen)
        pass
    def bungalow_reconstruction(self):
        print("House Reconstructed")
    def change_house_color(self,color):
        print("House color changed from {} to {}".format(self.color, color))

bungalow_1=bungalow('karachi','jauhar','12','100,000','yes','4','yes','pearl white')
bungalow_1.house_description()
bungalow_1.change_house_color('red')