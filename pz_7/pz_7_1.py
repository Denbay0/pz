"""
1. Дано целое число N (32 < N < 126). Вывести символ с кодом, равным N.
"""
def main():
    N = int(input("Введите число N (33 < N < 126): "))
    if 32 < N < 126:
        print("Символ с кодом N:", chr(N))
    else:
        print("Ошибка: число N должно быть в диапазоне от 33 до 125")

if __name__ == "__main__":
    main()
