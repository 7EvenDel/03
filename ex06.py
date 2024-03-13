def count_negative(a, b, c):
  negative_count = 0
  if a < 0:
    negative_count += 1
  if b < 0:
    negative_count += 1
  if c < 0:
    negative_count += 1

  return negative_count

def count_positive(a, b, c):
  positive_count = 0
  if a > 0:
    positive_count += 1
  if b > 0:
    positive_count += 1
  if c > 0:
    positive_count += 1

  return positive_count

def count_integer(a, b, c):
  integer_count = 0
  if a.is_integer():
    integer_count += 1
  if b.is_integer():
    integer_count += 1
  if c.is_integer():
    integer_count += 1

  return integer_count

def count_divisible(a, b, c, k):
  print("Число k є дільником:")
  if a % k == 0:
    print("a = ", a)
  if b % k == 0:
    print("b = ", b)
  if c % k == 0:
    print("c = ", c)

  print("Жодного з чисел a, b, c.")


a = float(input("Введіть число a: "))
b = float(input("Введіть число b: "))
c = float(input("Введіть число c: "))


negative_count = count_negative(a, b, c)
print("Кількість негативних чисел: ", negative_count)


positive_count = count_positive(a, b, c)
print("Кількість додатних чисел: ", positive_count)


integer_count = count_integer(a, b, c)
print("Кількість цілих чисел: ", integer_count)


k = int(input("Введіть число k: "))
count_divisible(a, b, c, k)