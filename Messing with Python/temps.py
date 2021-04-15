celsius = int(input("Enter a number: "))


def fahrenheit(num):
    return round(1.8*num + 32, 1)


print("The Fahrenheit equivalent of " + str(celsius) + " degrees Celsius is " + str(fahrenheit(celsius)) + ".")
