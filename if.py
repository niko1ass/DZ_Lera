w = input("введите знак (+, -, *, /): ")

a = float(input("введитие первое число: "))
b = float(input("введитие второе число: "))
с = float(input("введитие третье число: "))

if w == "+":
	c = a + b + с
	print("Результат: " + str(c))
elif w == "-":
	c = a - b - с
	print("Результат: " + str(c))
elif w == "*":
	c = a * b * с
	print("Результат: " + str(c))
elif w == "/":
	c = a / b / с
	print("Результат: " + str(c))
else:
	print("ERROR")
