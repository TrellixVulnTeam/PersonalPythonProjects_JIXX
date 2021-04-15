import random
import math

var1 = random.randint(10, 25)
var2 = random.randint(200, 400)

print("Your car can hold " + str(var1) + " gallons of gas, and it can travel " + str(var2) + " miles.")
print("Your gas mileage is " + str(math.floor(var2/var1)) + " miles per gallon.")
