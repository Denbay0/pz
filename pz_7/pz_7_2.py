"""
2. Дана строка, содержащая латинские буквы и круглые скобки. Если скобки
расставлены правильно (то есть каждой открывающей соответствует одна
закрывающая), то вывести число 0. В противном случае вывести или номер позиции,
в которой расположена первая ошибочная закрывающая скобка, или, если
закрывающих скобок не хватает, число —1.
"""
def main():
    string = input("Введите строку, содержащую латинские буквы и круглые скобки: ")
    result = check_brackets(string)
    if result == 0:
        print("Скобки расставлены правильно")
    elif result == -1:
        print("Не хватает закрывающих скобок")
    else:
        print(f"Ошибка в позиции {result}")

def check_brackets(string):
    stack = []
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                return i + 1
    if stack:
        return -1
    return 0

if __name__ == "__main__":
    main()
