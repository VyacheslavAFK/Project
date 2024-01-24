num1 = int(input("Введите первое число:"))
num2 = int(input("Введите второе число:"))

print()

print(f"результат сложения {num1} и {num2}:", num1 + num2)
print(f"результат вычитания {num2} из {num1}:", num1 - num2)
print(f"результат умножения {num1} и {num2}:", num1 * num2)
print(f"результат деления числа {num1} на {num2}:", num1 / num2)
print(f"результат возведения числа {num1} степень {num2}:", num1 ** num2)
print(f"результат деления с остатком числа {num1} на {num2}:", num1 // num2)

space = "\n"

print(space * 3, end="\t" * 2)
print("Programm finished!")