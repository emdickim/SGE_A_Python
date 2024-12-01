class Cotxe:
    # Constructor 
    def __init__(self, marca, color, rodes):
        #Atributs
        self.marca = marca
        self.color = color
        self.rodes = rodes

    # Getters i Setters
    def getMarca(self):
        return self.marca
    def setMarca(self, new_marca):
        self.marca = new_marca    

    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.color = new_color 
    
    def getRodes(self):
        return self.rodes
    def setRodes(self, new_rodes):
        self.rodes = new_rodes 


