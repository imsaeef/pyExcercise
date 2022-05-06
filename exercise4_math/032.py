import math

radius = int(input('enter the radius of the circle: '))
depth = int(input('Enter the depth of a cylinder: '))
area = math.pi*(radius**2)
volume = area*depth
print(round(volume, 3))
