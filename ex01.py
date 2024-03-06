def power(x):
  return x**2 if x >= 0 else x**4
a, b, c = map(float, input("Введіть 3 числа через пробіл ").split())

print(f"a^2 = {power(a)}")
print(f"b^2 = {power(b)}")
print(f"c^2 = {power(c)}")