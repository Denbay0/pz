def descending_numbers(a, b):
    """
    Вывод чисел от B-1 до A+1 в порядке убывания и их количества.
    :param a: int, меньшее число
    :param b: int, большее число
    :return: tuple (list, int), список чисел и их количество
    """
    try:
        # Проверяем корректность входных данных
        if not isinstance(a, int) or not isinstance(b, int):
            raise ValueError("Оба числа должны быть целыми.")
        if a >= b:
            raise ValueError("Число A должно быть меньше числа B.")

        # Генерация списка чисел в порядке убывания
        numbers = list(range(b - 1, a, -1))
        return numbers, len(numbers)

    except Exception as e:
        print(f"Ошибка: {e}")
        return [], 0


if __name__ == "__main__":
    try:
        a = int(input("Введите число A: "))
        b = int(input("Введите число B: "))
        numbers, count = descending_numbers(a, b)
        print(f"Числа: {numbers}")
        print(f"Количество чисел: {count}")
    except ValueError:
        print("Ошибка: Введите целые числа.")
