import math

def distance(x, y):
  return math.sqrt(x**2 + y**2)

x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())

distance_a = distance(x1, y1)
distance_b = distance(x2, y2)

if distance_a < distance_b:
  print("Точка A ближче")
elif distance_a > distance_b:
  print("Точка B ближче")
else:
  print("Точки розташовані на одинаковій відстані")