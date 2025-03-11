class Human:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


class Archer(Human):
    def __init__(self, name, num_arrows):
        super().__init__(name)
        self.__num_arrows = num_arrows

    def get_num_arrows(self):
        return self.__num_arrows
    

#Archer erft van Human, gebruikt super().__init__(name) om de naam in te 
# stellen en voegt de __num_arrows eigenschap toe. De methode 
#get_num_arrows retourneert het aantal pijlen.