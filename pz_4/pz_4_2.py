def has_odd_digit(n):
    """
    Проверка на наличие нечетных цифр в числе.
    :param n: int, положительное число
    :return: bool, True, если есть нечетные цифры, иначе False
    """
    try:
        # Проверяем корректность входных данных
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Число должно быть целым и положительным.")

        # Проверка наличия нечетных цифр
        while n > 0:
            digit = n % 10  # Последняя цифра числа
            if digit % 2 != 0:
                return True
            n //= 10  # Удаляем последнюю цифру

        return False

    except Exception as e:
        print(f"Ошибка: {e}")
        return False


if __name__ == "__main__":
    try:
        n = int(input("Введите положительное число N: "))
        result = has_odd_digit(n)
        print(f"Результат: {'TRUE' if result else 'FALSE'}")
    except ValueError:
        print("Ошибка: Введите целое положительное число.")
