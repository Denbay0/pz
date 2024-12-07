from math import sqrt


def mean(x, y):
    """
    Вычисляет среднее арифметическое и геометрическое двух положительных чисел.

    :param x: Первое положительное число.
    :param y: Второе положительное число.
    :return: Кортеж (среднее арифметическое, среднее геометрическое).
    """
    try:
        if x <= 0 or y <= 0:
            raise ValueError("Числа должны быть положительными.")
        a_mean = (x + y) / 2
        g_mean = sqrt(x * y)
        return a_mean, g_mean
    except TypeError:
        raise TypeError("Аргументы должны быть числами.")
    except ValueError as e:
        raise ValueError(str(e))


if __name__ == "__main__":
    # Входные данные
    a, b, c, d = 4, 16, 9, 25

    # Вычисления для каждой пары
    pairs = [(a, b), (a, c), (a, d)]
    for pair in pairs:
        try:
            a_mean, g_mean = mean(*pair)
            print(f"Пара {pair}: Среднее арифметическое = {a_mean}, Среднее геометрическое = {g_mean}")
        except Exception as e:
            print(f"Ошибка для пары {pair}: {e}")
