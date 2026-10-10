#Ningaloo Reef Field Tracker-Turtles hatchling
vulnerable_species = ["leatherback","loggerhead","olive Ridley","flatback"]
endangered_species = ["green"]
critically_species = ["kemp's ridley","hawksbill"]
name_species = input("Enter the name of the specie").lower()
sand_temperature = float(input("Enter the temperature of the sand"))
if name_species in vulnerable_species :
    statut_conservation = "The specie is in a vulnerable statut"

elif name_species in endangered_species :
    statut_conservation = "The specie is in a Endangered statut"

elif name_species in critically_species :
    statut_conservation = "The specie is in a Critically Endangered statut"

else:
 statut_conservation ="The specie is not part of defined in the local base "

if sand_temperature >= 31.0 :
    sex ="Female"

elif sand_temperature <= 28.0 :
    sex = "Male"

else :
    sex = "Balanced ratio"

print("======THE MISSION REPORT======")
print(f"Species     :    {name_species}")
print(f"Statut      :    {statut_conservation}")
print(f"Temperature :    {sand_temperature}°C")
print(f"Predicted Gender : {sex}")
print("==============================")