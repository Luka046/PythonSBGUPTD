def join_words():
    n = int(input("Введите количество слов: "))
    result = ""
    for i in range(n):
        word = input(f"Введите слово {i + 1}: ")
        result += word + " "
    print("Результат:", result.strip())

join_words()