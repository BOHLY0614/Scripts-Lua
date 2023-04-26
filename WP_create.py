from Waypoint import *
import numpy as np


# On point vers le bon dossier
file_path = "C:/Users/Nicolas BOHLY/Desktop/Scripts Lua/"
file_name = "waypoints.txt"


wp = [Waypoint(0, 10.8527, -75.5678, 100)]
wp.append(Waypoint(1, 40.2345, -75.6789, 150))
wp.append(Waypoint(2, 40.3456, -75.7890, 200))
wp.append(Waypoint(3, 52.8524, -70.7890, 250))


# write the waypoints data to the text file
with open(file_path + file_name, "a") as f:
    f.truncate(0)
    f.writelines("QGC WPL 110\n")
    for Waypoint in wp:
        f.writelines(Waypoint.to_string())

print("Fichier de waypoints crée")
# Il ne reste plus qu'a upload sur MP dan la section 2
