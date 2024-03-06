a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))

#1)
negative_count = 0
if a < 0:
  negative_count += 1
if b < 0:
  negative_count += 1
if c < 0:
  negative_count += 1

print("Кількість негативних чисел: ", negative_count)

#2)
positive_count = 0
if a > 0:
  positive_count += 1
if b > 0:
  positive_count += 1
if c > 0:
  positive_count += 1

print("Кількість додатних чисел: ", positive_count)

#3)
is_a_integer = a.is_integer()
is_b_integer = b.is_integer()
is_c_integer = c.is_integer()

integer_count = 0
if is_a_integer:
  integer_count += 1
if is_b_integer:
  integer_count += 1
if is_c_integer:
  integer_count += 1

print("Кількість цілих чисел: ", integer_count)

#4)
k = int(input("Введіть число k: "))

is_a_divisible = a % k == 0
is_b_divisible = b % k == 0
is_c_divisible = c % k == 0
print("Число k є дільником:")
if is_a_divisible:
  print("a = ", a)
if is_b_divisible:
  print("b = ", b)
if is_c_divisible:
  print("c = ", c)

print("Жодного з чисел a, b, c.")