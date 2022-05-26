class Item():

    def __init__(self):
        self.name = None
        self.description = None
        self.gender = None

    def get_description(self):
        return self.description

    def set_description(self, my_description):
        self.description = my_description

    def get_name(self):
        return self.name

    def set_name(self, my_name):
        self.name = my_name


    def get_gender(self):
        return self.gender

    def set_gender(self, my_gender):
        self.gender = my_gender
        
