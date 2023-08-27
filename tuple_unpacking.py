import math

points = [
    (12, 55),
    (880, 123),
    (64, 64),
    (190, 1024),
    (77, 33),
    (42, 11),
    (0, 90)
]

x, y = points[0]
closest_distance = math.sqrt(x ** 2 + y ** 2)

for x, y in points[1:]:
    distance = math.sqrt(x ** 2 + y ** 2)
    if distance < closest_distance:
        closest_distance = distance

print(closest_distance)