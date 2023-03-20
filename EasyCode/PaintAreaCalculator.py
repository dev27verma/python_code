import math

height_of_wall = int(input("Height of wall: "))
width_of_wall = int(input("Width of wall: "))
coverage_per_Can = 5

def paint_calc(height, width, coverage):
    can_required = height * width /coverage
    print("Can required for wall ", round(math.ceil(can_required)))

paint_calc(height_of_wall,width_of_wall,coverage_per_Can)