import random
def generate_x_y():
    x = random.randint(0,20)
    y = random.randint(0,20)
    return str(x) + " " + str(y) + "\n"
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False
def generate_input_file():
    with open("input.txt", "a") as f:
        r = "#Rect"
        f.write(r + "\n")
        f.write(generate_x_y())
        f.write(generate_x_y())
        c = "#Cricle"
        f.write(c + "\n")
        f.write(str(random.randint(0,20)) + "\n")
        f.write(generate_x_y())
        t = "#Triangle"
        f.write(t + "\n")
        while(True) :
            a = random.randint(0,20)
            b = random.randint(0,20)
            c = random.randint(0,20)
            if (is_triangle(a, b, c)) :
                f.write(str(a) + " " + str(b) + " " + str(c) +"\n")
                break
        f.write(generate_x_y())
for i in range(1000):
    generate_input_file()