# Normal Constant
name = "Aman"
print (name)

# Constant variables / Coventions 
# All letters in Capital 
PI = 3.1416
print (PI)

# We also can store constants in a different file and import into this file to work
import Constants
print (Constants.PI)

# we also can modify constant values in this file after importing
Constants.PI = 3.141596
print (Constants.PI)
# in that case we are not going to change the mother file but only into this imported file