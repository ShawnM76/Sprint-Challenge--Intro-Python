# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Vehicle is the base class
Class Vehicle:
    pass

Class FlightVehicle(Vehicle):
    pass

Class Starship(FlightVehicle):
    pass

Class GroundVehicle(Vehicle):
    pass

Class Airplane(FlightVehicle):
    pass

Class Car(GroundVehicle):
    pass

Class Motorcycle(GroundVehicle):
    pass
