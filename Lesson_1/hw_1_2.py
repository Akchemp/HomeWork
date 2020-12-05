# Задача_2: Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

time_in_sec = int(input("Введите время в секундах: "))
hours = time_in_sec // 3600
ostatok = time_in_sec % 3600
minutes = ostatok // 60
seconds = ostatok % 60
print(f"Время в секундах {hours:02}:{minutes:02}:{seconds:02}")


