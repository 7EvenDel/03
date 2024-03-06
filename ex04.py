def replace_numbers(x, y):

  # Перевірка, чи числа дійсні
  if x==y:
    print("Введені значення повинні бути не рівними")
    return

  if x < y:
    min_num = x
    max_num = y
  else:
    min_num = y
    max_num = x

  min_num = (min_num + max_num) / 2
  max_num = 2 * min_num * max_num

  return min_num, max_num

x = float(input("Введіть число x: "))
y = float(input("Введіть число y: "))

min_num, max_num = replace_numbers(x, y)


print("Мінімальне число після заміни:", min_num)
print("Максимальне число після заміни:", max_num)