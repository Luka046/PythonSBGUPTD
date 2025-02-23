def join_words_until_stop():
    result = ""
    while True:
        word = input("Введите слово (или 'stop' для завершения): ")
        if word.lower() == "stop":
            break
        result += word + " "
    print("Результат:", result.strip())

join_words_until_stop()