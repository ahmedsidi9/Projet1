import math

# Initialisation des variables
F = 10000  # en N
E = 210  # en GPa = 10^3 N/mm^2
L = 100  # en mm

# poutre rectangulaire
b = 10  # en mm
h = 20  # en mm

I_rectangulaire = b*h**3/12

delta_max1=  F*(L^3)/3*E*I_rectangulaire

# poutre carrée
a = 15  # en mm
I_carrée = a**4/12

delta_max2=  F*(L^3)/3*E*I_carrée

# poutre ronde
d = 5  # en mm
I_ronde= (math.pi*d**4)/64

delta_max3 =  F*(L^3)/3*E*I_ronde

# poutre creuse
D = 15  # en mm
d = 5  # en mm
I_creuse = math.pi*(D**4-d**4)/64

delta_max4=  F*(L^3)/3*E*I_creuse


# Calcul de la section optimale

delta_optimal = min(delta_max1, delta_max2, delta_max3, delta_max4)

# TRouver le type de section minimisant la déformation

if delta_optimal==delta_max1:
    type_section = "rectangulaire"

elif delta_optimal==delta_max2:
    type_section= "carrée"

elif delta_optimal == delta_max3:
    type_section = "ronde"

else:
    type_section = "creuse"

# affichage de la section optimale

print(f" Le type de section minimisant la déformation maximale est {type_section}, avec une déformation de {round(delta_optimal,2)} ")

