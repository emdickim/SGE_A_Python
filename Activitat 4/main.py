from Cotxe import Cotxe
from Colibri import Colibri 


# Instancia objectes Cotxe
cotxe_1 = Cotxe(marca="Toyota", color="Multicolor", rodes=4)
cotxe_2 = Cotxe(marca="Cupra", color="Blanc", rodes=4)
cotxe_3 = Cotxe(marca="Honda", color="Negre", rodes=4)
print(f'La marca del meu cotxe és {cotxe_1.getMarca()}')
print(f'El meu cotxe es de color {cotxe_1.getColor()}')
print(f'El meu cotxe te {cotxe_1.getRodes()} rodes')

# Instancia objectes Colibri
colibri_1 = Colibri(nom="pajarito", especie="Pardo", color="Multicolor", extremitats=4)
colibri_2 = Colibri(nom="piolin", especie="orejimorado", color="Blanc", extremitats=4)
colibri_3 = Colibri(nom="pio", especie="Orejavioleta", color="Negre", extremitats=4)
print(f'El meu colibri es diu {colibri_1.getNom()}')
print(f'El colibri es de la especie {colibri_1.getEspecie}')
print(f'El colibri es de color {colibri_1.getColor()}')
print(f'El meu ocell te {colibri_1.getExtremitats()} extremitats')


# Modificar 2 atributs de Cotxe a través dels setters
cotxe_1.setMarca("Citröen")
cotxe_1.setColor("Lila")


# Mostrar els 2 atributs modificats a través dels getters
print("\nAtributs modificats del Cotxe 1:")
print(f"Marca: {cotxe_1.getMarca()}")
print(f"Color: {cotxe_1.getColor()}")


# Modificar 2 atributs de Colibrí a través dels setters
colibri_1.setNom("Albert")
colibri_1.setColor("verd")

# Mostrar els 2 atributs modificats a través dels getters
print("\nAtributs modificats del Colibrí 1:")
print(f"Color: {colibri_1.getColor()}")
print(f"Extremitats: {colibri_1.getExtremitats()}")