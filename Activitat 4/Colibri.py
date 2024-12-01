class Colibri:
    # Constructor 
    def __init__(self, nom, especie, color, extremitats):
        #Atributs
        self.nom = nom
        self.especie = especie
        self.color = color
        self.extremitats = extremitats

    # Getters i Setters
    def getNom(self):
        return self.nom
    def setNom(self, new_nom):
        self.getNom = new_nom

    def getEspecie(self):
        return self.especie
    def setEspecie(self, new_especie):
        self.getEspecie = new_especie    

    def getColor(self):
        return self.color
    def setColor(self, new_color):
        self.marca = new_color 
    
    def getExtremitats(self):
        return self.extremitats
    def setExtremitats(self, new_extremitats):
        self.extremitats = new_extremitats 
