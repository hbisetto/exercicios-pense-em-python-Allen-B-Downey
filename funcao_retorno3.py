import math

#Funções
#círculo
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def area(radius):
    a = math.pi * radius**2
    return a

# def circle_area(xc, yc, xp, yp):
#     radius = distance(xc, yc, xp, yp)
#     result = area(radius)
#     return result
# mais consiso:
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))    

## ver se é divisível
# def is_divisible(x, y):
#     if x % y == 0:
#         return True
#     else:
#         return False
# mais conciso:
def is_divisible(x, y):
    return x % y == 0
        
print("Calculating area:")    
area = circle_area(1, 2, 4, 6)
print(area)
print()

x = 8
y = 4
print(f'Is divisible? x = {x} and y = {y}')

if is_divisible(x, y):
    print(f'x ({x}) is divisible by y ({y})')