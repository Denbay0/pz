def generate_powers_of_two():
    """
    Сформировать и вывести целочисленный список размера 10, содержащий степени
    двойки от первой до 10-й: 2, 4, 8,16, ... .
    """
    # Исходный список степеней двойки от 1 до 10
    powers = [2 ** i for i in range(1, 11)]
    return powers


if __name__ == "__main__":
    try:
        # Формирование списка
        initial_list = list(range(1, 11))  # Для демонстрации "исходного" списка
        result_list = generate_powers_of_two()

        # Вывод исходного и результирующего списков
        print("Исходный список (номера степеней от 1 до 10):", initial_list)
        print("Результирующий список (степени двойки):", result_list)
    except Exception as e:
        print(f"Ошибка: {e}")
