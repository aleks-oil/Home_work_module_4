print('Практическое задание "Модули и пакеты"')
from fake_math import divide_fake as fm
from true_math import divide_true as tm
fake_divide = fm
true_divide = tm

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)