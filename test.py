import pickle
import re

# Исходный текст
testText = 'Привет как дела'

# Шифровка
print('Шифровка:')
testBin = pickle.dumps(testText)
print(f"Размер сериализованного объекта: {len(testBin)} байт")
print(testBin)  # Выводим сериализованный объект

# Преобразуем сериализованный объект в строку
testBinText = ' '.join([f'\\x{hex(b)[2:].zfill(2)}' for b in testBin])  # Переводим в формат \x00
print(f"Размер строки после преобразования в строку: {len(testBinText)} символов")
print(testBinText)

# Разделяем на компоненты
arr = testBinText.split(' ')
print(f"Количество элементов после split: {len(arr)}")
print(arr)

# Переводим элементы в массив чисел в формате шестнадцатеричных значений
arr2 = []
for i in arr:
    arr2.append(i.split('\\x'))
print(f"Размер массива после split('\\x'): {len(arr2)}")
print(arr2)

# Шифруем: каждое число увеличиваем, например, на 2, и умножаем на 2
arr3 = []
for i in arr2:
    res = []
    for j in i:
        if len(j) > 0:
            # Обработка значений в десятичной системе
            new_value = (int(j, 16) + 2) * 2
            res.append(str(new_value))
    arr3.append(res)
print(f"Размер массива после шифрования: {len(arr3)}")
print(arr3)

# Дешифровка: делим на 2 и вычитаем 2
print('Дешифровка:')
arr4 = []
for i in arr3:
    res = []
    for j in i:
        # Восстанавливаем оригинальные байты
        new_value = (int(j) / 2) - 2
        res.append(hex(int(new_value)))
    arr4.append(res)
print(f"Размер массива после дешифровки: {len(arr4)}")
print(arr4)

# Убираем префикс '0x' из значений
arr5 = []
for i in arr4:
    res = []
    for j in i:
        res.append(j[2:])
    arr5.append(res)
print(f"Размер массива после удаления '0x' префикса: {len(arr5)}")
print(arr5)

# Формируем строку из элементов массива
arr6 = []
for i in arr5:
    res = []
    for j in i:
        if len(j) < 2:
            res.append(f'\\x0{j}')
        else:
            res.append(f'\\x{j}')
    textRes = ''.join(res)
    arr6.append(textRes)
print(f"Размер массива после формирования финальной строки: {len(arr6)}")
print(arr6)

# Собираем финальную строку
finBinText = ' '.join(arr6)
print(f"Размер финальной строки: {len(finBinText)} символов")
print(finBinText)

# Убираем все символы, которые не являются шестнадцатеричными числами
cleaned_text = ''.join(finBinText.split()).replace("\\x", "")
print(f"Размер строки после очистки: {len(cleaned_text)} символов")
print(f"Очистенная строка: {cleaned_text}")

# Преобразуем строку в байты
finBinBytes = bytes.fromhex(cleaned_text)
print(f"Размер байтов после преобразования: {len(finBinBytes)} байт")
print(finBinBytes)

# Десериализация
try:
    fin = pickle.loads(finBinBytes)
    print("Расшифрованнй текст:")
    print(fin)
except Exception as e:
    print(f"Ошибка при загрузке данных: {e}")
