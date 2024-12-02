def desenhar_grade_2_2():
    horizontal()
    bloco_vertical()
    horizontal()
    bloco_vertical()
    horizontal()

def desenhar_grade_4_4():
    horizontal_2()
    bloco_vertical_2()
    horizontal_2()
    bloco_vertical_2()
    horizontal_2()
    bloco_vertical_2()
    horizontal_2()
    bloco_vertical_2()
    horizontal_2()
    
   
    
def horizontal():
    print("+ " + 3 * "- " + "+ " + 3 * "- " + "+ ")
    
def horizontal_2():
    print("+ " + 3 * "- " + "+ " + 3 * "- " + "+ " + 3 * "- " + "+ " + 3 * "- " + "+" )
    
def vertical():
    print("| " + 3 * "  " + "| "+ 3 * "  " + "| ")

def vertical_2():
    print("| " + 3 * "  " + "| "+ 3 * "  " + "| "+ 3 * "  " + "| "+ 3 * "  " + "| ")
    
def bloco_vertical():
    vertical()
    vertical()
    vertical()
    vertical()
    
def bloco_vertical_2():
    vertical_2()
    vertical_2()
    vertical_2()
    vertical_2()
    
desenhar_grade_2_2()
desenhar_grade_4_4()