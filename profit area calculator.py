def areacalculator(): 
    _input_ = input("Enter the shape you want to calculate area of:\n").lower()
    area = 0 
    pie = 3.14
    if _input_ == "square":
        side = int(input("Enter the value of side: "))
        area = area + (side ** 2)
    elif _input_ == "circle":
        radius = int(input("Enter the value of radius: "))
        area = area + (2*pie*radius)
    elif _input_ == "rectangle":
        length = int(input("Enter the value of length: "))
        width = int(input("Enter the value of the width"))
        area = area + (length * width)
    elif _input_ == "triangle":
        length = int(input("Enter the value of length: "))
        width = int(input("Enter the value of the width"))
        area = area + (length * width / 2)
    else:
        print("Select a valid statement")
    print("%.2f" % area)

areacalculator()