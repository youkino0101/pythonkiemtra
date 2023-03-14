from shape.Rect import Rect
from shape.Circle import Circle
from shape.Triangle import Triangle
from collections import Counter
shapes = []
with open("input.txt", "r") as file:
    while (True):
        line = file.readline()
        if line == "":
            break
        if (line.strip() == "#Circle"):
            shapes.append(Circle(file.readline()))
        elif line.strip() == "#Rect":
            line = file.readline()
            data = line.strip().split()
            width = float(data[0])
            height = float(data[1])
            rect = Rect(width, height)
            shapes.append(rect)
        elif line.strip() == "#Triangle": 
            line = file.readline()
            data = line.strip().split()
            a = float(data[0])
            b = float(data[1])
            c = float(data[2])
            shapes.append(Triangle(a, b, c))

max_perimeter_shape = max(shapes, key=lambda shape: shape.chuVi())
max_area_shape = max(shapes, key=lambda shape: shape.dienTich())

print("Hình có chu vi lớn nhất:")
print(max_perimeter_shape.__class__.__name__)
print("Chu vi:", max_perimeter_shape.chuVi())

print("Hình có diện tích lớn nhất:")
print(max_area_shape.__class__.__name__)
print("Diện tích:", max_area_shape.dienTich())

overlapping_shapes = []

for i, shape1 in enumerate(shapes):
    for j, shape2 in enumerate(shapes):
        if i != j and shape1.isOverlapping(shape2):
            overlapping_shapes.append((i, j))

overlapping_count = Counter(overlapping_shapes)
most_overlapping_shapes = overlapping_count.most_common(1)

if most_overlapping_shapes:
    (i, j), count = most_overlapping_shapes[0]
    shape1 = shapes[i]
    shape2 = shapes[j]
    print(f"{count} hình nằm chồng lên nhau nhiều nhất:")
    print(f"{shape1.__class__.__name__} tại vị trí ({shape1.x}, {shape1.y})")
    print(f"{shape2.__class__.__name__} tại vị trí ({shape2.x}, {shape2.y})")
else:
    print("Không có hình nào nằm chồng lên nhau.")