import copy

class Point:
    """ Represents a point in 2-D space.
    """

class Rectangle:
    """Represents a rectangle.
       attributes: width, height, corner.
    """

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))
    
def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

def move_rectangle(rec):
    new_rec = copy.deepcopy(rec)
    return new_rec
    
blank = Point()
blank.x = 3.0
blank.y = 4.0
print_point(blank)
    
box = Rectangle()
box.width = 100.00
box.height = 200.00
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0
print(box.corner.x)
print(box.corner.y)
print(box.corner)

center = find_center(box)
print_point(center)
new_rec = move_rectangle(box)
print(new_rec)
print(box)
print(new_rec is box)

# Ver se o objeto é a estância de uma classe
isinstance(blank, Point)
print(isinstance(blank, Point))
# Verificar se tem algum atributo específico
hasattr(blank, 'x')
print(hasattr(blank, 'x'), hasattr(blank, 'z'))