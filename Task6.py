class company:
    type_1_dict={}
    def __init__(self,name,id,address):
        self.name=    name
        self.id=      id
        self.address= address

    @classmethod
    def create_company_object(cls):
        print("To proceed further.....")
        name=    input("Enter Company's name:    ")
        id=      input("Enter Company's ID:      ")
        address= input("Enter Company's address: ")
        company_info = company.create_company_object
        return cls(name,id,address)


    def company_interface():
        type_1.create_type_1_obj()


class type_1:
    def __init__(self,name,id,address,name_type,model_type):
        super().__init__(name,id,address)
        self.name_type=  name_type
        self.model_type= model_type
    @classmethod
    def create_type_1_obj(cls):
        name_type=  input("Enter the Type you wish to add:             ")
        model_type= input("Enter the Model name of the type you added: ")


company.create_company_object()
company.company_interface()