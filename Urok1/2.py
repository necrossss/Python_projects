# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_sec = int(input('Введите число секунд для перевода в формат чч:мм:сс - '))

hh = user_sec // 3600
mm = user_sec % 3600 // 60
ss = user_sec - (hh * 3600 + mm * 60)

print(f'В формате чч:мм:сс - {hh:02}:{mm:02}:{ss:02}')
