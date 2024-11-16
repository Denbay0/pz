
def check_odd_or_even(a):
    """
    . Дано целое число A. Проверить истинность высказывания: «Число A является
    нечетным».
    """
    try:
        if a % 2 != 0:
            return "Число нечетное"
        else:
            return "Число четное"
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    try:
        # Ввод числа
        a = int(input("Введите целое число для проверки: "))
        print(check_odd_or_even(a))
    except ValueError:
        print("Ошибка: Введите корректное целое число.")
