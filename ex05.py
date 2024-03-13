def find_point(x, y):
  if x == 0 and y == 0:
    return "Точка A лежить в початку координат."
  elif x == 0:
    return "Точка A лежить на осі OY."
  elif y == 0:
    return "Точка A лежить на осі OX."
  elif x > 0 and y > 0:
    return "Точка A лежить в першому координатному куті."
  elif x < 0 and y > 0:
    return "Точка A лежить в другому координатному куті."
  elif x < 0 and y < 0:
    return "Точка A лежить в третьому координатному куті."
  else:
    return "Точка A лежить в четвертому координатному куті."

x = float(input("Введіть координату x точки A: "))
y = float(input("Введіть координату y точки A: "))

result = find_point(x, y)
print(result)
