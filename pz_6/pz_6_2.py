def find_increasing_elements_indices(lst):
    """
    Дан список размера N. Найти номера тех элементов список, которые больше своего
    левого соседа, и количество таких элементов. Найденные номера выводить в
    порядке их убывания.
    """
    try:
        if not isinstance(lst, list):
            raise ValueError("Входные данные должны быть списком.")
        if len(lst) < 2:
            # Если длина меньше 2, нельзя сравнить с левым соседом
            return [], 0

        indices = []
        for i in range(1, len(lst)):
            if lst[i] > lst[i - 1]:
                indices.append(i)
        # Сортируем индексы в порядке убывания
        indices.sort(reverse=True)

        return indices, len(indices)
    except Exception as e:
        print(f"Ошибка: {e}")
        return [], 0


if __name__ == "__main__":
    try:
        # Пример: пользовательский ввод
        # Для теста можно ввести: 5 3 5 6 2 10
        input_str = input("Введите список чисел через пробел: ")
        # Преобразуем введенную строку в список чисел
        initial_list = list(map(int, input_str.split()))

        indices_list, count = find_increasing_elements_indices(initial_list)

        print("Исходный список:", initial_list)
        print("Индексы элементов, которые больше левого соседа (по убыванию):", indices_list)
        print("Количество таких элементов:", count)
    except ValueError:
        print("Ошибка: введите корректный список целых чисел.")
    except Exception as e:
        print(f"Ошибка: {e}")
