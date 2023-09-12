import calendar

print("Добро пожаловать в супер календарь\n")

year = int(input("Введите год: "))
month = int(input("Введите номер месяца: "))

print("\n", calendar.month(year, month))

print("Всего хорошего!")