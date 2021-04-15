length = int(input("Length: "))
width = int(input("Width: "))
height = int(input("Height: "))


def volume(x, y, z):
    return x * y * z


print("The volume of the rectangular prism is " + str(volume(length, width, height)) + " cubic feet.")
