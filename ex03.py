def check(a,b):
    sum = a + b
    if sum > 180:
        print("Трикутник не існує")
        return
    if a==90 or b==90:
        print("Трикутник існує і він є прямокутним")
    else:
        print("Трикутник не прямокутний")

a = float(input("Введіть градусну міру першого кута: "))
b = float(input("Введіть градусну міру другого кута: "))

check(a, b)