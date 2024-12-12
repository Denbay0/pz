def zero_between_min_and_max(lst):
    """
    Дан список размера N. Обнулить элементы списка, расположенные между его
    минимальным и максимальным элементами (не включая минимальный и
    максимальный элементы).
    """
    try:
        if not isinstance(lst, list):
            raise ValueError("Входные данные должны быть списком.")
        if len(lst) < 2:
            # Если список слишком короткий, нет смысла что-то обнулять
            return lst

        min_val = min(lst)
        max_val = max(lst)

        min_index = lst.index(min_val)
        max_index = lst.index(max_val)

        # Определяем границы
        start = min(min_index, max_index)
        end = max(min_index, max_index)

        # Обнулить все элементы между min и max (не включая сами min и max)
        for i in range(start + 1, end):
            lst[i] = 0

        return lst
    except Exception as e:
        print(f"Ошибка: {e}")
        return lst


if __name__ == "__main__":
    try:
        # Пример: ввод
        # Например: 4 7 1 9 3 8
        input_str = input("Введите список чисел через пробел: ")
        initial_list = list(map(int, input_str.split()))

        # Копия для отображения исходного списка
        original_list = initial_list[:]
        result_list = zero_between_min_and_max(initial_list)

        print("Исходный список:", original_list)
        print("Результирующий список:", result_list)
    except ValueError:
        print("Ошибка: введите корректный список целых чисел.")
    except Exception as e:
        print(f"Ошибка: {e}")
